import matplotlib.pyplot as plt
from drawarrow import ax_arrow

happiness = [10, 10, 10, 10, 30, 50, 50, 50, 50]

with plt.xkcd():
    fig, ax = plt.subplots()

    ax.plot(happiness, color="#cf3e3e")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_ylim(0, 55)
    ax.set_xlabel("Time since I started coding")
    ax.set_ylabel("Happiness")
    ax.text(
        x=2.5, y=40, s="The day I stopped\nusing notebooks", va="center", ha="center"
    )
    ax_arrow([2.5, 36], [3, 11], color="black", width=1.5)

    fig.savefig("xkcd/notebooks/main.png", dpi=300)
