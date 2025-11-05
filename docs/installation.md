# Installation Guide

This guide will walk you through setting up the img-conv tool on your system.

## 🚀 Quick Test (No Installation Required)

Try img-conv instantly without any local installation:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Test the tool directly from GitHub
uvx --from git+https://github.com/danielmacuare/img-conv img-conv --help
uvx --from git+https://github.com/danielmacuare/img-conv img-conv list --source-dir samples
uvx --from git+https://github.com/danielmacuare/img-conv img-conv convert --source-dir samples --help
```

**What this does:**

- Downloads and runs img-conv directly from GitHub
- No local installation or cloning required
- Perfect for testing before committing to installation
- Uses the latest version from the main branch

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

### 2. Install Directly from GitHub (Recommended)

Install the latest version directly from the repository:

```bash
# Install globally from GitHub
uv tool install git+https://github.com/danielmacuare/img-conv
```

**What this does:**
- Installs the latest version from GitHub
- No need to clone the repository
- Automatically handles all dependencies
- Makes `img-conv` available system-wide

### 3. Clone for Development (Alternative)

Only needed if you want to contribute or modify the code:

```bash
# If using git
git clone git@github.com:danielmacuare/img-conv.git
cd img-conv

# Or download and extract the ZIP file
```

### 4. Set Up Project with uv (Development Only)

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

This installs:

- `typer[all]` - CLI framework with all features
- `Pillow` - Image processing library (installed with typer)
- `rich` - Terminal formatting library (installed with typer)

### 5. Verify Installation

Test the installation by running:

```bash
# If you installed globally from GitHub (step 2)
img-conv --help

# If you're doing development setup (step 4)
uv run img-conv --help
```

You should see the help menu with available commands.

## Global Installation (Optional)

### What is Global Installation?

Global installation makes the `img-conv` command available system-wide, allowing you to run it from any directory without needing to activate a virtual environment or use `uv run`.

**Benefits:**
- Run `img-conv` from anywhere on your system
- No need to remember the project path
- Integrates with system PATH
- Works like other CLI tools (git, docker, etc.)

**Considerations:**
- Installs to your user directory (not system-wide)
- May conflict with other versions if installed multiple ways
- Updates require reinstalling globally

### Global Installation Steps

```bash
# Navigate to the project directory
cd /path/to/img-conv

# Install globally using uv tool
uv tool install .

# Reinstall the App after making a change
uv tool install --force .
```

**What this does:**
- Installs `img-conv` to your user's tool directory (usually `~/.local/bin/`)
- Adds the command to your PATH automatically
- Creates an isolated environment for the tool

### Verify Global Installation

```bash
# Test from any directory
img-conv --help

# Check installation location
uv tool list
```

### Update Global Installation

When you make changes to the code:

```bash
# Reinstall with latest changes
uv tool install --force .

# Or uninstall and reinstall
uv tool uninstall img-conv
uv tool install .
```

### Uninstall Global Installation

```bash
# Remove global installation
uv tool uninstall img-conv
```

## Alternative Installation Methods

### Using uv directly

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

### Direct Installation from Repository

Install directly from a Git repository:

```bash
# Install from GitHub (when published)
uv tool install git+https://github.com/username/img-conv.git

# Install from local path
uv tool install /path/to/img-conv
```

**What this does:** Installs directly from source without needing to clone the repository first.

## Installation Comparison

| Method | Use Case | Command | Global Access | Auto-Updates |
|--------|----------|---------|---------------|--------------|
| **Quick Test** | Try before installing | `uvx --from git+... img-conv` | ❌ | ✅ (always latest) |
| **Global Installation** | Daily use, system integration | `img-conv` | ✅ | ❌ (manual) |
| **Local Development** | Contributing, modifying code | `uv run img-conv` | ❌ | ✅ (automatic) |
| **Virtual Environment** | Isolated project use | `source .venv/bin/activate && img-conv` | ❌ | ❌ (manual) |

### Recommended Approach

- **First-time users**: Try with `uvx --from git+https://github.com/danielmacuare/img-conv img-conv`
- **Regular users**: Use global installation (`uv tool install git+https://github.com/danielmacuare/img-conv`)
- **Developers/Contributors**: Use local development (`uv run img-conv`)
- **CI/CD**: Use uvx or virtual environment

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
- For global installation: `uv tool install --force .`

#### Virtual environment issues

- Delete `.venv` folder and recreate: `rm -rf .venv && uv venv`
- Or use: `uv sync --reinstall` to rebuild everything

#### Global installation issues

##### "Command not found: img-conv"

- Check if uv tools directory is in PATH: `echo $PATH | grep .local/bin`
- Verify installation: `uv tool list`
- Reinstall: `uv tool install --force .`

##### "Global: Permission denied"

- Don't use `sudo` with uv tool install
- Check directory permissions: `ls -la ~/.local/bin/`
- Try: `uv tool install --python $(which python3) .`

##### "Multiple versions conflict"

- Uninstall all versions: `uv tool uninstall img-conv`
- Remove from pip if installed: `pip uninstall img-conv`
- Reinstall cleanly: `uv tool install .`

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
