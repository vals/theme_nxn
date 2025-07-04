"""Theme registration functionality for theme_nxn."""

from plotnine import theme_set

from .theme import theme_nxn


def register_theme_nxn():
    """
    Register the nxn theme with plotnine's theme system.
    
    This function makes the nxn theme available through plotnine's
    standard theme mechanisms.
    
    Returns
    -------
    None
    """
    # Store the current theme to allow restoration
    current_theme = theme_set()
    
    # Set nxn theme as default
    theme_set(theme_nxn())
    
    return current_theme


def set_theme_nxn(base_size=11, base_family=""):
    """
    Set the nxn theme as the current default theme.
    
    Parameters
    ----------
    base_size : int, default 11
        Base font size in points.
    base_family : str, default ""
        Base font family.
        
    Returns
    -------
    theme
        The previous theme that was set.
    """
    return theme_set(theme_nxn(base_size=base_size, base_family=base_family))