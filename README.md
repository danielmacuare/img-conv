# img-conv

A powerful command-line tool for batch image processing that converts images (JPG, JPEG, PNG, WEBP) to webp with optimization and detailed reporting.

## TO-DO

- Semantic Versioning
- Proper Logging
- Dev Branch
- Automatic Validation of markdown files.  
- Python tooling (Ruff, black, basedpyright, etc)
- Unit Tests
- Integration Tests

## Features

- 🖼️ **Batch Processing**: Convert multiple images in directories and subdirectories
- 📊 **Format Support**: JPEG, PNG, WEBP conversion with quality optimization
- 📈 **Size Optimization**: Automatic compression with detailed savings reports
- 🔍 **Image Analysis**: Display image information (size, path, format)
- 🗑️ **Safe Deletion**: Remove images by format with dry-run mode
- 🎨 **Rich Output**: Beautiful terminal tables and progress indicators
- 📁 **Directory Management**: Automatic output directory creation

> 💡 **Tip**: This repository includes sample JPEG images in the `samples/` directory - perfect for testing all commands!

## Quick Start

### 🚀 Try it instantly (no installation required)

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Run directly from GitHub (no local installation)
uvx --from git+https://github.com/danielmacuare/img-conv img-conv --help
uvx --from git+https://github.com/danielmacuare/img-conv img-conv list samples
uvx --from git+https://github.com/danielmacuare/img-conv img-conv convert samples 
```

### 📦 Full Installation

For regular use, see detailed installation instructions: [docs/installation.md](docs/installation.md)

```bash
# Option 1: Global installation (recommended for end users)
uv tool install git+https://github.com/danielmacuare/img-conv

# Option 2: Development setup (for contributors)
git clone git@github.com:danielmacuare/img-conv.git
cd img-conv
uv sync
```

### Basic Usage

```bash
# Local development (after uv sync)
uv run img-conv list samples
uv run img-conv convert samples
uv run img-conv delete samples

# Global installation (after uv tool install .)
img-conv list samples
img-conv convert samples
img-conv delete samples

# Single file processing
uv run img-conv convert photo.jpg
uv run img-conv list image.png
```

## Documentation

- 📦 [Installation Guide](docs/installation.md) - Detailed setup instructions
- 🚀 [Usage Guide](docs/usage.md) - Complete command reference and examples
- 🏗️ [Development Guide](docs/development.md) - Contributing and development setup
- 🔧 [Configuration](docs/configuration.md) - Advanced options and settings
- ❓ [FAQ](docs/faq.md) - Common questions and troubleshooting

## Commands Overview

| Command | Description | Local Development | Global Installation |
|---------|-------------|-------------------|-------------------|
| `list` | Display image information | `uv run img-conv list samples` | `img-conv list samples` |
| `convert` | Convert images to specified format | `uv run img-conv convert samples` | `img-conv convert samples` |
| `delete` | Remove images by extension | `uv run img-conv delete samples --auto-confirm` | `img-conv delete samples --auto-confirm` |

### Single File Examples

| Command | Description | Example |
|---------|-------------|---------|
| `list` | Analyze single image | `uv run img-conv list photo.jpg` |
| `convert` | Convert single image | `uv run img-conv convert photo.jpg` |
| `delete` | Delete single image | `uv run img-conv delete photo.jpg --auto-confirm` |

## Support

For detailed usage instructions, troubleshooting, and advanced features, please refer to the [documentation](docs/) folder.

## License

This project is open source. Please check the license file for details.
