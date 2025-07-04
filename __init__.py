"""
theme_nxn: A custom plotnine theme with harmonious color palette.

This package provides a custom theme for plotnine based on theme_minimal,
featuring a curated color palette and clean design aesthetics.
"""

from .colors import NXN_COLORS, NXN_PALETTE, get_nxn_palette
from .theme import theme_nxn, scale_color_nxn, scale_fill_nxn, guides_nxn
from .registration import register_theme_nxn, set_theme_nxn

__version__ = "0.1.0"
__author__ = "theme_nxn"

__all__ = [
    # Colors
    "NXN_COLORS",
    "NXN_PALETTE", 
    "get_nxn_palette",
    
    # Theme
    "theme_nxn",
    "scale_color_nxn",
    "scale_fill_nxn",
    "guides_nxn",
    
    # Registration
    "register_theme_nxn",
    "set_theme_nxn",
]