"""
img-conv - A powerful CLI tool for batch image processing and format conversion.

This package provides functionality to convert images between formats (JPEG, PNG, WEBP)
with optimization and detailed reporting.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .cli import app

__all__ = ["app"]