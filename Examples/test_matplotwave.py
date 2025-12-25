import matplotwave
import matplotlib.pyplot as plt
import seaborn as sns
import matplotwave
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sns.set_theme()
matplotwave.set_light_theme() #or dark theme
matplotwave.set_palette("windows95")

plt.plot([1, 2, 3, 4], [1, 3, 2, 4])
plt.plot([1, 2, 3, 4], [2, 1, 3, 2])
plt.plot([1, 2, 3, 4], [1.5, 2, 2.5, 3])
plt.show()
matplotwave.available()
#colormap
cmap = matplotwave.cmap("cool")
data =  np.linspace(1,0, 10).reshape(5,2)
plt.imshow(data, cmap=cmap)
plt.colorbar()
plt.show()

import matplotwave as mw




# Bonus: Same heatmap but with the darker, more readable variant on white background
cmap_dark = mw.cmap('neon_crystal_pepsi')
plt.imshow(A, cmap=cmap_dark)
mw.despine(plt.gca(), all=True)
plt.title("neon_crystal_pepsi colormap - random matrix (better on white)")
plt.show()

#Bonus: crystal_pepsi on dark background (classic vaporwave feel)
mw.set_dark_theme()
plt.imshow(A, cmap=cmap)
mw.despine(plt.gca(), all=True)
plt.title("crystal_pepsi on dark theme")
plt.show()
mw.set_light_theme()
# Palettes to demonstrate
palettes_to_demo = [
    "windows95", "vaporwave", "cool", "y2k", "crystal_pepsi",
    "mallsoft", "jazzcup", "sunset", "macplus", "seapunk",
    "avanti", "neon_crystal_pepsi"
]

# Global seaborn setup
sns.set_theme(style="white")

# Load and prepare data once (reused for all palettes)
brain_df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
used_networks = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17]
used_columns = (
    brain_df.columns.get_level_values("network")
    .astype(int)
    .isin(used_networks)
)
brain_df = brain_df.loc[:, used_columns]
corr_df = brain_df.corr().groupby(level="network").mean()


corr_df.index = corr_df.index.astype(int)
corr_df = corr_df.sort_index().T

# Ridgeline data
rs = np.random.RandomState(1979)
x = rs.randn(500)
groups = np.tile(list("ABCDEFGHIJ"), 50)
ridge_df = pd.DataFrame(dict(x=x, g=groups))
ridge_df["x"] += ridge_df.g.map(ord)

for pal in palettes_to_demo:

    mw.set_light_theme()
    mw.set_palette(pal)

    colors = [c["color"] for c in plt.rcParams["axes.prop_cycle"]]

    fig, axes = plt.subplots(
        2, 2, figsize=(14, 10),
        gridspec_kw=dict(hspace=0.35, wspace=0.25)
    )
    ax = axes[0, 0]
    unique_groups = sorted(ridge_df.g.unique())

    for i, g in enumerate(unique_groups):
        subset = ridge_df[ridge_df.g == g]
        sns.kdeplot(
            data=subset, x="x",
            fill=True,
            bw_adjust=0.5,
            linewidth=1.2,
            color=colors[i % len(colors)],
            ax=ax
        )



    ax.set_yticks([])
    ax.set_ylabel("")
    mw.despine(ax)

    ax = axes[0, 1]
    sns.violinplot(
        data=corr_df,
        bw_adjust=0.5,
        cut=1,
        linewidth=1,
        palette=colors,
        ax=ax
    )
    ax.set_ylim(-0.7, 1.05)
    mw.despine(ax)

 
    ax = axes[1, 0]
    x_vals = np.linspace(0, 2 * np.pi, 50)

    for i, c in enumerate(colors[:len(mw.palette(pal))]):
        ax.plot(x_vals, np.sin(x_vals) + i, linewidth=1.8)

    mw.despine(ax)

    ax = axes[1, 1]

    x = np.linspace(-5, 5, 500)
    y = np.linspace(-5, 5, 500)
    X, Y = np.meshgrid(x, y)

    Z = (
        np.sin(X) * np.cos(Y)
        + 0.5 * np.exp(-(X**2 + Y**2) / 2)
    )

    cmap = mw.cmap(pal)

    sns.heatmap(
        Z,
        cmap=cmap,
        center=0,
        cbar=True,
        xticklabels=False,
        yticklabels=False,
        ax=ax
    )
    fig.suptitle(f"{pal}", fontsize=16, y=0.98)
    plt.show()
