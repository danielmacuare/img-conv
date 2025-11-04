# img-conv

A powerful command-line tool for batch image processing that converts images between formats (JPEG, PNG, WEBP) with optimization and detailed reporting.

## TO-DO

-Automatic Validation of markdown files.

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
git clone <repository-url>
cd img-conv

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Set up project (creates venv and installs dependencies)
uv sync
```

### Basic Usage

```bash
# Show images in current directory
uv run img-conv show

# Convert images to WEBP format
uv run img-conv convert --source-dir ./images --output-extension webp

# Delete non-WEBP images (dry run)
uv run img-conv delete --source-dir ./images
```

## Documentation

- 📦 [Installation Guide](docs/installation.md) - Detailed setup instructions
- 🚀 [Usage Guide](docs/usage.md) - Complete command reference and examples
- 🏗️ [Development Guide](docs/development.md) - Contributing and development setup
- 🔧 [Configuration](docs/configuration.md) - Advanced options and settings
- ❓ [FAQ](docs/faq.md) - Common questions and troubleshooting

## Commands Overview

| Command | Description | Example |
|---------|-------------|---------|
| `show` | Display image information | `uv run img-conv show -s ./photos` |
| `convert` | Convert images to specified format | `uv run img-conv convert -e webp` |
| `delete` | Remove images by extension | `uv run img-conv delete -r png -y` |

## Support

For detailed usage instructions, troubleshooting, and advanced features, please refer to the [documentation](docs/) folder.

## License

This project is open source. Please check the license file for details.