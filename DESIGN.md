---
name: pdfyier
description: Images in, one PDF out, nothing kept. A lit stage in the dark, a ruled notebook in the light.
colors:
  # Dark theme, "Cyclorama Dawn" (default when the OS is dark)
  sky-black: "#000000"
  ink-white: "#f5f5f7"
  ink-silver: "#a1a1a6"
  ink-graphite: "#86868b"
  sheet-charcoal: "#1c1c1e"
  field-charcoal: "#161618"
  field-charcoal-hover: "#1f1f22"
  control-graphite: "#3a3a3c"
  fill-1: "rgb(255 255 255 / 0.07)"
  fill-2: "rgb(255 255 255 / 0.11)"
  fill-3: "rgb(255 255 255 / 0.16)"
  hairline: "rgb(255 255 255 / 0.1)"
  cobalt-lamp: "#2448ff"
  horizon-core: "#d6deff"
  cobalt-signal: "#7c95ff"
  rose-lamp: "#f0629a"
  rose-rim: "#ffb8d0"
  day-lamp: "#fff4ec"
  alert-red: "#ff453a"
  # Paper theme, "ruled college notebook" (default when the OS is light)
  paper-white: "#fbfbf8"
  paper-ink: "#1f2433"
  paper-ink-soft: "#4f5566"
  paper-ink-faint: "#5f6576"
  ballpoint-blue: "#1d3a9a"
  ballpoint-blue-hover: "#2447b8"
  red-pen: "#c62f2e"
  notebook-rule: "#d3e2f1"
  margin-red: "#e27474"
  highlighter-yellow: "#ffe240"
  masking-tape: "#ece2c4"
  photo-white: "#ffffff"
  paper-fill-1: "rgb(29 58 154 / 0.05)"
  paper-fill-2: "rgb(29 58 154 / 0.09)"
  paper-fill-3: "rgb(29 58 154 / 0.14)"
  paper-hairline: "rgb(31 36 51 / 0.14)"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "64px"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.022em"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "48px"
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-0.022em"
  lede:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "-0.012em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.016em"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: "-0.01em"
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: "-0.01em"
    fontFeature: "tnum"
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, Inter, Segoe UI, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  mono:
    fontFamily: "ui-monospace, SF Mono, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0"
  paper-display:
    fontFamily: "Kalam, Bradley Hand, Segoe Print, cursive"
    fontSize: "68px"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0"
  paper-headline:
    fontFamily: "Kalam, Bradley Hand, Segoe Print, cursive"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0"
  paper-note:
    fontFamily: "Kalam, Bradley Hand, Segoe Print, cursive"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: "0"
rounded:
  sheet: "3px"
  code: "6px"
  pre: "12px"
  field: "14px"
  pill: "999px"
  taped-photo: "1px"
  hand-pill: "255px 20px 225px 20px / 20px 225px 20px 255px"
  hand-circle: "55% 45% 52% 48% / 48% 55% 45% 52%"
spacing:
  gutter: "24px"
  gutter-compact: "16px"
  wide: "1120px"
  dock: "632px"
  control-gap: "12px"
  row-gap: "34px"
  page-h: "176px"
  page-h-md: "150px"
  page-h-sm: "118px"
  notebook-rule: "32px"
  section: "150px"
components:
  button-primary:
    backgroundColor: "{colors.ink-white}"
    textColor: "{colors.sky-black}"
    rounded: "{rounded.pill}"
    typography: "{typography.body}"
    height: "50px"
    padding: "0 28px"
  button-primary-hover:
    backgroundColor: "#ffffff"
  button-primary-disabled:
    backgroundColor: "#1d1d1f"
    textColor: "{colors.ink-graphite}"
  button-secondary:
    backgroundColor: "{colors.fill-2}"
    textColor: "{colors.ink-white}"
    rounded: "{rounded.pill}"
    height: "44px"
    padding: "0 22px"
  button-secondary-hover:
    backgroundColor: "{colors.fill-3}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink-silver}"
    rounded: "{rounded.pill}"
    height: "34px"
    padding: "0 14px"
  button-text-hover:
    backgroundColor: "{colors.fill-1}"
    textColor: "{colors.ink-white}"
  field:
    backgroundColor: "{colors.field-charcoal}"
    textColor: "{colors.ink-white}"
    rounded: "{rounded.field}"
    height: "50px"
    padding: "12px 16px"
  field-hover:
    backgroundColor: "{colors.field-charcoal-hover}"
  theme-toggle:
    backgroundColor: "{colors.fill-1}"
    textColor: "{colors.ink-white}"
    rounded: "{rounded.pill}"
    typography: "{typography.caption}"
    height: "30px"
    padding: "0 12px 0 10px"
  page-badge:
    backgroundColor: "rgb(0 0 0 / 0.62)"
    textColor: "#ffffff"
    rounded: "11px"
    height: "22px"
    padding: "0 7px"
  paper-button-primary:
    backgroundColor: "{colors.ballpoint-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.hand-pill}"
    height: "50px"
    padding: "0 28px"
  paper-button-primary-hover:
    backgroundColor: "{colors.ballpoint-blue-hover}"
  paper-button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ballpoint-blue}"
    rounded: "255px 18px 225px 18px / 18px 225px 18px 255px"
    height: "44px"
    padding: "0 22px"
  paper-field:
    backgroundColor: "transparent"
    textColor: "{colors.paper-ink}"
    rounded: "0"
    height: "50px"
    padding: "12px 16px"
  paper-page-badge:
    backgroundColor: "{colors.photo-white}"
    textColor: "{colors.red-pen}"
    rounded: "{rounded.hand-circle}"
    typography: "{typography.paper-note}"
    height: "26px"
    padding: "0 6px"
---

# Design System: pdfyier

## Overview

**Creative North Star: "The Lit Stage and the Notebook"**

pdfyier is one converter shown in two materials that share a single skeleton. In the dark, the page is a cyclorama before dawn: a depthless black sky, one full-bleed horizon line with a near-white core riding the top edge of the dock, and pages standing at their true aspect on pools of floor light. The light is the progress indicator. Four registered number properties (cobalt, rose, day, surge) are set by the job's phase: night when empty, cobalt first light once pages are set, rose dawn climbing with the upload percentage, warm white day when the PDF lands. The mood is Apple's dark Pro pages: SF Pro on Apple devices, self-hosted Inter elsewhere, a white pill primary, solid dark fields.

In the light, the same stage becomes a ruled college notebook (user-pinned): blue rules every 32px under a blank header band, a red margin line, blue-ballpoint ink, Kalam handwriting for headings and notes only. Pages become photos taped in at a slight random tilt, page numbers are circled in red pen, and the lamps map to paper tools: a yellow highlighter grows along the line the pages sit on with upload %, each page gets a red-pen check as its bytes leave, and a red check marks the finished status. Theme follows `prefers-color-scheme`, is remembered, and switches through a circular view transition opening from the toggle.

Density is low and centered. Nothing is boxed: light (dark) or ruled lines and tape (paper) separate things, together with generous spacing.

**Key Characteristics:**
- One system, two theme-scoped token sets on `data-theme` (`dark` / `paper`); components change material, never structure.
- State is carried by light (dark) or pen and highlighter (paper), always doubled by status text and button labels.
- Pages keep their true aspect ratio; the stage never crops them into a uniform grid.
- A single horizon line on the dock's top edge, which floats with the dock when pages overflow.
- Print type for everything you operate; handwriting only for what a student would write in.

## Colors

Dark is near-monochrome black and Apple greys lit by three lamp colours; paper is off-white with blue ink, red pen, and a yellow highlighter.

### Primary
- **Cobalt Lamp** (dark): first light. Horizon glow, floor pools under each row, the page rim light, the drop-veil horizon. Stored as channels (`--cobalt: 36 72 255`) so light levels drive alpha.
- **Horizon Core** (dark): the near-white centre of the horizon line and route line. Never a fill.
- **Ballpoint Blue** (paper): all ink. Wordmark, headings, primary button fill, field underline, text-button colour, focus outline and caret. It takes over `--cobalt-hi` in paper, so link and focus rules are shared.

### Secondary
- **Rose Lamp / Rose Rim** (dark): dawn. Rose rises only while sending, scaled by upload fraction (`--lx-rose` 0.08 to 0.80). Rose Rim is the sent-page rim, the travelling sheen on the page being sent, and the processing pulse.
- **Red Pen** (paper): circled page numbers, per-page checks, the done tick, step numbers, errors and the oversize warning (it replaces Alert Red in paper).

### Tertiary
- **Day Lamp** (dark): the warm near-white wash when the PDF lands. It lights the horizon zone only; the headline area stays black.
- **Highlighter Yellow** (paper): the progress bar along the page line (`scaleX(--progress)`, 0.6 alpha, `multiply`), the headline phrase and section-heading underlay, hover and focus washes, and text selection.
- **Cobalt Signal** (dark): links, focus outlines (2px, 3px offset), caret, "more" disclosure.

### Neutral
- **Sky Black / Paper White**: page ground. Dark nav and dock are black at 0.72 / 0.78 with `saturate(180%) blur(20px)`; the paper nav is paper at 0.86.
- **Ink White, Ink Silver, Ink Graphite** (dark) / **Paper Ink, Paper Ink Soft, Paper Ink Faint** (paper): primary text, secondary text, tertiary text (labels, formats, footer).
- **Sheet Charcoal / Photo White**: the page backing and the add tile.
- **Field Charcoal** (hover a step lighter), **Control Graphite** (remove button).
- **Fill 1-3**: translucent washes for toggle, secondary pill, code and hover. Paper versions are tinted with ballpoint blue.
- **Notebook Rule, Margin Red (0.6 alpha), Masking Tape (0.78 alpha)**: the notebook's own materials.
- **Alert Red** (dark): error status and the oversize warning capsule.

### Named Rules
**The Light Is the Progress Rule.** Lamp colours appear only as light: gradients, pools, rim edges and the horizon line, driven by `--lx-*` levels. Never use cobalt, rose or day as a flat button, card or text fill.

**The Earned Dawn Rule.** Rose appears only while bytes are leaving and Day only when a PDF has landed. No decorative sunrise at rest.

**The Three Tools Rule.** Paper colour is limited to what a student carries: blue ballpoint, red pen, yellow highlighter, plus the notebook's rules, margin and tape.

## Typography

**Display Font:** SF Pro via `-apple-system` (with self-hosted Inter, then Segoe UI and system-ui)
**Handwriting Font:** Kalam 400/700, self-hosted, loaded only when paper is on (with Bradley Hand, Segoe Print)
**Mono Font:** ui-monospace / SF Mono (with Menlo, Consolas)

**Character:** Tight, confident Apple print: negative tracking that tightens as size grows, weight 600 for every heading. Paper swaps the heads to warm Kalam at weight 700 and zero tracking, while everything operable stays in print.

### Hierarchy
- **Display** (600, 64px / 56px at ≤1068px / 40px at ≤734px, 1.05, -0.022em): the single page headline, balanced, max 14em. Paper: Kalam 700 68px / 44px, rotated -0.6deg, the key phrase highlighted.
- **Headline** (600, 48px / 40px / 32px, 1.08): section heads (Privacy, Help). The pipeline section sits one step down at 32px / 26px. Paper: Kalam 700 set inline with a highlighter underlay.
- **Lede** (400, 21px, 1.4, max 30em): the subhead and section ledes. 17px on phones.
- **Title** (600, 17-24px): empty-stage prompt (24px), fact terms (21px), FAQ questions (19px), step and route names (17px). Paper: Kalam 700 at 20-28px.
- **Body** (400, 17px, 1.47, -0.01em): running text. Explanatory paragraphs at 15-17px / 1.55, max 58-60ch.
- **Label** (400, 14px, tabular nums): the stage detail line, status line, formats line, text buttons. Paper sets the detail line in Kalam 17px as a note.
- **Caption** (400, 12px, 0 tracking): nav links, theme toggle, footer fine print.
- **Mono** (12.5px, 1.6): the pipeline code block. Inline code and kbd at 0.88em on Fill 2.

### Named Rules
**The Print for Controls Rule.** Buttons, the filename input, body copy, status text and nav links are always SF Pro / Inter, in both themes. Kalam is reserved for headings, notes, labels and marks (wordmark, headings, detail line, field label, add tile, page numbers, step numbers).

**The Tracking Follows Size Rule.** Print tracking runs from -0.022em at display down to 0 at 12px. Handwriting is always 0.

## Layout

A centred single column on a 1120px max width with 24px gutters (16px at ≤734px). The nav is a 52px sticky bar (48px on phones): wordmark left, three caption links and the theme toggle right. The intro is centred: 76px top padding, headline, 18px gap, lede. The stage follows 52px below (min-height 320px). Pages sit in centred, bottom-aligned, wrapping rows with 34px row gaps. Page height is a token (176 / 150 / 118px) and width is `page-h × aspect ratio`, so aspect is always preserved.

The dock (632px inner width: filename field plus Create PDF pill, 12px gap, status row under) is sticky to the viewport bottom. When pages overflow, it floats with a blurred black backing and carries the horizon with it, so the light is always in view. Documentation starts 150px below (104px on phones) in a 5fr/7fr split with a 64px gap that collapses to one column at 734px. The route is five columns joined by a horizontal cobalt-to-rose line, vertical on phones. The footer starts 160px below.

Paper adds a fixed page geometry: rules every 32px starting below a 116px blank header band, and a red margin at `max(12px, 50vw - 596px)` (8px on phones).

Breakpoints: 1068px (smaller page height and headings) and 734px (phone layout). Touch devices (`hover: none`) show the remove control permanently and swap "Drop images here" for "Add your images".

## Elevation & Depth

Dark depth is theatrical lighting, not material layering. Surfaces are flat. Depth comes from radial light gradients behind the pages (horizon glow up to 720px tall, floor pools under each row), a hairline rim light on each page's lower edge, and deep black drop shadows that throw each page toward the viewer. Paper depth is physical and shallow: taped photos cast soft ink-tinted shadows, tape strips float above them, and the stage lifts a page only when it is grabbed.

### Shadow Vocabulary
- **Stage page (dark)** (`box-shadow: 0 26px 34px -18px rgb(0 0 0 / 0.95), 0 10px 14px -8px rgb(0 0 0 / 0.8)`): every page at rest.
- **Grabbed page (dark)** (`0 40px 50px -20px #000, 0 16px 24px -10px rgb(0 0 0 / 0.9)`, plus translateY(-10px) scale(1.04)): lifted while being moved.
- **Rim light** (`inset 0 0 0 0.5px rgb(255 255 255 / 0.12), inset 0 -1.5px 0 rgb(cobalt / 0.25 + lx × 0.55)`): the lower edge catches the horizon. It turns Rose Rim when the page has been sent.
- **Taped photo (paper)** (`0 1px 1px rgb(31 36 51 / 0.1), 0 10px 18px -10px rgb(31 36 51 / 0.4)`): every paper page at rest.
- **Floating control** (`0 2px 10px rgb(0 0 0 / 0.6)` dark; `0 1px 4px rgb(31 36 51 / 0.25)` paper): the remove button.

### Named Rules
**The No Box Rule.** No content cards and no bordered panels. Separation comes from light, spacing and single hairlines (`inset 0 1px 0` rules between FAQ items and footer rows). Filled, rounded surfaces are reserved for controls, code and the pages themselves.

**The Light Follows the Job Rule.** Every lamp level is set by phase or progress (`night`, `first`, `dawn`, `day`, `error`, plus `surge` while files hover). Nothing glows independently of state.

## Shapes

Dark is Apple-soft geometry: full pills (999px) for every button, a 14px field, 12px code blocks, 6px inline code, and nearly square pages (3px) so they read as paper. Circles appear only for the remove control and the route stops (9px ring). Paper replaces geometric curves with hand-drawn irregular ones. Buttons use asymmetric elliptical radii that read as a pen-drawn loop, the page number is a wobbly circle (`55% 45% 52% 48% / 48% 55% 45% 52%`), the add tile is a 2px dashed irregular rectangle, the field is an underline only (radius 0), and photos have 1px corners with a per-page random tilt between -1.3deg and 1.3deg. The pen-drawn page line is a slightly wavering 1.6px SVG stroke.

## Components

### Buttons
Quiet, pill-shaped and Apple-exact in dark; inked by hand in paper.
- **Shape:** full pill (999px); paper uses the hand-pill loop radius.
- **Primary (Create PDF):** Ink White fill with black text, 50px tall, 28px side padding (20px on phones), 17px/600. Paper: Ballpoint Blue fill with white text.
- **Hover / Active:** primary brightens to pure white (paper: `#2447b8`). All pills press to `scale(0.97)`. Focus is the global 2px Cobalt Signal / Ballpoint Blue outline at 3px offset.
- **Disabled:** `#1d1d1f` fill with Ink Graphite text. Paper: transparent with a 2px faint ink outline.
- **Secondary (Choose Images):** 44px, Fill 2, weight 500; hover Fill 3. Paper: transparent with a 2px ballpoint outline, highlighter wash on hover.
- **Text button (Clear All):** 34px, no fill, Ink Silver, pill hover wash of Fill 1; 0.4 opacity when disabled.
- **Theme toggle:** 30px caption pill on Fill 1 with a 14px stroke icon (pen to go to paper, moon to go to dark). The word hides on phones.

### Inputs / Fields
- **Style (dark):** solid Field Charcoal, 14px radius, min 50px, inline Ink Graphite "File name" label, 17px value, fixed ".pdf" suffix in Ink Graphite.
- **Focus (dark):** a one-step-lighter fill plus a 2px Cobalt Signal ring (`box-shadow: 0 0 0 2px`), with a cobalt caret.
- **Paper:** a name written on a line. Transparent, radius 0, `inset 0 -2px 0` ballpoint underline at 0.45 (0.7 on hover, full on focus), and a faint highlighter wash on focus. The label is handwritten (Kalam 18px); the value stays in print.

### Navigation
A 52px sticky translucent bar with backdrop blur and a 1px bottom hairline. Wordmark 21px/600 (paper: Kalam 700 25px in Ballpoint Blue). Links are 12px Ink Silver and go to Ink White on hover, with 24px gaps (18px on phones).

### Page (signature)
Each image stands at its true aspect ratio on a Sheet Charcoal backing (paper: a white photo with a masking-tape strip at the top, tilted). A number badge sits at the lower left: a 22px blurred black pill in dark, a 26px red-pen circle in Kalam 15px/700 in paper. A 24px remove control appears on hover or focus (always visible on touch). An oversized image gets an alert capsule across the top and the image dims to 0.45. In dark, each page stands on a 26px pool of floor light with a 1px lit edge; the pool goes rose once the page is sent and day-white when done. Reordering is lift-and-set with FLIP reflow: a 260ms long-press on touch, Space/arrows/Space on keyboard. The ghost lifts to `scale(1.06) rotate(-1.5deg)` (paper -2.5deg) and settles in 260ms. While a page is sending, a sheen crosses it (rose in dark, highlighter in paper) over 0.9s. Paper adds a red-pen check that pops in as each page is sent.

### Horizon and dock (signature)
One 1px line across the full viewport width: transparent to cobalt to Horizon Core to cobalt to transparent, with a blurred copy for glow. It sits on the dock's top edge. Above it, stacked radial layers (cobalt, rose, pulse, day) have opacity and scale driven by the `--lx-*` levels. Below it, floor washes. Lamp transitions: cobalt 1.4s, rose 0.6s, day 2.2s, surge 0.35s. While the server builds the PDF, a rose pulse breathes on a 2.8s cycle. In paper, all light layers are hidden. The line becomes a wavering ballpoint stroke with a highlighter bar laid over it at `scaleX(progress)`, and the done tick draws itself in red pen.

### Drop veil
While files are dragged over the window: a full-viewport veil (black at 0.62 with 14px blur; paper at 0.82), a 40px headline, and its own cobalt horizon at 24% from the bottom. `surge` brightens the stage horizon under it.

### Disclosure and FAQ
Details rows separated by hairlines only, with 19px/600 summaries (paper: Kalam 22px/700) and a chevron that rotates 180deg over 0.3s. The pipeline "more" disclosure is a Cobalt Signal text link.

## Do's and Don'ts

### Do:
- **Do** drive every lamp from state: set `data-phase` and the `--lx-*` numbers, and let the registered properties fade (cobalt 1.4s, rose 0.6s, day 2.2s).
- **Do** keep pages at their true aspect ratio: height from `--page-h`, width from the image's own ratio.
- **Do** keep a text equivalent for every light phase in the status line and button labels.
- **Do** use `cubic-bezier(0.16, 1, 0.3, 1)` for arrivals, lifts and lamps, and `cubic-bezier(0.2, 0.8, 0.2, 1)` for settles, reflows and progress. Under reduced motion, stop the sheen and pulse, show the tick fully drawn, and snap drags.
- **Do** scope every paper change under `:root[data-theme="paper"]` and change material only: ink, tape, rules, highlighter. Keep the layout identical across themes.
- **Do** tilt each paper photo by its own random angle (±1.3deg) and circle its number in red pen.
- **Do** self-host every font (Inter, Kalam); no visit touches a third party.

### Don't:
- **Don't** put content in cards or bordered panels; light, spacing and single hairlines separate things.
- **Don't** fill buttons, text or surfaces with cobalt, rose or day in the dark theme; they are light only.
- **Don't** set buttons, the filename value, body copy or status text in Kalam.
- **Don't** crop pages into uniform thumbnails or square tiles.
- **Don't** add paper colours beyond blue ballpoint, red pen, yellow highlighter and the notebook's rule, margin and tape.
- **Don't** show rose or day light while nothing is uploading or nothing has landed.
