"""Color palette definitions for theme_nxn."""

# Base colors from the specification
NXN_COLORS = {
    "charcoal": "#242323",
    "coral": "#ED746B",
    "sand": "#E5D3B8",
    "teal": "#0E6F82"
}

# Extended harmonious colors to reach 8 total colors
NXN_PALETTE = [
    "#242323",  # charcoal - dark neutral
    "#ED746B",  # coral - warm accent
    "#E5D3B8",  # sand - light neutral
    "#0E6F82",  # teal - cool accent
    "#8B7B7A",  # warm gray - darker sand variant
    "#7BA098",  # sage - muted teal-green
    "#F5A07A",  # peach - lighter coral
    "#1F4E5C",  # navy - darker teal
]

def get_nxn_palette(n=None):
    """
    Get the nxn color palette.
    
    Parameters
    ----------
    n : int, optional
        Number of colors to return. If None, returns all 8 colors.
        
    Returns
    -------
    list
        List of hex color codes.
    """
    if n is None:
        return NXN_PALETTE.copy()
    
    # Cycle through palette if more colors needed
    if n <= len(NXN_PALETTE):
        return NXN_PALETTE[:n]
    else:
        # Repeat palette if more colors needed
        full_cycles = n // len(NXN_PALETTE)
        remainder = n % len(NXN_PALETTE)
        return NXN_PALETTE * full_cycles + NXN_PALETTE[:remainder]