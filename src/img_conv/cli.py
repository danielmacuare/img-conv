#!/usr/bin/env python3

from pathlib import Path
from typer import Argument, Option, Typer
from typing import Optional

from .helpers import (
    convert_images,
    delete_images,
    get_images_info,
    show_results,
    show_savings,
    validate_dir,
)


app = Typer(no_args_is_help=True)


@app.command("list")
def list_images(
    target: str = Argument(".", help="File or directory to analyze"),
    mode: str = Option("show", hidden=True),
):
    images_info = get_images_info(target)
    show_results(images_info, mode)


@app.command("convert")
def convert(
    target: str = Argument(".", help="File or directory to convert"),
    destination_dir: Optional[str] = Option(
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
    mode: str = Option("convert", hidden=True),
):
    # If no destination specified, determine based on target type
    if not destination_dir:
        target_path = Path(target)
        if target_path.is_file():
            destination_dir = str(target_path.parent)
        else:
            destination_dir = target
    
    print("Convert Images")
    validate_dir(destination_dir)
    images_info = get_images_info(target)
    converted_images = convert_images(
        images_info,
        target,
        destination_dir,
        output_extension,
    )
    show_savings(converted_images)
    show_results(converted_images, mode)


@app.command("delete")
def delete(
    target: str = Argument(".", help="File or directory to process"),
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
    images_info = get_images_info(target)
    delete_images(images_info, target, remove_extension.lower(), auto_confirm)


def main():
    """Main entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()
