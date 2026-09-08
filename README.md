# PPTX Creator Runtime

A repository-scoped agent runtime for creating, editing, extracting, and QA-checking PowerPoint decks and native interactive HTML presentations.

It is designed for terminal-based coding agents—including **Pi Coding Agent**, **Claude Code**, **OpenAI Codex CLI**, and similar tools—that can read files, run commands, and write generated artifacts.

## Features

- Create `.pptx` decks from scratch with PptxGenJS.
- Edit existing decks through Office Open XML unpack/edit/clean/pack workflows.
- Extract content from PowerPoint, Word, Excel, PDF, Markdown, CSV, JSON, and HTML sources.
- Generate **native interactive HTML slide presentations** with selectable text, semantic tables, and SVG/canvas/DOM charts.
- Add presentation navigation, fullscreen and overview modes, keyboard/touch controls, filters, search, focus states, and chart tooltips.
- Choose from **17 packaged design themes** automatically by presentation type or explicitly by theme ID.
- Render and inspect slides through repeatable content and visual QA workflows.
- Use `.docs/` for default source material and `.generated/` for outputs and intermediate artifacts.

## Quick Start

```bash
git clone https://github.com/abdtirtayasa24/pptx-creator.git
cd pptx-creator
python setup.py
```

`setup.py` creates `.docs/`, `.generated/`, and `.venv/`; installs the declared Python and Node dependencies; and runs the platform-specific dependency check.

System tools such as LibreOffice and Poppler are not installed automatically. See [Dependencies](#dependencies).

## Creating Presentations

Place source documents in `.docs/` unless another location is specified. Generated decks, HTML presentations, scripts, extracted content, and QA artifacts are written to `.generated/` by default.

### Pi Coding Agent

This repository includes `.pi/prompts/pptx.md`, which provides the project command alias:

```text
/pptx html <prompt>
/pptx pptx <prompt>
```

Examples:

```text
/pptx html Create an interactive quarterly performance presentation from the Excel workbook in .docs/. Use lagoon and add month and channel filters.
```

```text
/pptx pptx Create a board-ready annual report from the documents in .docs/. Use meridian.
```

Pi's native skill invocation also works:

```text
/skill:pptx html <prompt>
/skill:pptx <prompt>
```

If `.pi/prompts/` was added after Pi started, restart or reload Pi before using `/pptx`.

### Claude Code

Claude Code discovers the skill through `.claude/skills/pptx`, which should be a symbolic link or Windows directory junction to the canonical `.agents/skills/pptx` directory. It can then be invoked directly:

```text
/pptx html <prompt>
/pptx <prompt>
```

If the link is not present after cloning, create it from the repository root on a system that supports symbolic links:

```bash
mkdir -p .claude/skills
ln -s ../../.agents/skills/pptx .claude/skills/pptx
```

On Windows, enable Developer Mode or use an elevated terminal for a true symbolic link. A directory junction is also suitable for local Claude Code discovery.

### Other CLI Agents

Agents without skill discovery can be instructed explicitly:

```text
Read .agents/skills/pptx/SKILL.md, scan .docs/, create the requested presentation, and write all generated files to .generated/.
```

## Output Modes

| Mode | Trigger | Default output | Primary implementation |
|---|---|---|---|
| PPTX | `/pptx pptx <prompt>`, `/skill:pptx <prompt>`, or a normal deck request | `.generated/<name>.pptx` | PptxGenJS or Office Open XML editing |
| Interactive HTML | `/pptx html <prompt>`, `/skill:pptx html <prompt>`, or an explicit interactive HTML request | `.generated/<name>.html` | Native HTML, CSS, JavaScript, and SVG/canvas/DOM |

HTML mode does not create a `.pptx` or `.pdf` unless the user explicitly asks for those formats too.

### Native HTML Contract

The complete implementation requirements are in the [native HTML workflow](.agents/skills/pptx/html.md). Interactive HTML presentations must:

- represent every source/requested slide as an ordered 16:9 HTML slide;
- keep text selectable and searchable;
- use real `<table>` elements for tables;
- use SVG, canvas, or DOM marks for charts;
- never use rendered PowerPoint pages as full-slide images;
- preserve access to dense data through readable focused views, filters, tabs, drill-down, or scrolling;
- support keyboard navigation, touch navigation, fullscreen, overview, and visible focus states;
- remain responsive and preferably self-contained; and
- complete at least one browser-based visual fix-and-verify cycle.

Validate a generated HTML presentation with:

```bash
source .venv/Scripts/activate  # Windows Git Bash
python .agents/skills/pptx/scripts/validate_html_presentation.py .generated/deck.html --min-slides 1
```

On Linux or macOS, activate the environment with `source .venv/bin/activate`.

## Design Themes

The runtime contains 17 interchangeable themes under `.agents/skills/pptx/design-themes/themes/`:

```text
aurora      blueprint    blush       broadsheet   clay
crayon      foundry      grove       lagoon       linen
marmalade   meridian     obsidian    spectrum     terminal
vellum      workbench
```

Theme behavior:

1. A theme named by the user is used directly.
2. Otherwise, the agent selects one from the audience, subject, content density, and delivery setting.
3. Exactly one theme is loaded per deck.
4. PPTX generation uses `theme.json`; HTML generation also embeds or adapts `theme.css`.
5. Theme colors, typography, spacing, radii, chart series, and signature motif remain consistent throughout the deck.

See:

- [Theme catalog and selection rules](.agents/skills/pptx/design-themes/catalog.md)
- [Visual theme gallery](.agents/skills/pptx/design-themes/preview.html)
- [Theme schema](.agents/skills/pptx/design-themes/SCHEMA.md)

## Supported Sources

The declared document-ingestion layer supports:

| Source type | Extensions |
|---|---|
| PowerPoint | `.pptx` |
| Word | `.docx` |
| Excel | `.xlsx`, `.xls` |
| PDF | `.pdf` |
| Markdown and text | `.md`, `.markdown`, `.txt`, `.text` |
| Structured text | `.json`, `.jsonl`, `.csv` |
| HTML | `.html`, `.htm` |
| Presentation assets | `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp` |

Images can be embedded as presentation assets. Semantic extraction from images requires a vision/OCR-capable agent or tool outside the base dependency set.

## Repository Layout

```text
.
├── .agents/skills/pptx/
│   ├── SKILL.md                         # Canonical agent instructions
│   ├── editing.md                       # Template/editing workflow
│   ├── pptxgenjs.md                     # PPTX-from-scratch workflow
│   ├── html.md                          # Native interactive HTML workflow
│   ├── design-themes/
│   │   ├── catalog.md                   # Theme selection guide
│   │   ├── preview.html                 # Gallery of all themes
│   │   ├── SCHEMA.md                    # Theme token contract
│   │   └── themes/<id>/
│   │       ├── theme.json
│   │       └── theme.css
│   └── scripts/
│       ├── validate_html_presentation.py
│       └── office/...
├── .claude/skills/pptx                  # Claude Code link to canonical skill
├── .pi/prompts/pptx.md                  # Pi `/pptx` command alias
├── .docs/                               # Default source documents
├── .generated/                          # Generated outputs and QA artifacts
├── demo/                                # Example source data and deck output
├── scripts/                             # Dependency checks
├── package.json
├── requirements.txt
├── setup.py
└── README.md
```

## Runtime Architecture

### Agent workflow layer

`.agents/skills/pptx/SKILL.md` selects PPTX or HTML mode, establishes input/output conventions, chooses a design theme, and requires content and visual QA.

### Document and Office tooling

MarkItDown normalizes supported source documents for agent reasoning. The Office helpers unpack, clean, validate, render, and repack PowerPoint packages.

Important utilities include:

- `scripts/office/unpack.py` — extract and pretty-print package XML;
- `scripts/office/pack.py` — repack Office XML into `.pptx`;
- `scripts/office/validate.py` — validate package structure;
- `scripts/office/soffice.py` — wrap LibreOffice conversion;
- `scripts/thumbnail.py` — build thumbnail grids;
- `scripts/add_slide.py` — duplicate or create slides from layouts; and
- `scripts/clean.py` — remove orphaned slides, media, and relationships.

### PPTX generation layer

PptxGenJS creates new PowerPoint decks programmatically when no template is supplied.

### Native HTML layer

HTML mode creates browser-native slides and validates their structure with `validate_html_presentation.py`. Charts and interactions remain editable and inspectable rather than being flattened into slide screenshots.

## Dependencies

### Declared packages

| Dependency | Purpose |
|---|---|
| Python 3.10+ | Runtime for extraction, validation, and Office helpers |
| `markitdown[pptx,docx,xlsx,xls,pdf]` | Source-document extraction |
| Pillow | Thumbnail and image processing |
| Node.js and `pptxgenjs` | Programmatic PPTX generation |

### System tools for PPTX rendering

| Tool | Purpose |
|---|---|
| LibreOffice / `soffice` | Convert `.pptx` to `.pdf` |
| Poppler / `pdftoppm` | Convert PDF pages to slide images |

Pure HTML mode does not require LibreOffice, Poppler, or PptxGenJS unless a PowerPoint source must also be inspected or rendered.

Check the full PPTX toolchain with:

```bash
npm run check:pptx       # Linux, macOS, Git Bash, or WSL
npm run check:pptx:win   # Windows PowerShell
```

## Manual Setup

```bash
mkdir -p .docs .generated
python -m venv .venv
source .venv/bin/activate  # use .venv/Scripts/activate on Windows Git Bash
python -m pip install -r requirements.txt
npm install
npm run check:pptx         # use check:pptx:win in Windows PowerShell
```

## QA Policy

Every completed presentation should include:

1. source-to-slide content verification;
2. overflow, overlap, contrast, alignment, and readability checks;
3. representative rendering at the intended presentation size;
4. at least one visual fix-and-verify cycle; and
5. re-validation after fixes.

PPTX mode uses MarkItDown plus PDF/image rendering. HTML mode uses the structural validator, JavaScript syntax checks, and desktop/compact browser inspection.

## Demo

A generated PowerPoint and HTML deck example is available in `demo/generated/`. Its source prompt is in `demo/prompt/`, and its source CSV files are under `demo/docs/`.

The dataset is available from:
- [Kaggle - TikTok & Instagram Addiction Dataset (2015–2060)](https://www.kaggle.com/datasets/abdulmaliklodhra/tiktok-and-instagram-addiction-dataset-20152060) (PPTX deck example).
- [Kaggle - E-Commerce Delivery Analytics Dataset](https://www.kaggle.com/datasets/datascikhan/e-commerce-delivery-and-shipping-data-2026) (HTML deck example).

## Notes and Limitations

- Legacy `.doc` files are not part of the declared base workflow.
- PDF extraction quality depends on the PDF structure and parser behavior.
- Font availability affects PPTX rendering; presentation generators should use each theme's documented fallback stack when necessary.
- Packaged HTML themes use web-font URLs, so offline viewing may fall back to local fonts unless fonts are embedded.
- Do not install dependencies during normal agent execution unless the user explicitly requests environment setup.

## License

See `LICENSE` and `.agents/skills/pptx/LICENSE.txt` for licensing terms.
