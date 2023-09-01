#!/usr/bin/evn python3

# TO-DO
# 0 - Check for error handling and edge cases
# 14 - Error, no images found on this starting path
#

# Done
# 10 - Check if there's a better way to do typer with this.
# 8 - Add summary of Items and space saved
# 6 - Add rich in tables (Done)
# 7 - Get Sizes of the images (Done)
# 15 - [Success] - Image Created at {Path} (Done)
# 16 - [ERROR] - Image Created at {Path} (Done)
# 0 - Fix python main.py convert (Done)
# 0 - Add all Saved space in each run, (Done)
# 1 - Pass starting_path and output_folder as var with Typer on Nebula (Done)
# 2 - Loop through all directories from the specified folder (Done)
# 3 - Function to identify all current .jpg,/jpeg,etc and their paths (Done)
# 4 - Function to delete all shit images
# 9 - Add colors to the Skipping messages, etc
# 13 - Give mode two options [show and convert]
# 12 - convert needs to have an optional argument


"""
This script is used to convert .jpg, .jpeg and .png images to .Webp.
The script will convert the images and will tell you how much space was saved.

How to Use

python main.py --help
python main.py show ~/repos/danielmacuare.github.io/assets/img/posts
python main.py convert ~/repos/danielmacuare.github.io/assets/img/posts --output-path ~/Desktop/outputs

Typer
python main.py commands arguments options


# RICH Emoji Codes
https://github.com/Textualize/rich/blob/master/rich/_emoji_codes.py
"""

from pathlib import Path
from sys import exit
from typing import Dict, List, Optional

from PIL import Image
from rich import inspect
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer, run

from constants import (
    ERROR_EMOT,
    GREEN,
    INFO_EMOT,
    SKIPPING_EMOT,
    SUCCESS_EMOT,
    WARNING_EMOT,
    YELLOW,
)
from tables import (
    create_conversion_table,
    create_show_table,
    show_results,
    show_savings,
)

console: Console = Console()


def get_images_info(input_path: Path) -> List[dict]:
    """Get Initial Images Info Like name, path, original_size,

    Args:
        input_path (Path): Directory path where images will be read from
        output_path (Path): Directory path where converted images will be stored

    Returns:
        List[dict]: Each dictionary represents an image. Keys: name, path, original_size
    """
    try:
        rprint(
            f"{INFO_EMOT} Looking for images at: {input_path.expanduser().resolve()}"
        )
        # Geting a list of folders to search
        input_folders = [
            directory
            for directory in input_path.expanduser().iterdir()
            if directory.is_dir()
        ]

        input_folders.append(input_path.expanduser().resolve())

        images_info = process_images(input_folders)

        return images_info

    except FileNotFoundError:
        console.print(
            f'{ERROR_EMOT} The folder "{input_path}" from which the files will be read from, doesn\'t exists.'
        )
        exit(1)


def process_images(input_folders: List[Path]):
    images_info = []
    for directory in input_folders:
        input_path = Path(directory)
        for image_path in input_path.glob("*.*"):
            if file_is_image(image_path):
                images_info.append(
                    {
                        "name": image_path.name,
                        "path": image_path.expanduser(),
                        "original_size_kb": image_path.stat().st_size
                        / 1024,  # Result in KB
                    }
                )
    return images_info


def file_is_image(possible_image: Path) -> bool:
    image_extensions = [".jpeg", ".jpg", ".png", ".webp"]
    return possible_image.suffix.lower() in image_extensions


def convert_to_webp(
    images_info_dict: List[dict], input_path: Path, output_path: Path
) -> List[dict]:
    """Convert Images (.pg, .jpeg and .png) to Webp images

    Args:
        images_info_dict (List[dict]): Dictionary containing Image's Info
        input_path (Path): Directory path where images will be read from
        output_path (Path): Directory path where converted images will be stored

    Returns:
        results (List[dict]: keys used path, name, original_size_kb, size_after_kb, reduction
    """
    results = []
    for image_props in images_info_dict:
        try:
            # Only the name, I need to add th starting path
            input_path = image_props["path"]
            image = Image.open(input_path)
            if image.format in ["JPEG", "jpeg", "PNG", "png"]:
                output_filename = input_path.stem + ".webp"
                output_file_path = Path.joinpath(output_path, output_filename)
                image.save(output_file_path, "WEBP", quality=80)
                console.print(
                    f"{SUCCESS_EMOT} Image saved at: {output_file_path.resolve()}"
                )

                converted_size_kb = output_file_path.stat().st_size / 1024
                reduction_percentage = f" {(1 - (converted_size_kb / image_props['original_size_kb'])) * 100: .2f}%"  # Result in KB

                results.append(
                    {
                        "path": f"{input_path.parent}",
                        "name": f"{input_path.name}",
                        "original_size_kb": f"{image_props['original_size_kb']:.2f}",
                        "size_after_kb": f"{converted_size_kb:.2f}",
                        "reduction": reduction_percentage,
                    }
                )
            else:
                console.print(f"{SKIPPING_EMOT} Won't convert: {input_path}")
        except Exception as error:
            console.print(f"{ERROR_EMOT} []Error processing {input_path}: {str(error)}")
            exit(2)
    return results


# @app.command()
def main(
    mode: str = Argument(
        "show",
        help='Options: "show" or "convert"',
    ),
    starting_path: str = Argument(".", help="Directory Path to read image files from"),
    target_path: Optional[str] = Argument(
        None, help="Directory Path to save converted files"
    ),
):
    """This script will help you to convert .jpeg, .jpg and .png to .webp"""

    input_path = Path(starting_path)

    images_info = get_images_info(input_path)

    if mode == "convert":
        if target_path is None:
            rprint(
                f"{WARNING_EMOT} No target Path Provided: Using the current directory"
            )
            output_path = Path(".")
        else:
            output_path = Path(target_path)
        if not output_path.exists():
            print(f'The dir: "{output_path.absolute()}" doesn\'t exists.')
            output_path.mkdir(parents=True)
            print(
                f'The dir: "{output_path.absolute()}" has been created to save the results'
            )
        images_info = convert_to_webp(images_info, input_path, output_path)
        if not images_info:
            rprint(
                f"{WARNING_EMOT} No images were found at: {input_path.expanduser().resolve()}"
            )
            exit(3)
        else:
            show_savings(images_info)

    if not images_info:
        rprint(
            f"{WARNING_EMOT} No images were found at: {input_path.expanduser().resolve()}"
        )
        exit(3)
    show_results(images_info, mode=mode)


if __name__ == "__main__":
    run(main)
