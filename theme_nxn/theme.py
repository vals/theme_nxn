"""Main theme factory function for theme_nxn."""

from plotnine import theme_minimal, theme, element_rect, element_text, element_line, guides, guide_legend
from plotnine.scales import scale_color_discrete, scale_fill_discrete

from .colors import NXN_COLORS, get_nxn_palette


def theme_nxn(base_size=11, base_family=""):
    """
    Create the nxn theme based on theme_minimal.
    
    This theme provides a clean, minimal design with:
    - White background (not transparent)
    - Charcoal color for text and axes instead of black
    - Fixed legend point size for geom_point
    - Custom discrete color palette
    
    Parameters
    ----------
    base_size : int, default 11
        Base font size in points.
    base_family : str, default ""
        Base font family.
        
    Returns
    -------
    theme
        A plotnine theme object.
    """
    charcoal = NXN_COLORS["charcoal"]
    
    return (
        theme_minimal(base_size=base_size, base_family=base_family) +
        theme(
            # Set background to white instead of transparent with no borders
            panel_background=element_rect(fill="white", color=None),
            plot_background=element_rect(fill="white", color=None, size=0),
            
            # Use charcoal instead of black for text elements
            text=element_text(color=charcoal),
            plot_title=element_text(color=charcoal, hjust=0),
            axis_title=element_text(color=charcoal),
            axis_text=element_text(color=charcoal),
            legend_text=element_text(color=charcoal),
            legend_title=element_text(color=charcoal),
            strip_text=element_text(color=charcoal),
            
            # Use charcoal for axis lines and ticks
            axis_line=element_line(color=charcoal),
            axis_ticks=element_line(color=charcoal),
            
            # Legend styling
            legend_background=element_rect(fill="white", color=None, size=0),
            legend_key=element_rect(fill="white", color=None, size=0),
        )
    )


def scale_color_nxn(n=None, **kwargs):
    """
    Create a discrete color scale using the nxn palette.
    
    Parameters
    ----------
    n : int, optional
        Number of colors to use from the palette.
    **kwargs
        Additional arguments passed to scale_color_manual.
        
    Returns
    -------
    scale
        A plotnine color scale.
    """
    from plotnine.scales import scale_color_manual
    
    colors = get_nxn_palette(n)
    return scale_color_manual(values=colors, **kwargs)


def scale_fill_nxn(n=None, **kwargs):
    """
    Create a discrete fill scale using the nxn palette.
    
    Parameters
    ----------
    n : int, optional
        Number of colors to use from the palette.
    **kwargs
        Additional arguments passed to scale_fill_manual.
        
    Returns
    -------
    scale
        A plotnine fill scale.
    """
    from plotnine.scales import scale_fill_manual
    
    colors = get_nxn_palette(n)
    return scale_fill_manual(values=colors, **kwargs)


def guides_nxn():
    """
    Create guides with fixed legend point size for geom_point.
    
    Returns
    -------
    guides
        A plotnine guides object with fixed point size in legend.
    """
    return guides(
        color=guide_legend(override_aes={"size": 6}),
        fill=guide_legend(override_aes={"size": 6})
    )