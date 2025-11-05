# Usage Guide

Complete guide to using the img-conv tool for all your image processing needs.

## Sample Images

This repository includes sample JPEG images in the `samples/` directory that you can use to test all commands:

```bash
# See what sample images are available
uv run img-conv list samples

# Try converting them
uv run img-conv convert samples --output-extension webp
```

The sample images are perfect for learning how the tool works before using it on your own images.

## Command Structure

```bash
uv run img-conv <command> [target] [options]
```

Where `target` can be:

- **A single file**: `image.jpg`, `photo.png`, `picture.webp`
- **A directory**: `./photos`, `samples`, `/path/to/images`
- **Current directory** (default): `.` or omit the target entirely

## Commands

### List Command

Display information about images in a file or directory.

```bash
uv run img-conv list [TARGET]
```

**Arguments:**
- `TARGET`: File or directory to analyze (default: current directory)

**Examples:**

```bash
# List images in current directory
uv run img-conv list

# List sample images (try this first!)
uv run img-conv list samples

# List images in specific directory
uv run img-conv list ./photos

# Analyze a single image file
uv run img-conv list samples/Image1.jpg

# List images in home Pictures folder
uv run img-conv list ~/Pictures
```

**Output:**

- Table showing image paths, names, and file sizes
- For directories: scans subdirectories automatically
- For files: shows information about that specific image
- Supports JPEG, PNG, and WEBP formats

### Convert Command

Convert images between formats with optimization.

```bash
uv run img-conv convert [TARGET] [OPTIONS]
```

**Arguments:**
- `TARGET`: File or directory to convert (default: current directory)

**Options:**
- `-d, --destination-dir TEXT`: Output directory (default: see "Default Behavior" below)
- `-e, --output-extension TEXT`: Output format - WEBP, PNG, JPG (default: WEBP)

**Examples:**

```bash
# Convert all images to WEBP in current directory
uv run img-conv convert

# Convert sample images (try this first!)
uv run img-conv convert samples

# Convert a single image file
uv run img-conv convert samples/Image1.jpg

# Convert to PNG format
uv run img-conv convert samples --output-extension png

# Convert single file to PNG
uv run img-conv convert samples/Image1.jpg --output-extension png

# Convert with specific destination directory
uv run img-conv convert ./input --destination-dir ./output

# Convert single file to different directory
uv run img-conv convert photo.jpg --destination-dir ./converted

# Examples showing default destination behavior:

# Single file - saves to same directory as source
uv run img-conv convert /home/user/Documents/image.jpg
# Creates: /home/user/Documents/image.webp

# Directory - saves inside the source directory (in-place)
uv run img-conv convert /home/user/vacation-photos/
# Creates converted files inside: /home/user/vacation-photos/
# Example: beach.jpg → beach.webp (both in vacation-photos/)
```

**Features:**
- Automatic quality optimization (80% for WEBP)
- Preserves original files
- Shows conversion statistics and file size savings
- Creates output directories automatically
- Skips files already in target format
- Works with both single files and entire directories
- Smart default placement: saves converted files alongside originals

**Default Behavior (no `--destination-dir` specified):**
- **For single files**: Saves to the same directory as the source file
  - Example: `uv run img-conv convert /home/user/photo.jpg` → creates `/home/user/photo.webp`
- **For directories**: Saves converted images inside the same directory (in-place conversion)
  - Example: `uv run img-conv convert /home/user/photos/` → creates converted files inside `/home/user/photos/`

**Custom Destination (`--destination-dir` specified):**
- Saves all converted images to the specified directory
  - Example: `uv run img-conv convert photo.jpg --destination-dir ./output/` → creates `./output/photo.webp`

### Delete Command

Remove images by extension with safety features.

```bash
uv run img-conv delete [TARGET] [OPTIONS]
```

**Arguments:**
- `TARGET`: File or directory to process (default: current directory)

**Options:**
- `-r, --remove-extension TEXT`: Extension to remove - WEBP, PNG, JPG, or * (default: *)
- `-y, --auto-confirm`: Skip confirmation prompt (default: dry-run mode)

**Examples:**

```bash
# Dry run - show what would be deleted (default behavior)
uv run img-conv delete

# Delete all non-WEBP images from samples (dry run)
uv run img-conv delete samples

# Delete a specific image file (dry run)
uv run img-conv delete samples/Image1.jpg

# Delete only JPG files from samples with confirmation
uv run img-conv delete samples --remove-extension jpg --auto-confirm

# Delete specific file with confirmation
uv run img-conv delete samples/Image1.jpg --auto-confirm

# Delete all non-WEBP images with confirmation
uv run img-conv delete samples --auto-confirm
```

**Safety Features:**
- Dry-run mode by default (shows what would be deleted)
- Confirmation required for actual deletion
- Only processes supported image formats
- Preserves WEBP files when using default "*" option
- Works with both single files and entire directories

## Workflow Examples

### Basic Image Optimization Workflow

```bash
# 1. Check what images you have (try with samples first!)
uv run img-conv list samples

# 2. Convert to WEBP for optimization
uv run img-conv convert samples

# 3. Review the results and savings

# 4. Clean up original files (dry run first)
uv run img-conv delete samples

# 5. Confirm deletion if satisfied
uv run img-conv delete samples --auto-confirm
```

### Single File Processing

```bash
# Analyze a specific image
uv run img-conv list photo.jpg

# Convert single image to WEBP
uv run img-conv convert photo.jpg

# Convert single image to PNG
uv run img-conv convert photo.jpg --output-extension png

# Delete specific image (dry run first)
uv run img-conv delete photo.jpg

# Confirm deletion
uv run img-conv delete photo.jpg --auto-confirm
```

### Batch Processing Multiple Directories

```bash
# Process each directory separately
for dir in photo1 photo2 photo3; do
    echo "Processing $dir..."
    uv run img-conv convert "$dir"
done
```

### Format-Specific Operations

```bash
# Convert sample images to PNG (lossless)
uv run img-conv convert samples --output-extension png

# Remove only JPEG files from samples
uv run img-conv delete samples --remove-extension jpg --auto-confirm

# Remove only PNG files from samples
uv run img-conv delete samples --remove-extension png --auto-confirm
```

## Understanding Destination Directory Behavior

### Default Behavior (No `--destination-dir` specified)

The tool saves converted images based on the source type:

#### Single File Processing
```bash
# Source file: /home/user/photos/vacation.jpg
uv run img-conv convert /home/user/photos/vacation.jpg

# Result: /home/user/photos/vacation.webp
# (Same directory as the source file)
```

#### Directory Processing  
```bash
# Source directory: /home/user/photos/ (contains multiple images)
uv run img-conv convert /home/user/photos/

# Results saved inside the same directory:
# /home/user/photos/beach.jpg → /home/user/photos/beach.webp
# /home/user/photos/sunset.png → /home/user/photos/sunset.webp
# (In-place conversion within the source directory)
```

### Custom Destination Directory

When you specify `--destination-dir`, all converted images go to that location:

```bash
# Single file to custom directory
uv run img-conv convert /home/user/photos/vacation.jpg --destination-dir ./converted/
# Result: ./converted/vacation.webp

# Directory to custom directory  
uv run img-conv convert /home/user/photos/ --destination-dir ./converted/
# Results: ./converted/beach.webp, ./converted/sunset.webp, etc.
```

## Understanding Output

### List Command Output

- **Path**: Directory containing the image
- **Name**: Image filename
- **Size (KB)**: File size in kilobytes

### Convert Command Output

- **Conversion progress**: Success/error messages for each file
- **Summary table**: Before/after sizes and percentage savings
- **Total statistics**: Overall space saved across all conversions

### Delete Command Output

- **Dry-run mode**: Lists files that would be deleted
- **Confirmation mode**: Shows files as they're deleted
- **Error handling**: Reports any files that couldn't be deleted

## Tips and Best Practices

### Performance

- Process smaller batches for very large image collections
- Use SSD storage for faster processing
- Close other applications when processing many large images

### Quality Settings

- WEBP at 80% quality provides good balance of size and quality
- For archival purposes, consider PNG for lossless compression
- JPEG is good for photographs where some quality loss is acceptable

### Safety

- Always run delete commands in dry-run mode first
- Keep backups of important images
- Test on a small batch before processing large collections

### Directory Organization

- Use separate output directories to keep originals safe
- Organize by date or project for easier management
- Consider using descriptive directory names

## Troubleshooting

### Common Issues

#### "No images found"

- Check the file or directory path
- Ensure images have supported extensions (.jpg, .jpeg, .png, .webp)
- Verify directory permissions

#### "Permission denied"

- Check write permissions for output directory
- Run with appropriate user permissions
- Ensure files aren't open in other applications

#### "Conversion failed"

- Check if source images are corrupted
- Ensure sufficient disk space
- Verify image format is supported

#### "Large file processing"

- Monitor system memory usage
- Process in smaller batches
- Close other applications to free up resources

For more troubleshooting help, see [FAQ](faq.md).
