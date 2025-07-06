# theme_nxn: Custom Plotnine Theme Package

A Python package providing a custom theme for Plotnine with harmonious color palette and clean design aesthetics.

## Overview

The `theme_nxn` package implements a custom plotnine theme based on `theme_minimal` with:
- Clean, minimal design with white backgrounds
- Harmonious 8-color discrete palette
- Charcoal-based text and axes instead of black
- Fixed legend point sizing
- Easy theme registration and usage

## Package Structure

```
theme_nxn/
├── __init__.py          # Package exports
├── colors.py            # 8-color palette definitions
├── theme.py             # Theme factory and color scales
└── registration.py      # Theme registration functions
```

## Core Features

### Theme Factory
- `theme_nxn()` - Main theme factory function
- Built on `theme_minimal()` foundation
- Returns: `theme_minimal() + theme(custom_settings)`
- White background (not transparent)
- Charcoal color (#242323) for all text, axes, titles, labels

### Color Palette
7-color harmonious discrete palette:

**Base Colors:**
- Charcoal: `#242323`
- Coral: `#ED746B` 
- Teal: `#0E6F82`

**Extended Colors:**
- Warm Gray: `#8B7B7A`
- Sage: `#7BA098`
- Peach: `#F5A07A`
- Navy: `#1F4E5C`

### Legend Control
- Fixed legend point size (6) for `geom_point`
- Overrides actual point size in legends
- Consistent legend appearance across plots

### Theme Registration
- `register_theme_nxn()` - Register with plotnine theme system
- `set_theme_nxn()` - Set as default theme
- Integration with plotnine's theme mechanisms

## Usage

```python
from theme_nxn import theme_nxn, scale_color_nxn, scale_fill_nxn, guides_nxn

# Apply theme to a plot
plot = (ggplot(data, aes(x='x', y='y', color='group')) +
        geom_point() +
        theme_nxn() +
        scale_color_nxn() +
        guides_nxn())

# Set as default theme
from theme_nxn import set_theme_nxn
set_theme_nxn()
```

## API Reference

### Theme Functions
- `theme_nxn(base_size=11, base_family="")` - Main theme factory
- `register_theme_nxn()` - Register theme with plotnine
- `set_theme_nxn()` - Set as default theme

### Color Functions  
- `scale_color_nxn(n=None)` - Discrete color scale
- `scale_fill_nxn(n=None)` - Discrete fill scale
- `get_nxn_palette(n=None)` - Get palette colors
- `guides_nxn()` - Fixed legend point size

### Constants
- `NXN_COLORS` - Base color dictionary
- `NXN_PALETTE` - Full 7-color palette list

