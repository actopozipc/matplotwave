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
    matplotwave.set_light_theme() #alternatively, dark theme
    matplotwave.set_palette("vaporwave")
    
    plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.show()
## Documentation
### view all palettes
Visualize them:
  matplotwave.available()
or just as a list:
  print(matplotwave.available(show=False))
