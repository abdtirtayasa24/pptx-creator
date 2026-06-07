# PPTX Creator Runtime

A repository-scoped runtime and skill pack for creating, editing, extracting, and QA-checking PowerPoint presentations from command-line coding agents.

This project is designed to be usable inside any CLI-based agent environment, including **Claude Code**, **OpenAI Codex CLI**, **Pi Coding Agent**, and similar terminal agents that can read files, execute shell commands, and write generated artifacts.

## Capabilities

The repository provides a PPTX-focused agent skill under:

```text
.agents/skills/pptx/
```

The skill supports:

- Creating `.pptx` files from scratch using `pptxgenjs`
- Editing existing `.pptx` files through Office Open XML unpack/edit/pack workflows
- Reading and extracting content from `.pptx` using MarkItDown
- Converting rendered slides to images for visual QA
- Using `.docs/` as the default source-document directory
- Using `.generated/` as the default output directory

With the declared Python dependencies, the content-ingestion layer can handle:

| Source type | Extensions |
|---|---|
| PowerPoint | `.pptx` |
| Word | `.docx` |
| Excel | `.xlsx`, `.xls` |
| PDF | `.pdf` |
| Markdown/text | `.md`, `.markdown`, `.txt`, `.text` |
| Structured text | `.json`, `.jsonl`, `.csv` |
| HTML | `.html`, `.htm` |
| Images as slide assets | `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg` |

> Note: Image files can be embedded as slide assets. Extracting semantic text from images requires a vision/OCR-capable tool outside the base dependency set.

## Repository Layout

```text
.
├── .agents/
│   └── skills/
│       └── pptx/
│           ├── SKILL.md
│           ├── editing.md
│           ├── pptxgenjs.md
│           └── scripts/
├── .docs/
│   └── *.md / *.pdf / *.docx / *.xlsx / ...
├── .generated/
│   └── generated decks, scripts, extracted text, QA renders
├── demo/
│   ├── docs/
│   │   └── global-tiktok-instagram-addiction-(2015-2060)/
│   └── generated/
│       └── demo PPTX deck and QA/render artifacts
├── scripts/
│   ├── check-pptx-deps.sh
│   └── check-pptx-deps.ps1
├── package.json
├── requirements.txt
├── setup.py
└── README.md
```

## Runtime Architecture

The project combines three layers:

### 1. Agent Skill Layer

`.agents/skills/pptx/SKILL.md` defines agent-facing operating rules:

- when to trigger the PPTX workflow
- where to scan default source documents
- where to write generated outputs
- how to create decks from scratch
- how to edit templates safely
- how to perform content and visual QA

### 2. Python Document/Office Tooling

Python dependencies are declared in `requirements.txt`:

```text
markitdown[pptx,docx,xlsx,xls,pdf]
Pillow
```

MarkItDown is used to normalize source documents into Markdown-like text for agent reasoning and deck planning.

The skill also includes helper scripts for Office Open XML manipulation:

- `unpack.py` — extract and pretty-print `.pptx` package XML
- `pack.py` — repack edited Office XML into `.pptx`
- `validate.py` — validate package structure
- `soffice.py` — wrap LibreOffice conversion calls
- `thumbnail.py` — create thumbnail grids for deck inspection
- `add_slide.py` — duplicate or create slides from layouts
- `clean.py` — remove orphaned slides/media/rels

### 3. Node PPTX Generation Layer

Node dependencies are declared in `package.json`:

```json
{
  "dependencies": {
    "pptxgenjs": "^4.0.0"
  }
}
```

`pptxgenjs` is used when creating `.pptx` files programmatically from scratch.

## System Dependencies

For full rendering and visual QA, install these system-level tools:

| Tool | Purpose |
|---|---|
| LibreOffice / `soffice` | Convert `.pptx` to `.pdf` |
| Poppler / `pdftoppm` | Convert `.pdf` pages to slide images |
| Node.js | Run `pptxgenjs` deck generators |
| Python 3.10+ | Run MarkItDown and Office helper scripts |

## Clone and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abdtirtayasa24/pptx-creator.git
cd pptx-creator
```

### 2. Run the setup helper

```bash
python setup.py
```

The setup helper will:

- create `.docs/` for source documents if it does not exist
- create `.generated/` for generated decks, scripts, extracted text, and QA artifacts if it does not exist
- create `.venv/` if it does not exist
- install Python dependencies from `requirements.txt`
- install Node dependencies from `package.json`
- run the platform-specific PPTX dependency check

The dependency check validates Python packages, `pptxgenjs`, LibreOffice, and Poppler.

> Note: `setup.py` does not install system tools such as LibreOffice or Poppler. Install those separately if the dependency check reports that they are missing.

### Manual setup alternative

If you prefer to run the setup steps manually, use the commands below.

```bash
mkdir -p .docs .generated
python -m venv .venv
source .venv/bin/activate # or .venv/Scripts/Activate for Windows
python -m pip install -r requirements.txt
npm install
npm run check:pptx  # or npm run check:pptx:win for Windows
```

## Using with CLI Agents

This repository is intentionally agent-friendly. Any CLI agent can operate on it if it can:

1. read repository files,
2. execute shell commands,
3. write files into `.generated/`, and
4. follow the instructions in `.agents/skills/pptx/SKILL.md`.

Recommended agent behavior:

- Read `.agents/skills/pptx/SKILL.md` before any PPTX task.
- Use `.docs/` as the default source input directory unless the user specifies another path.
- Use `.generated/` as the default output directory.
- Prefer `pptxgenjs` for new decks without a template.
- Prefer unpack/edit/pack for template-based decks.
- Always perform content QA and visual QA before reporting completion.

Example prompt for a CLI agent:

```text
Read .agents/skills/pptx/SKILL.md, scan .docs/, create a polished PPTX deck from the available source material, and write all generated files to .generated/.
```

## Output Policy

Unless explicitly overridden by the user:

- Source documents live in `.docs/`
- Generated scripts live in `.generated/`
- Generated presentations live in `.generated/`
- Extracted text and QA render artifacts live in `.generated/`

This keeps the repository predictable for repeated agent runs.

## Demo

A generated example PowerPoint deck is available in `demo/generated/`.
The initial agent prompt used to execute this demo is available in `demo/demo_prompt.md`.
The demo source CSV files are stored in:

```text
demo/docs/global-tiktok-instagram-addiction-(2015-2060)/
```

Those CSV files are from the Kaggle dataset **TikTok and Instagram Addiction Dataset (2015–2060)**:

```text
https://www.kaggle.com/datasets/abdulmaliklodhra/tiktok-and-instagram-addiction-dataset-20152060
```

## Notes and Limitations

- `.docx` is supported; legacy `.doc` is not part of the declared base workflow.
- `.xlsx` and `.xls` are supported through MarkItDown extras.
- `.pdf` extraction quality depends on the PDF structure and parser behavior.
- Image embedding is supported; OCR/vision extraction is not guaranteed without additional tooling.
- Do not install dependencies automatically during normal agent execution unless the user explicitly asks for environment setup.

## License

See `LICENSE` and `.agents/skills/pptx/LICENSE.txt` for licensing terms.
