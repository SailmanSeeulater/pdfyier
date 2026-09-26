import os
import subprocess
import tempfile
import uuid

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Image to PDF Service")

# Allow the frontend (served from anywhere for now) to call this API.
# Tighten allow_origins to your actual domain once deployed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pdfyier.latesailor.dev", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".gif"}
MAX_FILES = 50
MAX_FILE_SIZE = 20 * 1024 * 1024       # 20 MB per file
MAX_TOTAL_SIZE = 150 * 1024 * 1024     # 150 MB per request


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/convert")
async def convert(files: list[UploadFile]):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")
    if len(files) > MAX_FILES:
        raise HTTPException(status_code=400, detail=f"Max {MAX_FILES} files per request")

    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        total_size = 0

        # Save uploads in the order they were sent (this becomes page order)
        for idx, f in enumerate(files):
            ext = os.path.splitext(f.filename or "")[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                raise HTTPException(status_code=400, detail=f"Unsupported file type: {f.filename}")

            content = await f.read()

            if len(content) > MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=413,
                    detail=f"{f.filename} exceeds {MAX_FILE_SIZE // (1024*1024)}MB limit",
                )

            total_size += len(content)
            if total_size > MAX_TOTAL_SIZE:
                raise HTTPException(
                    status_code=413,
                    detail=f"Total upload size exceeds {MAX_TOTAL_SIZE // (1024*1024)}MB limit",
                )

            # Prefix with index to guarantee order regardless of original filename
            safe_name = f"{idx:03d}_{uuid.uuid4().hex}{ext}"
            path = os.path.join(tmp, safe_name)
            with open(path, "wb") as out:
                out.write(content)
            paths.append(path)

        output_path = os.path.join(tmp, "output.pdf")
        # -auto-orient applies each photo's EXIF rotation, so portrait phone shots
        # land upright in the PDF (they already look upright in the browser preview).
        cmd = ["magick", *paths, "-auto-orient", output_path]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            raise HTTPException(status_code=500, detail="Conversion took too long. Try fewer or smaller images.")
        if result.returncode != 0:
            # Keep ImageMagick's stderr (paths, versions) out of the response.
            raise HTTPException(
                status_code=500,
                detail="Couldn't convert these images. One of them may be damaged or in an unusual format.",
            )

        if not os.path.exists(output_path):
            raise HTTPException(status_code=500, detail="Conversion produced no output")

        # Read into memory before the temp dir is cleaned up on context exit
        with open(output_path, "rb") as f:
            pdf_bytes = f.read()

    # Write to a short-lived temp file for FileResponse, or return bytes directly
    from fastapi.responses import Response
    return Response(content=pdf_bytes, media_type="application/pdf",
                     headers={"Content-Disposition": "attachment; filename=output.pdf"})
