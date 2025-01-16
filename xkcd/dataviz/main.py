import matplotlib.pyplot as plt
from drawarrow import ax_arrow

confidence = [
    10,
    10,
    10,
    5,
    5,
    5,
    20,
    20,
    20,
    25,
    25,
    25,
    10,
    10,
    10,
    40,
    40,
    40,
    5,
    5,
    5,
    -10,
    -10,
    -10,
]
x = list(range(len(confidence)))
labels = [
    "I can make charts with Excel,\nI'm the boss",
    "I discover R and ggplot, overwhelmed",
    "ChatGPT comes in, finally\nI can make nice things",
    "Getting paid to do Matplotlib,\nI'm the king",
    "See what others do, I'm\nactually not that great",
    "Doing Matplotlib all the time,\nfeeling unbeatable",
    "About to discover D3.js and\nthe interactive world",
    "Visualization with Blender and 3D tools",
]

with plt.xkcd():
    fig, ax = plt.subplots(figsize=(15, 5), dpi=300)

    ax.plot(x, confidence, color="#cf3e3e", clip_on=False, lw=3)
    ax.plot(x[-7:], confidence[-7:], color="#a0a0a0", clip_on=False, zorder=10, lw=3)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_xlabel("Time")
    ax.set_ylabel("Confidence")
    ax.set_xticks([])
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.set_ylim(0, 42)
    ax.text(x=0, y=40, s="My dataviz journey", size=30, weight="bold")
    ax.text(x=20, y=27, s="I'm here", ha="center")
    ax_arrow([20, 30], [17.3, 39], color="black", width=2)

    for i in range(len(labels)):
        ax.text(
            x=i * 3 + 1, y=confidence[i * 3] + 2, s=labels[i], ha="center", zorder=100
        )

    fig.savefig("xkcd/dataviz/main.png", dpi=300, bbox_inches="tight")
