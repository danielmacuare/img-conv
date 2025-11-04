#!/usr/bin/env python3

from typer import Option, Typer

from .helpers import (
    convert_images,
    delete_images,
    get_images_info,
    show_results,
    show_savings,
    validate_dir,
)


"""
How to Use


## Long Use
python main.py --help

## Short Use

Typer
python im.py commands arguments options
"""


app = Typer()


@app.command("show")
def show(
    source_dir: str = Option(
        ".", "--source-dir", "-s", help="Directory path to look for images"
    ),
    mode: str = "show",
):
    images_info = get_images_info(source_dir)
    show_results(images_info, mode)


@app.command("convert")
def convert(
    source_dir: str = Option(
        ".", "--source-dir", "-s", help="Directory path to look for images"
    ),
    destination_dir: str = Option(
        None,
        "--destination-dir",
        "-d",
        help="Directory path where to store the converted images",
    ),
    output_extension: str = Option(
        "WEBP",
        "--output-extension",
        "-e",
        help="Output extension of the files to be converted (WEBP, PNG, JPG)",
    ),
    mode: str = "convert",
):
    if not destination_dir:
        destination_dir = source_dir
    print("Convert Images")
    validate_dir(destination_dir)
    images_info = get_images_info(source_dir)
    converted_images = convert_images(
        images_info,
        source_dir,
        destination_dir,
        output_extension,
    )
    show_savings(converted_images)
    show_results(converted_images, mode)


@app.command("delete")
def delete(
    source_dir: str = Option(
        ".", "--source-dir", "-s", help="Directory path to look for images"
    ),
    mode: str = "delete",
    remove_extension: str = Option(
        "*",
        "--remove-extension",
        "-r",
        help="Extension of the files to be removed (WEBP, PNG, JPG). Default * removes all except webp images",
    ),
    auto_confirm: bool = Option(
        False,
        "--auto-confirm",
        "-y",
        help="Set this option to auto-confirm the removal of all images [Default: Dry-Run]",
    ),
):
    images_info = get_images_info(source_dir)
    delete_images(images_info, source_dir, remove_extension.lower(), auto_confirm)


def main():
    """Main entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()

    """
 TO-DO
- Default to convert output on the same directory than the images    
    """
