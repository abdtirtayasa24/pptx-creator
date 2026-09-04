---
name: pptx
description: "Creates, reads, edits, and converts presentation decks, including native interactive HTML slide presentations. Use when a .pptx file is involved; when the user mentions decks, slides, or presentations; or when `/pptx html` or HTML presentation output is requested. HTML mode recreates every slide with native HTML/CSS/SVG and interactive charts, filters, tooltips, navigation, and responsive presentation behavior."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill

## Quick Reference

| Task | Guide |
|------|-------|
| Check dependencies | Verify runtime dependencies before first use |
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit or create from template | Read [editing.md](editing.md) |
| Create PPTX from scratch | Read [pptxgenjs.md](pptxgenjs.md) |
| Create native interactive HTML slides | Read [html.md](html.md) |

---

## Default Project Paths

Unless the user explicitly provides another path:

- Scan source documents for presentation creation in `.docs/`.
- Write generated presentation files and intermediate/generated assets to `.generated/`.
- In HTML mode, use `.generated/<descriptive-name>.html` and do not also create `.pptx` or `.pdf` unless explicitly requested.

## Mode Selection (Required)

Determine the output mode before checking dependencies or generating files:

- If the first command argument is `html`, or the user requests an interactive HTML presentation, use **HTML mode**.
- In HTML mode, read [html.md](html.md) completely and output native `.html`, not `.pptx` or `.pdf`.
- Otherwise, use the normal PPTX workflow in this file.
- Pi's native skill command is `/skill:pptx html <instructions>`. This project also provides the `/pptx html <instructions>` prompt-template alias.

## Dependency Policy

Dependencies are environment-level prerequisites.

- Do not install dependencies during normal skill execution.
- Do not run `pip install`, `npm install`, `apt install`, or `brew install` unless the user explicitly requests environment setup.
- Prefer checking whether dependencies exist before using them.
- If dependencies are missing, report the missing dependency and provide installation guidance.
- For repeated usage, dependencies should be installed once in the agent runtime, virtual environment, container image, or project-level setup files.

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Editing Workflow

**Read [editing.md](editing.md) for full details.**

1. Analyze template with `thumbnail.py`
2. Unpack → manipulate slides → edit content → clean → pack

---

## Creating from Scratch

**Read [pptxgenjs.md](pptxgenjs.md) for full details.**

Use when no template or reference presentation is available.

---

## Design Ideas

**Don't create boring slides.** Plain bullets on a white background won't impress anyone. Consider ideas from this list for each slide.

### Before Starting

- **Pick a bold, content-informed color palette**: The palette should feel designed for THIS topic. If swapping your colors into a completely different presentation would still "work," you haven't made specific enough choices.
- **Dominance over equality**: One color should dominate (60-70% visual weight), with 1-2 supporting tones and one sharp accent. Never give all colors equal weight.
- **Dark/light contrast**: Dark backgrounds for title + conclusion slides, light for content ("sandwich" structure). Or commit to dark throughout for a premium feel.
- **Commit to a visual motif**: Pick ONE distinctive element and repeat it — rounded image frames, icons in colored circles, thick single-side borders. Carry it across every slide.

### Color Palettes

Choose colors that match your topic — don't default to generic blue. Use these palettes as inspiration:

| Theme | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| **Midnight Executive** | `1E2761` (navy) | `CADCFC` (ice blue) | `FFFFFF` (white) |
| **Forest & Moss** | `2C5F2D` (forest) | `97BC62` (moss) | `F5F5F5` (cream) |
| **Coral Energy** | `A5222A` (coral) | `F9E795` (gold) | `2F3C7E` (navy) |
| **Warm Terracotta** | `8F342A` (terracotta) | `E7E8D1` (sand) | `A7BEAE` (sage) |
| **Ocean Gradient** | `065A82` (deep blue) | `0E5A75` (teal) | `21295C` (midnight) |
| **Charcoal Minimal** | `36454F` (charcoal) | `F2F2F2` (off-white) | `212121` (black) |
| **Teal Trust** | `005E69` (teal) | `13BFA6` (seafoam) | `02C39A` (mint) |
| **Berry & Cream** | `6D2E46` (berry) | `7A4547` (dusty rose) | `ECE2D0` (cream) |
| **Sage Calm** | `84B59F` (sage) | `7BB8AD` (eucalyptus) | `2F5965` (slate) |
| **Cherry Bold** | `990011` (cherry) | `FCF6F5` (off-white) | `2F3C7E` (navy) |

### For Each Slide

**Every slide needs a visual element** — image, chart, icon, or shape. Text-only slides are forgettable.

**Layout options:**
- Two-column (text left, illustration on right)
- Icon + text rows (icon in colored circle, bold header, description below)
- 2x2 or 2x3 grid (image on one side, grid of content blocks on other)
- Half-bleed image (full left or right side) with content overlay

**Data display:**
- Large stat callouts (big numbers 60-72pt with small labels below)
- Comparison columns (before/after, pros/cons, side-by-side options)
- Timeline or process flow (numbered steps, arrows)

**Visual polish:**
- Icons in small colored circles next to section headers
- Italic accent text for key stats or taglines

### Typography

**Choose an interesting font pairing** — don't default to Arial. Pick a header font with personality and pair it with a clean body font.

| Header Font | Body Font |
|-------------|-----------|
| Georgia | Calibri |
| Arial Black | Arial |
| Calibri | Calibri Light |
| Cambria | Calibri |
| Trebuchet MS | Calibri |
| Impact | Arial |
| Palatino | Garamond |
| Consolas | Calibri |

| Element | Size |
|---------|------|
| Slide title | 36-44pt bold |
| Section header | 20-24pt bold |
| Body text | 14-16pt |
| Captions | 10-12pt muted |

### Spacing

- 0.5" minimum margins
- 0.3-0.5" between content blocks
- Leave breathing room—don't fill every inch

### Avoid (Common Mistakes)

- **Don't repeat the same layout** — vary columns, cards, and callouts across slides
- **Don't center body text** — left-align paragraphs and lists; center only titles
- **Don't skimp on size contrast** — titles need 36pt+ to stand out from 14-16pt body
- **Don't default to blue** — pick colors that reflect the specific topic
- **Don't mix spacing randomly** — choose 0.3" or 0.5" gaps and use consistently
- **Don't style one slide and leave the rest plain** — commit fully or keep it simple throughout
- **Don't create text-only slides** — add images, icons, charts, or visual elements; avoid plain title + bullets
- **Don't forget text box padding** — when aligning lines or shapes with text edges, set `margin: 0` on the text box or offset the shape to account for padding
- **Don't use low-contrast elements** — icons AND text need strong contrast against the background; avoid light text on light backgrounds or dark text on dark backgrounds
- **NEVER use accent lines under titles** — these are a hallmark of AI-generated slides; use whitespace or background color instead

---

## QA (Required)

**Assume there are problems. Your job is to find them.**

Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step. If you found zero issues on first inspection, you weren't looking hard enough.

### Content QA

```bash
python -m markitdown output.pptx
```

Check for missing content, typos, wrong order.

**When using templates, check for leftover placeholder text:**

```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|this.*(page|slide).*layout"
```

If grep returns results, fix them before declaring success.

### Visual QA

**⚠️ USE SUBAGENTS** — even for 2-3 slides. You've been staring at the code and will see what you expect, not what's there. Subagents have fresh eyes.

Convert slides to images (see `## Converting to Images`), then use this prompt:

```
Visually inspect these slides. Assume there are issues — find them.

Look for:
- Overlapping elements (text through shapes, lines through words, stacked elements)
- Text overflow or cut off at edges/box boundaries
- Decorative lines positioned for single-line text but title wrapped to two lines
- Source citations or footers colliding with content above
- Elements too close (< 0.3" gaps) or cards/sections nearly touching
- Uneven gaps (large empty area in one place, cramped in another)
- Insufficient margin from slide edges (< 0.5")
- Columns or similar elements not aligned consistently
- Low-contrast text (e.g., light gray text on cream-colored background)
- Low-contrast icons (e.g., dark icons on dark backgrounds without a contrasting circle)
- Text boxes too narrow causing excessive wrapping
- Leftover placeholder content

For each slide, list issues or areas of concern, even if minor.

Read and analyze these images:
1. /path/to/slide-01.jpg (Expected: [brief description])
2. /path/to/slide-02.jpg (Expected: [brief description])

Report ALL issues found, including minor ones.
```

### Verification Loop

1. Generate slides → Convert to images → Inspect
2. **List issues found** (if none found, look again more critically)
3. Fix issues
4. **Re-verify affected slides** — one fix often creates another problem
5. Repeat until a full pass reveals no new issues

**Do not declare success until you've completed at least one fix-and-verify cycle.**

---

## Converting to Images

Convert presentations to individual slide images for visual inspection:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

This creates `slide-01.jpg`, `slide-02.jpg`, etc.

To re-render specific slides after fixes:

```bash
pdftoppm -jpeg -r 150 -f N -l N output.pdf slide-fixed
```

---

## Runtime Dependencies

This skill assumes the following dependencies are already installed in the agent runtime.
Do not install dependencies during normal skill execution.

Required Python packages:

- `markitdown[pptx,docx,xlsx,xls,pdf]` — text extraction from `.pptx`, `.docx`, `.xlsx`, `.xls`, and `.pdf`
- `Pillow` — thumbnail grid generation

Required Node package:

- `pptxgenjs` — creating `.pptx` files from scratch

Required system binaries:

- LibreOffice / `soffice` — converting `.pptx` to `.pdf`
- Poppler / `pdftoppm` — converting `.pdf` pages to images

Before using PPTX reading, editing, rendering, or generation features, verify dependencies using the npm scripts provided by this repository. Pure HTML mode does not require LibreOffice, Poppler, or PptxGenJS unless a `.pptx` source must be inspected.

### Linux / macOS / Git Bash / WSL

```bash
npm run check:pptx
```

### Windows PowerShell

```bash
npm run check:pptx:win
```

If any dependency check fails, stop normal skill execution and report the missing dependency.
Do not run `pip install`, `npm install`, `apt install`, `brew install`, `winget install`, or `choco install` automatically unless the user explicitly asks for environment setup.