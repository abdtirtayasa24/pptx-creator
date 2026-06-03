#!/usr/bin/env bash
set -e

python - <<'PY'
import importlib.util

deps = {
    "markitdown": "markitdown",
    "Pillow": "PIL",
    "mammoth (Word/docx support)": "mammoth",
    "pandas (Excel support)": "pandas",
    "openpyxl (xlsx support)": "openpyxl",
    "xlrd (xls support)": "xlrd",
    "pdfminer-six (PDF support)": "pdfminer",
    "pdfplumber (PDF support)": "pdfplumber",
}

missing = []

for name, module in deps.items():
    if importlib.util.find_spec(module) is None:
        missing.append(name)

if missing:
    raise SystemExit(f"Missing Python dependencies: {', '.join(missing)}")

print("Python dependencies OK")
PY

node -e "require('pptxgenjs'); console.log('pptxgenjs OK')"

command -v soffice >/dev/null || {
  echo "Missing LibreOffice binary: soffice"
  exit 1
}

command -v pdftoppm >/dev/null || {
  echo "Missing Poppler binary: pdftoppm"
  exit 1
}

echo "All PPTX skill dependencies are ready"