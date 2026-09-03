# pdfyier

Turn a batch of images into a single PDF, right in the browser. Drag to reorder pages, name your file, and download — nothing you upload is ever written to disk or kept around after your download finishes.

**Live:** https://pdfyier.latesailor.dev

## What it does

- Drop or select multiple images (JPG, PNG, WEBP, BMP, TIFF, GIF)
- Reorder pages by dragging thumbnails
- Name the downloaded file
- Converts everything into one multi-page PDF and streams it straight back

## How it works

```
browser (drag/drop images)
   → nginx (TLS termination, request size limit, rate limiting on /convert)
   → FastAPI (validates file type/size, saves to RAM-backed temp storage)
   → ImageMagick CLI (decodes images, renders each as a PDF page)
   → FastAPI reads the finished PDF into memory, deletes the temp files
   → response streamed back over HTTPS
   → browser downloads the PDF
```

The whole pipeline runs inside a single request/response cycle. Nothing is written to persistent disk at any point — temp storage is `tmpfs` (RAM-backed) on both the host and inside the container — and nothing is logged beyond standard access-log fields (IP, timestamp, path, status code).

## Stack

| Layer | Tech |
|---|---|
| Frontend | Static HTML/CSS/vanilla JS (no build step) |
| Backend | FastAPI (Python) |
| Conversion | ImageMagick (`magick` CLI, shelled out via `subprocess`) |
| Reverse proxy | nginx — TLS, request size limits, rate limiting |
| TLS | Let's Encrypt via Certbot, auto-renewing |
| Container | Docker + Docker Compose |
| Host | Oracle Cloud VM (Ubuntu) |

## Project structure

```
pdfyier/
├── index.html          # Frontend — drop zone, reorderable grid, filename input, info panels
├── favicon.svg          # Site favicon
├── main.py              # FastAPI app (/health, /convert)
├── requirements.txt      # Python dependencies
├── Dockerfile            # Python + ImageMagick, with PDF policy patch
└── docker-compose.yml    # Container config, tmpfs mount for /tmp
```

## Running locally

**With Docker (recommended):**
```bash
docker-compose up -d --build
```
API will be live at `http://localhost:8000`.

**Serve the frontend:**
```bash
python -m http.server 5500
```
Open `http://localhost:5500/index.html` — it auto-detects `localhost` and points at the local API.

> Frontend must be served over `http://`, not opened as a `file://` URL — browsers block cross-origin requests from local files.

## API

### `GET /health`
Returns `{"status": "ok"}`.

### `POST /convert`
Multipart form upload, field name `files` (repeatable, order = page order).

**Limits (enforced server-side):**
- Max 50 files per request
- Max 20MB per file
- Max 150MB total per request
- Allowed extensions: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`, `.gif`

**Response:** `application/pdf` binary stream on success, JSON `{"detail": "..."}` with an appropriate 4xx/5xx status on failure.

## Deployment notes

- `index.html` is served directly by nginx as a static file from `/var/www/pdfyier/` — it is **not** served from the git checkout, so after pulling changes on the server, copy the updated file into place:
  ```bash
  sudo cp index.html favicon.svg /var/www/pdfyier/
  ```
- `main.py` changes require rebuilding the container:
  ```bash
  docker-compose up -d --build
  ```
- `docker-compose.yml`-only changes (no Dockerfile edits) just need a recreate:
  ```bash
  docker-compose up -d --force-recreate
  ```

## Security posture

- HTTPS everywhere (Certbot-managed cert, auto-renews)
- No persistent storage — uploads and generated PDFs live only in RAM (`tmpfs`) for the duration of a single request
- No database, no accounts, no cookies
- Access logs capture only IP/timestamp/path/status — never filenames or file contents
- File type allowlist and size limits enforced at both nginx and application level
- Rate limiting on `/convert` (the only compute-heavy endpoint) to prevent abuse
- CORS restricted to the deployed frontend origin

## License / usage

Personal project — built as a learning exercise in deploying a small full-stack tool end to end (containerized backend, reverse proxy, TLS, static frontend, basic hardening).
