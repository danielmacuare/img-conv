"""
img-conv - A powerful CLI tool for batch image processing and format conversion.

This package provides functionality to convert images between formats (JPEG, PNG, WEBP)
with optimization and detailed reporting.
"""

__version__ = "0.1.0"
__author__ = "Daniel Macuare"
__email__ = "danielmacuare.uk@gmail.com"

from .cli import app

__all__ = ["app"]