from pypalettes import load_cmap
import matplotlib.pyplot as plt
import pandas as pd
from pyfonts import load_font
from drawarrow import ax_arrow
import matplotlib.patheffects as path_effects

data = pd.read_csv(
    "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/gapminderData.csv"
)
data["continent"] = pd.Categorical(data["continent"])
data = data[data["year"] == 2007]

font = load_font(
    "https://github.com/coreyhu/Urbanist/blob/main/fonts/ttf/Urbanist-Bold.ttf?raw=true"
)

fig, ax = plt.subplots(dpi=300)

ax.scatter(
    y=data["lifeExp"],
    x=data["gdpPercap"],
    s=data["pop"] / 250000,
)
ax.set_xlim(-3000, 52_000)
ax.set_yticks([40, 50, 60, 70, 80], labels=[40, 50, 60, 70, 80])
ax.set_xlabel("GDP/capita")
ax.set_ylabel("Life Expectancy")

fig.savefig("gapminder/gapminder-bad.png", dpi=300, bbox_inches="tight")

#######################################################################

cmap = load_cmap("Alosa_fallax")

fig, ax = plt.subplots(dpi=300)

ax.scatter(
    y=data["lifeExp"],
    x=data["gdpPercap"],
    s=data["pop"] / 250000,
    c=data["continent"].cat.codes,
    cmap=cmap,
    alpha=0.7,
    edgecolors="#212020",
    linewidth=1,
    zorder=10,
)
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(size=0)
ax.set_xlim(-3000, 52_000)
ax.set_xticks(
    [0, 10_000, 20_000, 30_000, 40_000, 50_000],
    labels=[
        "$0k",
        "$10k",
        "$20k",
        "$30k",
        "$40k",
        "$50k",
    ],
    font=font,
)
ax.set_yticks([40, 50, 60, 70, 80], labels=[40, 50, 60, 70, 80], font=font)
ax.grid(zorder=-10)

text_params = dict(
    size=12,
    weight="bold",
    font=font,
    path_effects=[
        path_effects.Stroke(linewidth=1, foreground="black"),
        path_effects.Normal(),
    ],
)

arrow_args = dict(
    color="black",
    radius=0.3,
    head_length=5,
    head_width=3,
    fill_head=False,
    zorder=5,
)
ax.text(x=38_000, y=70, s="United States", color=cmap(1), **text_params)
ax_arrow([47_000, 71.5], [45_000, 76], **arrow_args)

ax.text(x=11_000, y=63, s="India", color=cmap(2), **text_params)
ax_arrow([11_200, 65], [7_500, 65], **arrow_args)

ax.text(x=0, y=82, s="China", color=cmap(2), **text_params)
ax_arrow([500, 82], [1_400, 78], **arrow_args)

ax.text(x=18_000, y=47, s="South Africa", color=cmap(0), **text_params)
ax_arrow([18_000, 48], [10_500, 49.5], **arrow_args)

ax.text(
    x=34000, y=73, s="Germany", color=cmap(3), ha="center", va="center", **text_params
)
ax_arrow([34000, 73.5], [32500, 78], **arrow_args)

ax.text(x=40_200, y=42, s="Gapminder, 2007", font=font, size=5, color="#c8c6c6")
ax.text(x=40_200, y=41, s="matplotlib-journey.com", font=font, size=5, color="#c8c6c6")

ax.set_xlabel("GDP/capita", fontdict={"font": font})
ax.set_ylabel("Life Expectancy", fontdict={"font": font})

fig.savefig("gapminder/gapminder-good.png", dpi=300, bbox_inches="tight")
