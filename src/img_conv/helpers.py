#!/usr/bin/evn python3

from pathlib import Path
from sys import exit
from typing import Dict, List, Optional

from PIL import Image
from rich import inspect
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from typer import Exit

from .constants import (
    DRY_RUN_EMOT,
    ERROR_EMOT,
    GREEN,
    INFO_EMOT,
    SKIPPING_EMOT,
    SUCCESS_EMOT,
    WARNING_EMOT,
    YELLOW,
)

console: Console = Console()


def get_images_info(source_dir: str) -> List[dict]:
    """Get Initial Images Info Like name, path, original_size,

    Args:
        source_dir (Path): Directory path where images will be read from

    Returns:
        List[dict]: Each dictionary represents an image. Keys: name, path, original_size
    """

    try:
        source_dir_path = Path(source_dir).expanduser().resolve()
        # source_dir_full_path = source_dir.expanduser().resolve()
        rprint(f"{INFO_EMOT} Looking for images at: {source_dir_path}")
        # Getting a list of folders to search
        input_folders = [
            element for element in source_dir_path.iterdir() if element.is_dir()
        ]

        input_folders.append(source_dir_path)

        images_info = process_images(input_folders)

        if images_info:
            return images_info
        else:
            rprint(f"{ERROR_EMOT}3 No images were found at: {source_dir_path}")
            exit(4)

    except FileNotFoundError:
        console.print(
            f'{ERROR_EMOT}1 The folder "{source_dir_path}" from which the files will be read from, doesn\'t exists.'
        )
        exit(1)


def process_images(input_folders: List[Path]):
    images_info = []
    for directory in input_folders:
        source_dir = Path(directory)
        for image_path in source_dir.glob("*.*"):
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


def show_results(
    images_info: List[dict],
    mode: str = "show",
):
    if mode == "show":
        create_show_table(images_info)
    if mode == "convert":
        create_conversion_table(images_info)


def create_show_table(
    images_info: List[dict],
):
    table = Table(show_header=True, header_style=f"{YELLOW}")
    table.add_column(header="Path", justify="center", vertical="middle")
    table.add_column(header="Name", justify="center", vertical="middle")
    table.add_column(header="Size (KB)", justify="center", vertical="middle")

    for image in images_info:
        table.add_row(
            f"{Path(image['path']).parent}",
            image["name"],
            f"{image['original_size_kb']:.2f}",
        )

    table.title_justify = "center"

    console.print(table)


def create_conversion_table(
    images_info: List[dict],
):
    # console = Console()
    table = Table(show_header=True, header_style=YELLOW)
    table.add_column(header="Path", justify="center", vertical="middle")
    table.add_column(header="Name", justify="center", vertical="middle")
    table.add_column(header="Size Before (KB)", justify="center", vertical="middle")
    table.add_column(header="Size After (KB)", justify="center", vertical="middle")
    table.add_column(
        header="Reduced by (%)", justify="center", vertical="middle", style=GREEN
    )

    for image in images_info:
        table.add_row(
            image["path"],
            image["name"],
            image["original_size_kb"],
            image["size_after_kb"],
            image["reduction"],
        )

    console.print(table)


def validate_dir(destination_dir: str):
    destination_dir_path = Path(destination_dir).resolve().absolute()
    if not destination_dir_path.exists():
        rprint(f"{INFO_EMOT} The dir: '{destination_dir_path}' doesn't exists.")
        destination_dir_path.mkdir(parents=True)
        rprint(
            f"{INFO_EMOT} The dir: '{destination_dir_path}' has been created to save the results"
        )


def convert_images(
    images_info_dict: List[dict],
    source_dir: str,
    destination_dir: str,
    output_extension: str = "WEBP",
) -> List[dict]:
    """Convert Images (.pg, .jpeg and .png) to Webp images

    Args:
        images_info_dict (List[dict]): List containing general Image's Info
        destination_dir (Path): Directory path where converted images will be stored
        output_extension (str): Output extension of the files to be converted (WEBP, PNG, JPG, JPEG)

    Returns:
        converted_images (List[dict]: keys used path, name, original_size_kb, size_after_kb, reduction

    TO-DO
    Test Cases
    - Current format is the same as the output fmt - Skip
    - output_fmt doesn't exists or is not allowed. Error
    """
    destination_dir_path = Path(destination_dir)
    converted_images = []
    for image_props in images_info_dict:
        try:
            # Only the name, I need to add th starting path
            source_image_path = image_props["path"]
            image = Image.open(source_image_path)
            if image.format in ["JPEG", "jpeg", "PNG", "png"]:
                output_filename = (
                    source_image_path.stem + f".{output_extension.lower()}"
                )

                # Define where the Image is going to get saved
                # Save output on the destination_dir defined by user
                if source_dir != destination_dir:
                    output_file_path = Path.joinpath(
                        destination_dir_path, output_filename
                    )
                # When the user didn't define a dest_dir, then save the image
                # in the same dir as the original image.
                else:
                    output_file_path = Path.joinpath(
                        source_image_path.parent, output_filename
                    )

                image.save(output_file_path, output_extension.capitalize(), quality=80)
                console.print(
                    f"{SUCCESS_EMOT} Image saved at: {output_file_path.resolve()}"
                )

                converted_size_kb = output_file_path.stat().st_size / 1024
                reduction_percentage = f"{(1 - (converted_size_kb / image_props['original_size_kb'])) * 100: .2f}%"  # Result in KB

                converted_images.append(
                    {
                        "path": f"{source_image_path.parent}",
                        "name": f"{source_image_path.name}",
                        "original_size_kb": f"{image_props['original_size_kb']:.2f}",
                        "size_after_kb": f"{converted_size_kb:.2f}",
                        "reduction": reduction_percentage,
                    }
                )
            else:
                console.print(f"{SKIPPING_EMOT} Won't convert: {source_dir}")
        except Exception as error:
            console.print(f"{ERROR_EMOT} []Error processing {source_dir}: {str(error)}")
            exit(2)
    if not converted_images:
        rprint(f"{WARNING_EMOT}3 No images were found at: {source_dir}")
        exit(3)

    return converted_images


def show_savings(images_info: List[dict]):
    total_original_size_kb: float = 0.0
    total_reduced_size_kb: float = 0.0
    for image in images_info:
        total_original_size_kb += float(image["original_size_kb"])
        total_reduced_size_kb += float(image["size_after_kb"])
    total_saved_size_kb = total_original_size_kb - total_reduced_size_kb
    total_saved_size_percentage = (
        1 - (total_reduced_size_kb / total_original_size_kb)
    ) * 100

    table = Table(show_header=True, header_style=YELLOW)
    table.title = "Summary"
    table.add_column(header="Description", justify="left", vertical="middle")
    table.add_column(header="Figure", justify="center", vertical="middle")

    table.add_row("Number of Images Converted", f"{len(images_info)}")
    table.add_row("Total Original Size", f"{total_original_size_kb:.2f} KB")
    table.add_row("Total Reduced Size", f"{total_reduced_size_kb:.2f} KB")
    table.add_row("Total Saved Size", f"{total_saved_size_kb:.2f} KB")
    table.add_row("Total Saved Size %", f"{total_saved_size_percentage:.2f} %")

    console.print(table)



def delete_images(
    images_info: List[dict],
    source_dir: str,
    remove_extension: str,
    auto_confirm: bool = False,
):
    """Deletes all the images by default that are not webp.
    Additionally, you can pass the a value in the remove_extension
    to remove a specific image type like png, jpg or jpeg.

    Args:
        images_info (List[dict]): General info associated with each image
        source_dir (str): Source Directory to get the images to be deleted
        remove_extension (str): jpeg, jpg or png
        auto_confirm (bool, optional): Allows to delete the images.
            Defaults to False (Dry-Run).
    """
    img_formats: List[str] = []
    if remove_extension == "*":
        img_formats = ["jpg", "jpeg", "png"]
    else:
        img_formats.append(remove_extension)
    for image in images_info:
        # rprint(f"Image Info: {image}")
        # rprint(f"Image Extension to be deleted: {image['path'].suffix[1:]}")
        # rprint(f"Image Format to be deleted: {img_formats}")
        if image["path"].is_file() and image["path"].suffix[1:] in img_formats:
            # rprint(f"Image Path to be deleted: {image['path']}")
            if auto_confirm:
                try:
                    image["path"].unlink()
                    rprint(f"{SUCCESS_EMOT} The Image {image['path']} was deleted")
                except Exception as e:
                    rprint(
                        f"{ERROR_EMOT} The Image {image['path'].expanduser().resolve()} was not deleted: {e}"
                    )
                    continue
            else:
                rprint(
                    f"{DRY_RUN_EMOT} The Image {image['path'].expanduser().resolve()} will be deleted"
                )
