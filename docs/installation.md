# Installation Guide

This guide will walk you through setting up the img-conv tool on your system.

## System Requirements

- **Python**: Version 3.11 or higher (uv can install this for you if needed)
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 512MB RAM (more for large image batches)
- **Storage**: At least 100MB free space for dependencies
- **uv**: Modern Python package manager (faster than pip)

## Installation Steps

### 1. Install uv

First, install `uv`, a fast Python package manager that will handle Python versions and dependencies:

```bash
# On macOS/Linux using curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows using PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Alternative: using pip if you already have Python
pip install uv
```

**What this does:** Downloads and installs `uv`, which is significantly faster than `pip` and can manage Python versions automatically. It also handles virtual environments more efficiently.

### 2. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd img-conv

# Or download and extract the ZIP file
```

### 3. Set Up Project with uv

Use `uv` to automatically create a virtual environment and install dependencies:

```bash
# Initialize project with Python 3.11+ (uv will install Python if needed)
uv python install 3.11

# Create virtual environment and install dependencies in one command
uv sync
```

**What this does:**

- `uv python install 3.11`: Downloads and installs Python 3.11 if not already available
- `uv sync`: Creates a virtual environment (`.venv/`) and installs all dependencies from `pyproject.toml` in one fast operation

### 4. Alternative: Manual Virtual Environment

If you prefer explicit control over the virtual environment:

```bash
# Create virtual environment with specific Python version
uv venv --python 3.11

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

**What this does:**
- `uv venv --python 3.11`: Creates a virtual environment using Python 3.11 (much faster than `python -m venv`)
- `uv pip install -r requirements.txt`: Installs dependencies using uv's faster resolver (10-100x faster than pip)

This installs:

- `typer[all]` - CLI framework with all features
- `Pillow` - Image processing library (installed with typer)
- `rich` - Terminal formatting library (installed with typer)

### 5. Verify Installation

Test the installation by running:

```bash
# Using the installed CLI command
uv run img-conv --help
```

You should see the help menu with available commands.

## Alternative Installation Methods

### Using uv directly

If you prefer not to use requirements.txt:

```bash
uv pip install "typer[all]"
```

**What this does:** Installs the typer package with all optional dependencies directly, bypassing the requirements.txt file.

### Development Installation

For development work, you might want additional tools:

```bash
uv pip install "typer[all]" mypy black flake8
```

**What this does:** Installs the main dependencies plus development tools:
- `mypy`: Type checking for Python code
- `black`: Code formatter for consistent styling
- `flake8`: Linting tool for code quality checks

### Global Installation with uvx

For system-wide access without virtual environments:

```bash
uvx install typer
```

**What this does:** Installs the tool globally using `uvx` (uv's equivalent to `pipx`), making it available system-wide without affecting other projects.

## Troubleshooting

### Common Issues

#### "Python not found"

- Ensure Python is installed and added to your PATH
- Try `python3` instead of `python`

#### "Permission denied"

- Use `uv` instead of `pip` - it handles permissions better
- Ensure you have write permissions in the project directory
- Try: `uv pip install --user "typer[all]"` for user-level installation

#### "Module not found"

- Make sure your virtual environment is activated
- Reinstall dependencies: `uv sync` or `uv pip install -r requirements.txt`

#### Virtual environment issues

- Delete `.venv` folder and recreate: `rm -rf .venv && uv venv`
- Or use: `uv sync --reinstall` to rebuild everything

### Platform-Specific Notes

#### Windows

- Use `py` instead of `python` if you have the Python Launcher
- Use backslashes in paths: `.venv\Scripts\activate`

#### macOS

- You might need to install Xcode command line tools: `xcode-select --install`
- Use `python3` if `python` points to Python 2

#### Linux

- `uv` handles Python installation automatically, no need for system packages
- If you prefer system Python: `sudo apt install python3-venv python3-pip`
- For older systems, you might need: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Next Steps

Once installed, proceed to the [Usage Guide](usage.md) to learn how to use the tool.