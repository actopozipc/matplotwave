# matplotwave

A Matplotlib extension for vaporwave-inspired color schemes, forked and improved from the unmaintained [vapeplot](https://github.com/dantaki/vapeplot). 

Improvements include
- Reordered palette colors for better contrast
- Dark mode
- Smooth colormaps
- Additional palettes
- Scientific notation support
![Color palettes](https://github.com/actopozipc/matplotwave/blob/main/Examples/all_palettes.png)
Keywords: vaporwave matplotlib, aesthetic color palette, retro colors matplotlib, neon plots, 80s aesthetics visualization, synthwave colormap, vaporwave style charts, retrofuturism, y2k, lofi

## Installation

```bash
pip install matplotwave
```



## Quick Start
    import seaborn as sns
    import matplotwave
    import matplotlib.pyplot as plt
    sns.set_theme()
    matplotwave.set_light_theme() #or dark theme
    matplotwave.set_palette("windows95")
    plt.plot([1, 2, 3, 4], [1, 3, 2, 4])
    plt.plot([1, 2, 3, 4], [2, 1, 3, 2])
    plt.plot([1, 2, 3, 4], [1.5, 2, 2.5, 3])
    plt.show()

<img src="https://github.com/actopozipc/matplotwave/blob/main/Examples/quickstart.png" >

## Color palettes and examples
### vaporwave
Iconic neon pink/blue mix with a lot of different colors.
<img src="https://github.com/actopozipc/matplotwave/blob/main/Examples/vaporwave.png"/>

### y2k
Inspired by the y2k-aesthetic
![y2k ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/y2k_ridge.png)
![y2k sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/y2k.png)
### cool
Vibrant magenta and cyan tones
![cool ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/cool_ridge.png)
![cool sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/cool.png)
### crystal_pepsi and neon_crystal_pepsi
Light pastel colors.
![crystal_pepsi ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/crystal_pepsi_ridge.png)
Since crystal pepsi can, dependend on the screen, be hard to read on a white background,
![crystal_pepsi sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/crystal_pepsi.png)
I either recommend the neon_crystal_pepsi palette, which is just a bit darker:
![crystal_pepsi ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/neon_crystal_pepsi_ridge.png)
or, if you really want to stick with the soft pastels, the dark mode:
![cool dark mode](https://github.com/actopozipc/matplotwave/blob/main/Examples/crystal_pepsi_dark.png)
### windows95
Inspired by the windows 95 operating system. 
![windows95 ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/windows95_ridge.png)
![windows95 sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/windows95.png)
### mallsoft
Soft shopping mall pastels
![mallsoft ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/mallsoft_ridge.png)
![mallsoft sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/mallsoft.png)
### Jazzcup
Classic 90s jazz cup design colors
![jazzcup ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/jazzcup_ridge.png)
![jazzcup sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/jazzcup.png)
### Sunset
Warm neon sunset gradient
![sunset ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/sunset_ridge.png)
![sunset sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/sunset.png)
### Avanti
Bold red and blue retro scheme [by mike-u](https://github.com/mike-u)
![sunset ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/avanti_ridge.png)
![sunset sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/avanti.png)
### Seapunk
Underwater teal and purple vibes
![sunset ridge plot](https://github.com/actopozipc/matplotwave/blob/main/Examples/seapunk_ridge.png)
![sunset sinus waves](https://github.com/actopozipc/matplotwave/blob/main/Examples/seapunk.png)
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
![vaporwave dark mode](https://github.com/actopozipc/matplotwave/blob/main/Examples/vaporwave_dark.png)


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


