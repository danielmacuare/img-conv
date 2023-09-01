#!/usr/bin/evn python3
from pathlib import Path
from typing import Dict, List, Optional

from rich import inspect
from rich import print as rprint
from rich.console import Console
from rich.table import Table

console: Console = Console()

from constants import (
    ERROR_EMOT,
    GREEN,
    INFO_EMOT,
    SKIPPING_EMOT,
    SUCCESS_EMOT,
    WARNING_EMOT,
    YELLOW,
)


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
        tp1 = type(f"{Path(image['path']).parent}")
        tp2 = type(image["name"])
        tp3 = type(f"{image['original_size_kb']:.2f}")

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


def show_savings(images_info: List[dict]):
    total_original_size_kb: int = 0
    total_reduced_size_kb: int = 0
    for image in images_info:
        total_original_size_kb += float(image["original_size_kb"])
        total_reduced_size_kb += float(image["size_after_kb"])
    total_saved_size_kb = total_original_size_kb - total_reduced_size_kb
    total_saved_size_percentage = (
        1 - (total_reduced_size_kb / total_original_size_kb)
    ) * 100

    rprint(f"Total Original Size: {total_original_size_kb:.2f} KB")
    rprint(f"Total Reduced Size: {total_reduced_size_kb:.2f} KB")
    rprint(f"Total Saved Size: {total_saved_size_kb:.2f} KB")
    rprint(f"Total Saved Size (%): {total_saved_size_percentage:.2f} %")
    rprint

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
