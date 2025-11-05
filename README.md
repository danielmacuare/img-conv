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

## Quick Start

### Requirements

- Python 3.11 or higher
- pip package manager

### Installation

See detailed installation instructions: [docs/installation.md](docs/installation.md)

```bash
# Clone and setup
git clone git@github.com:danielmacuare/img-conv.git
cd img-conv

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Option 1: Local development (recommended for contributors)
uv sync

# Option 2: Global installation (recommended for end users)
uv tool install .

# For option 2: After making changes to the application, you will need to reinstall the APP
uv tool install --force .
```

### Basic Usage

```bash
# Local development (after uv sync)
uv run img-conv list
uv run img-conv convert --source-dir ./images --output-extension webp
uv run img-conv delete --source-dir ./images

# Global installation (after uv tool install .)
img-conv list
img-conv convert --source-dir ./images --output-extension webp
img-conv delete --source-dir ./images
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
| `list` | Display image information | `uv run img-conv list -s ./photos` | `img-conv list -s ./photos` |
| `convert` | Convert images to specified format | `uv run img-conv convert -e webp` | `img-conv convert -e webp` |
| `delete` | Remove images by extension | `uv run img-conv delete -r png -y` | `img-conv delete -r png -y` |

## Support

For detailed usage instructions, troubleshooting, and advanced features, please refer to the [documentation](docs/) folder.

## License

This project is open source. Please check the license file for details.
