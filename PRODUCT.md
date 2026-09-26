# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Everyday people who need several images turned into one PDF: receipts, scanned pages, phone photos of documents, homework, forms. They arrive with a handful of files, want them in the right order under a sensible name, and want to leave with a PDF in under a minute. They care that their files are not kept anywhere.

## Product Purpose

pdfyier turns a batch of images into a single multi-page PDF in the browser. Drop or pick images, drag to set page order, name the file, download. Success is a correct PDF in the visitor's downloads with no sign-up, no waiting room, and no copy left behind on the server.

## Positioning

Privacy by construction, not by promise: uploads live only in RAM-backed temp storage for the length of one request, are converted by ImageMagick on the project's own server, and are deleted before the response finishes. No accounts, no tracking cookies, no third parties. The site is open about exactly how that pipeline works.

## Operating Context

- Used on desktop and phone browsers, usually as a one-off task with files already on hand.
- Single request/response pipeline: browser → nginx (TLS, size limits, rate limiting) → FastAPI → `magick` CLI → PDF streamed back.
- Found through search; the page is also the site's only landing page (`https://pdfyier.latesailor.dev/`).

## Capabilities and Constraints

- Accepted formats: JPG, JPEG, PNG, WEBP, BMP, TIFF, GIF.
- Limits enforced server-side: 50 files per request, 20 MB per file, 150 MB per request.
- Features: drop or select files, drag-to-reorder thumbnails with page numbers, remove single file, clear all, custom filename (always `.pdf`), upload progress, a technical "how it works" explainer, Privacy / Terms / Help panels.
- Static HTML/CSS/vanilla JS frontend, no build step. Backend is FastAPI in Docker.
- Not decided: HEIC/HEIF (iPhone default photo format) is not accepted today.

## Brand Commitments

- Name is `pdfyier`, lowercase in prose.
- `favicon.svg` stays as it is.
- The owner asked for the product to feel luxurious and like a first-party Apple product, in the mood of Apple's dark Pro product pages rather than the bright Apple Store look.

## Evidence on Hand

- Real privacy, terms, and help copy in `index.html`; it may be tightened but must not gain new claims.
- The pipeline description in `Readme.md` and the in-page explainer.
- No testimonials, usage numbers, press, or reviews exist; none may be invented.

## Product Principles

1. The task comes first: a first-time visitor can add files, order them, and download without reading anything.
2. Privacy is shown through how the product behaves and explains itself, never through vague reassurance.
3. Nothing extra: no accounts, no upsells, no feature that stores anything.
4. Every claim on the page must be true of the running system.

## Accessibility & Inclusion

No product-specific standard set; WCAG 2.2 AA is the working floor (keyboard-reachable drop target and reordering, readable contrast, reduced motion respected).
