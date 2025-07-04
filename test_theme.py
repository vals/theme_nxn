"""Test script for theme_nxn package."""

import sys
sys.path.insert(0, '.')

try:
    from theme_nxn import (
        theme_nxn, 
        scale_color_nxn, 
        scale_fill_nxn, 
        guides_nxn,
        get_nxn_palette,
        NXN_COLORS,
        NXN_PALETTE
    )
    
    print("✓ Successfully imported theme_nxn")
    
    # Test color palette
    print(f"✓ Base colors: {NXN_COLORS}")
    print(f"✓ Full palette ({len(NXN_PALETTE)} colors): {NXN_PALETTE}")
    
    # Test palette function
    palette_4 = get_nxn_palette(4)
    print(f"✓ First 4 colors: {palette_4}")
    
    # Test theme creation
    theme = theme_nxn()
    print("✓ Theme created successfully")
    
    # Test scale functions
    color_scale = scale_color_nxn()
    fill_scale = scale_fill_nxn()
    guides_obj = guides_nxn()
    print("✓ Scales and guides created successfully")
    
    print("\n🎉 All tests passed! The theme_nxn package is ready to use.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure plotnine is installed: pip install plotnine")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()