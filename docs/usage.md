# Usage Guide

Complete guide to using the img-conv tool for all your image processing needs.

## Command Structure

```bash
uv run img-conv <command> [options]
```

## Commands

1. Show Command
---------------

Display information about images in a directory.

```bash
uv run img-conv show [OPTIONS]
```

**Options:**

- `-s, --source-dir TEXT`: Directory to scan for images (default: current directory)

**Examples:**

```bash
# Show images in current directory
uv run img-conv show

# Show images in specific directory
uv run img-conv show --source-dir ./photos

# Using short option
uv run img-conv show -s ~/Pictures
```

**Output:**
- Table showing image paths, names, and file sizes
- Scans subdirectories automatically
- Supports JPEG, PNG, and WEBP formats

2. Convert Command
-----------------

Convert images between formats with optimization.

```bash
uv run img-conv convert [OPTIONS]
```

**Options:**
- `-s, --source-dir TEXT`: Source directory (default: current directory)
- `-d, --destination-dir TEXT`: Output directory (default: same as source)
- `-e, --output-extension TEXT`: Output format - WEBP, PNG, JPG (default: WEBP)

**Examples:**

```bash
# Convert all images to WEBP in current directory
uv run img-conv convert

# Convert with specific source and destination
uv run img-conv convert -s ./input -d ./output -e webp

# Convert to PNG format
uv run img-conv convert --output-extension png

# Convert in-place (same directory)
uv run img-conv convert --source-dir ./photos
```

**Features:**
- Automatic quality optimization (80% for WEBP)
- Preserves original files
- Shows conversion statistics and file size savings
- Creates output directories automatically
- Skips files already in target format

3. Delete Command
----------------

Remove images by extension with safety features.

```bash
uv run img-conv delete [OPTIONS]
```

**Options:**
- `-s, --source-dir TEXT`: Directory to process (default: current directory)
- `-r, --remove-extension TEXT`: Extension to remove - WEBP, PNG, JPG, or * (default: *)
- `-y, --auto-confirm`: Skip confirmation prompt (default: dry-run mode)

**Examples:**

```bash
# Dry run - show what would be deleted (default behavior)
uv run img-conv delete

# Delete all non-WEBP images (dry run)
uv run img-conv delete --source-dir ./photos

# Delete only PNG files with confirmation
uv run img-conv delete -r png -y

# Delete all non-WEBP images with confirmation
uv run img-conv delete --auto-confirm
```

**Safety Features:**
- Dry-run mode by default (shows what would be deleted)
- Confirmation required for actual deletion
- Only processes supported image formats
- Preserves WEBP files when using default "*" option

## Workflow Examples

Basic Image Optimization Workflow
----------------------------------

```bash
# 1. Check what images you have
uv run img-conv show -s ./photos

# 2. Convert to WEBP for optimization
uv run img-conv convert -s ./photos -e webp

# 3. Review the results and savings

# 4. Clean up original files (dry run first)
uv run img-conv delete -s ./photos

# 5. Confirm deletion if satisfied
uv run img-conv delete -s ./photos -y
```

Batch Processing Multiple Directories
-------------------------------------

```bash
# Process each directory separately
for dir in photo1 photo2 photo3; do
    echo "Processing $dir..."
    uv run img-conv convert -s "$dir" -e webp
done
```

Format-Specific Operations
--------------------------

```bash
# Convert only to PNG (lossless)
uv run img-conv convert -e png

# Remove only JPEG files
uv run img-conv delete -r jpg -y

# Remove only PNG files
uv run img-conv delete -r png -y
```

Understanding Output
====================

Show Command Output
-------------------

- **Path**: Directory containing the image
- **Name**: Image filename
- **Size (KB)**: File size in kilobytes

Convert Command Output
----------------------

- **Conversion progress**: Success/error messages for each file
- **Summary table**: Before/after sizes and percentage savings
- **Total statistics**: Overall space saved across all conversions

Delete Command Output
---------------------

- **Dry-run mode**: Lists files that would be deleted
- **Confirmation mode**: Shows files as they're deleted
- **Error handling**: Reports any files that couldn't be deleted

Tips and Best Practices
========================

Performance
-----------
- Process smaller batches for very large image collections
- Use SSD storage for faster processing
- Close other applications when processing many large images

Quality Settings
----------------
- WEBP at 80% quality provides good balance of size and quality
- For archival purposes, consider PNG for lossless compression
- JPEG is good for photographs where some quality loss is acceptable

Safety
------
- Always run delete commands in dry-run mode first
- Keep backups of important images
- Test on a small batch before processing large collections

Directory Organization
----------------------
- Use separate output directories to keep originals safe
- Organize by date or project for easier management
- Consider using descriptive directory names

## Troubleshooting

Common Issues
-------------

"No images found"
-------------------

- Check the source directory path
- Ensure images have supported extensions (.jpg, .jpeg, .png, .webp)
- Verify directory permissions

"Permission denied"
-------------------

- Check write permissions for output directory
- Run with appropriate user permissions
- Ensure files aren't open in other applications

"Conversion failed"
-------------------

- Check if source images are corrupted
- Ensure sufficient disk space
- Verify image format is supported

"Large file processing"
-----------------------

- Monitor system memory usage
- Process in smaller batches
- Close other applications to free up resources

For more troubleshooting help, see [FAQ](faq.md).
