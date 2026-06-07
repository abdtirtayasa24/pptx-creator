"""
Repository setup helper for PPTX Creator Runtime.

This script follows the setup flow:
- create working directories used by the runtime
- create a local Python virtual environment
- install Python dependencies
- install Node dependencies
- run the repository dependency check
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
MIN_PYTHON = (3, 10)


def log(message: str) -> None:
    print(f"\n==> {message}")


def run(command: list[str], *, cwd: Path = ROOT) -> None:
    print(f"$ {' '.join(command)}")
    subprocess.run(command, cwd=cwd, check=True)


def require_python_version() -> None:
    if sys.version_info < MIN_PYTHON:
        required = ".".join(map(str, MIN_PYTHON))
        current = platform.python_version()
        raise SystemExit(f"Python {required}+ is required. Current version: {current}")


def ensure_runtime_dirs() -> None:
    for directory in (ROOT / ".docs", ROOT / ".generated"):
        directory.mkdir(exist_ok=True)
        print(f"Ensured {directory.relative_to(ROOT)}/ exists")


def ensure_virtualenv() -> Path:
    if not VENV_DIR.exists():
        run([sys.executable, "-m", "venv", str(VENV_DIR)])
    else:
        print(".venv already exists")

    if os.name == "nt":
        python_path = VENV_DIR / "Scripts" / "python.exe"
    else:
        python_path = VENV_DIR / "bin" / "python"

    if not python_path.exists():
        raise SystemExit(f"Virtual environment Python was not found at: {python_path}")

    return python_path


def install_python_dependencies(python_path: Path) -> None:
    requirements = ROOT / "requirements.txt"
    if not requirements.exists():
        raise SystemExit("requirements.txt was not found")

    run([str(python_path), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(python_path), "-m", "pip", "install", "-r", str(requirements)])


def npm_command() -> str:
    command = "npm.cmd" if os.name == "nt" else "npm"
    resolved = shutil.which(command)
    if not resolved:
        raise SystemExit("npm was not found. Install Node.js, then run this setup script again.")
    return resolved


def install_node_dependencies(npm: str) -> None:
    package_json = ROOT / "package.json"
    if not package_json.exists():
        raise SystemExit("package.json was not found")

    run([npm, "install"])


def run_dependency_check(npm: str) -> None:
    if os.name == "nt":
        run([npm, "run", "check:pptx:win"])
    else:
        run([npm, "run", "check:pptx"])


def main() -> None:
    if len(sys.argv) > 1:
        if sys.argv[1] in {"-h", "--help"}:
            print("Usage: python setup.py")
            print("Creates .docs/, .generated/, .venv/, installs dependencies, and runs checks.")
            return
        raise SystemExit("Usage: python setup.py")

    os.chdir(ROOT)

    log("Checking Python version")
    require_python_version()

    log("Creating runtime directories")
    ensure_runtime_dirs()

    log("Creating Python virtual environment")
    python_path = ensure_virtualenv()

    log("Installing Python dependencies")
    install_python_dependencies(python_path)

    log("Checking Node/npm")
    npm = npm_command()

    log("Installing Node dependencies")
    install_node_dependencies(npm)

    log("Running PPTX runtime dependency check")
    run_dependency_check(npm)

    log("Setup complete")
    print("The project is ready to use.")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.returncode) from exc
