# matplotwave

A Matplotlib extension for vaporwave-inspired color schemes, forked and improved from the unmaintained [vapeplot](https://github.com/dantaki/vapeplot). 

Improvements include
- Reordered palette colors for better contrast
- Dark mode
- Smooth colormaps
- Additional palettes
- Scientific notation support

Keywords: vaporwave matplotlib, aesthetic color palette, retro colors matplotlib, neon plots, 80s aesthetics visualization, synthwave colormap, vaporwave style charts, retrofuturism, y2k, lofi

## Installation

```bash
pip install matplotwave
```



## Quick Start
    import matplotwave
    import matplotlib.pyplot as plt
    matplotwave.set_light_theme() #or dark theme
    matplotwave.set_palette("vaporwave")
    
    plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.show()
## Documentation
### view all palettes
Visualize them:

    matplotwave.available()

![Color palettes](https://github.com/actopozipc/matplotwave/blob/main/Examples/all_palettes.png)
or just as a list:

    print(matplotwave.available(show=False))

View just specific palettes:

    matplotwave.view_palette("vaporwave", "windows95", "cool")
### Setting the Color Cycle

    matplotwave.set_palette("neon_crystal_pepsi")
        
### Colormaps 
Colormaps use linear interpolation between the discrete palette colors to produce 256 smooth shades, which makes it also usable for continuous data visualization.

    cmap = matplotwave.cmap("y2k")
    plt.imshow(data, cmap=cmap)
### Theme Management
Some palettes from the original branch like crystal_pepsi use very light colors that can be hard to read on a white background. For these, I recommend the dark theme:

    matplotwave.set_dark_theme()
    
In order to switch back:

    matplotwave.set_light_theme()
    
### Obtaining color palettes
Retrieve the list of colors for a palette:

    colors = matplotwave.palette("cool")
    print(colors)
    
or a reversed version:

    reversed_colors = matplotwave.reverse("cool")
    
### Other
Althrough this was in the original branch, it was never documented properly. Clean up plots by removing spines:

    matplotwave.despine(plt.gca())  # Remove top and right spines
    matplotwave.despine(plt.gca(), all=True)  # Remove all spines and ticks
    
Adjust global font size:

    matplotwave.font_size(14)
## Color palettes and examples

