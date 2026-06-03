$ErrorActionPreference = "Stop"

Write-Host "Checking Python dependencies..."

python -c "import markitdown, PIL; print('Python dependencies OK')"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Missing Python dependencies. Install with: pip install `"markitdown[pptx]`" Pillow"
    exit 1
}

Write-Host "Checking Node dependency: pptxgenjs..."

node -e "require('pptxgenjs'); console.log('pptxgenjs OK')"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Missing Node dependency. Install with: npm install pptxgenjs"
    exit 1
}

Write-Host "Checking LibreOffice..."

$soffice = Get-Command soffice -ErrorAction SilentlyContinue
if (-not $soffice) {
    $possibleSoffice = "C:\Program Files\LibreOffice\program\soffice.exe"

    if (Test-Path $possibleSoffice) {
        Write-Host "LibreOffice found at: $possibleSoffice"
    } else {
        Write-Error "Missing LibreOffice / soffice. Add LibreOffice program folder to PATH."
        exit 1
    }
} else {
    soffice --version
}

Write-Host "Checking Poppler..."

$pdftoppm = Get-Command pdftoppm -ErrorAction SilentlyContinue
if (-not $pdftoppm) {
    $possiblePopplerPaths = @(
        "C:\Program Files\poppler\Library\bin\pdftoppm.exe",
        "C:\Program Files\poppler-*\Library\bin\pdftoppm.exe",
        "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\oschwartz10612.Poppler_*\poppler-*\Library\bin\pdftoppm.exe"
    )

    $found = $false

    foreach ($path in $possiblePopplerPaths) {
        $matches = Get-ChildItem $path -ErrorAction SilentlyContinue
        if ($matches) {
            Write-Host "Poppler found at: $($matches[0].FullName)"
            $found = $true
            break
        }
    }

    if (-not $found) {
        Write-Error "Missing Poppler / pdftoppm. Add Poppler bin folder to PATH."
        exit 1
    }
} else {
    pdftoppm -v
}

Write-Host "All PPTX dependencies are ready."