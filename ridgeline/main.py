import pypalettes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pyfonts import load_font

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

temp = pd.read_csv("temp.csv")

month_dict = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december",
}

font = load_font(
    "https://github.com/coreyhu/Urbanist/blob/main/fonts/ttf/Urbanist-Bold.ttf?raw=true"
)
fontlight = load_font(
    "https://github.com/coreyhu/Urbanist/blob/main/fonts/ttf/Urbanist-Light.ttf?raw=true"
)

g = sns.FacetGrid(
    temp,
    row="month",
    hue="mean_month",
    aspect=15,
    height=0.75,
    # palette="Alacena_gradient",
    # palette="Fall_gradient",
    palette="Geyser_gradient",
)

g.map(
    sns.kdeplot,
    "Mean_TemperatureC",
    bw_adjust=1,
    clip_on=False,
    fill=True,
    alpha=0.8,
    linewidth=1.5,
)

g.map(sns.kdeplot, "Mean_TemperatureC", bw_adjust=1, clip_on=False, color="w", lw=2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)

for i, ax in enumerate(g.axes.flat):
    ax.text(
        -15,
        0.02,
        month_dict[i + 1],
        fontsize=15,
        font=font,
        color=ax.lines[-1].get_color(),
    )

g.fig.subplots_adjust(hspace=-0.3)

g.set_titles("")
g.set_yticklabels("")
g.set_ylabels("")
g.despine(bottom=True, left=True)

plt.setp(ax.get_xticklabels(), fontsize=15, fontweight="bold")
plt.xlabel("Temperature in degree Celsius", fontsize=15, font=fontlight)

g.fig.text(
    x=0.07,
    y=0.95,
    s="Daily average temperature in Seattle per month",
    ha="left",
    fontsize=24,
    font=fontlight,
)

plt.savefig("ridge.png", dpi=500, bbox_inches="tight")
plt.show()
