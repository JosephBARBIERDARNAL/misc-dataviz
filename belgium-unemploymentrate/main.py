import pandas as pd
import cartopy.crs as ccrs
import geopandas as gpd
import matplotlib.pyplot as plt
from pypalettes import add_cmap
from pyfonts import load_font
import unicodedata

if not x:
    x = 0


def remove_accents(text):
    return "".join(
        c if not unicodedata.combining(c) else ""
        for c in unicodedata.normalize("NFKD", text)
    )


belgium = gpd.read_file("belgium-unemploymentrate/belgium.json").drop(
    columns=[
        "prov_nis",
        "prov_fr",
        "prov_nl",
        "arr_nis",
        "id",
        "reg_nis",
        "reg_nl",
        "reg_fr",
        "arr_fr",
        "arr_nl",
        "nis",
    ]
)
belgium["name_nl"] = belgium["name_nl"].apply(remove_accents).str.lower()

rates = pd.read_csv("belgium-unemploymentrate/rate.csv")
rates["Gemeente"] = rates["Gemeente"].apply(remove_accents).str.lower()

df = belgium.merge(rates, left_on="name_nl", right_on="Gemeente", how="left")

projection = ccrs.Mercator()
df.crs = "EPSG:4326"
df_ = df.to_crs(projection.proj4_init)

##########################################################################

regular = load_font(
    "https://github.com/googlefonts/roboto-2/blob/main/src/hinted/Roboto-Regular.ttf?raw=true"
)
bold = load_font(
    "https://github.com/googlefonts/roboto-2/blob/main/src/hinted/Roboto-Bold.ttf?raw=true"
)

cmap = add_cmap(
    colors=[
        "#5A1A74",
        "#661d5c",
        "#86277A",
        "#9D2D7A",
        "#C74370",
        "#FB9A70",
        "#FDC48C",
        "#FED69A",
        "#FCFCBD",
    ][::-1],
    cmap_type="continuous",
    name="Sunset3",
)

fig, ax = plt.subplots(subplot_kw={"projection": projection})
ax.axis("off")

df.plot(
    ax=ax,
    column="Werkloosheidsgraad",
    cmap=cmap,
    edgecolor="#e6e6e6",
    lw=0.3,
)

bar_ax = ax.inset_axes(bounds=[0.05, 0.15, 0.4, 0.3], zorder=-1)
n, bins, _ = bar_ax.hist(df["Werkloosheidsgraad"], bins=18, alpha=0)
colors = [cmap((val - min(bins)) / (max(bins) - min(bins))) for val in bins]
bar_ax.bar(bins[:-1], n, color=colors)
bar_ax.spines[["top", "left", "right"]].set_visible(False)
bar_ax.set_yticks([])
x_ticks = list(range(0, 19, 3))
bar_ax.set_xticks(x_ticks, labels=["0", "3", "6", "9", "12", "15", "18%"], size=8)
bar_ax.tick_params(axis="x", length=2)

fig.text(x=0.2, y=0.89, s="Unemployment rate in Belgium", size=12, font=bold)
fig.text(x=0.2, y=0.86, s="By municipality, in December 2024", size=8, font=regular)
fig.text(
    x=0.2,
    y=0.13,
    s="Map: Koen Van den Eeckhout · Source: RVA (Interactive Statistics)",
    size=6,
    color="#909090",
    font=regular,
)

x += 1
fig.savefig(
    f"belgium-unemploymentrate/intermediate/{x}.png", dpi=300, bbox_inches="tight"
)
