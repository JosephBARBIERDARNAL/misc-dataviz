import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from drawarrow import ax_arrow


def calculer_impots(salaire):
    tranches = [
        (11294, 0),
        (28797, 0.11),
        (82341, 0.30),
        (177106, 0.41),
        (float("inf"), 0.45),
    ]

    impots = 0
    revenu_restant = salaire
    seuil_prec = 0

    for seuil, taux in tranches:
        if revenu_restant <= 0:
            break
        if salaire <= seuil:
            impots += revenu_restant * taux
            break
        else:
            tranche_imposable = seuil - seuil_prec
            impots += tranche_imposable * taux
            revenu_restant -= tranche_imposable
        seuil_prec = seuil

    return impots


max_salaire = 200_000
salaires = list(range(0, max_salaire + 1000, 1000))
impots = [calculer_impots(salaire) for salaire in salaires]
revenus_nets = [salaire - impot for salaire, impot in zip(salaires, impots)]

df = pd.DataFrame({"brut": salaires, "impot": impots, "net": revenus_nets})
col1 = "#fb8500"
col2 = "#023047"

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_xlim(0, max_salaire)
ax.set_ylim(0, max_salaire)
ax.axis("off")

arrow_args = dict(color="black", clip_on=False, fill_head=False, zorder=20)
ax_arrow((0, 0), (max_salaire * 1.05, 0), **arrow_args)
ax_arrow((0, 0), (0, max_salaire * 1.05), **arrow_args)
ax.text(x=max_salaire * 1.05, y=-7000, s="Revenu brut", size=15, ha="center")
ax.text(x=5000, y=max_salaire * 1.03, s="Revenu net", size=15, va="center")

seuils = [11294, 28797, 82341, 177106]
ax.vlines(x=seuils, ymin=-1000, ymax=1000, clip_on=False, color="black", lw=0.7)
for seuil in seuils:
    ax.text(x=seuil, y=-5000, s=f"{seuil}€", ha="center", color="#4f4f4f", size=8)

ax.plot(df["brut"], df["net"], lw=3, color=col2)
ax.plot([0, max_salaire], [0, max_salaire], lw=3, color=col1)

ax.text(x=203_000, y=200_000, s="Brut = Net", color=col1, size=15, weight="bold")
ax.text(
    x=203_000, y=133_000, s="Revenu après impôt", color=col2, size=15, weight="bold"
)

ax.text(x=83_000, y=60_000, s="64352€")
ax.text(x=83_000, y=74_000, s="~22% d'impôt", rotation=20, size=8)
ax.text(x=178_000, y=115_000, s="120264€")

ax_arrow(
    (82341, 82341), (82341, 64352), double_headed=True, color="black", fill_head=False
)

fig.text(x=0.5, y=1.08, s="Impôt sur le revenu en France", size=35, ha="center")

const = 5000
y = 160000
text_args = dict(rotation=90, color="black", va="center", ha="center")
ax.text(x=0 + const, y=y, s="0% d'imposition", **text_args)
ax.text(x=11294 + const, y=y, s="11% d'imposition", **text_args)
ax.text(x=28797 + const, y=y, s="30% d'imposition", **text_args)
ax.text(x=82341 + const, y=y, s="41% d'imposition", **text_args)
ax.text(x=177106 + const, y=y, s="45% d'imposition", **text_args)

color = "#c5c4c4"
ax.add_patch(patch.Rectangle((0, 0), 11294, max_salaire, alpha=0, color=color))
ax.add_patch(
    patch.Rectangle((11294, 0), 28797 - 11294, max_salaire, alpha=0.1, color=color)
)
ax.add_patch(
    patch.Rectangle((28797, 0), 82341 - 28797, max_salaire, alpha=0.2, color=color)
)
ax.add_patch(
    patch.Rectangle((82341, 0), 177106 - 82341, max_salaire, alpha=0.3, color=color)
)
ax.add_patch(
    patch.Rectangle(
        (177106, 0), max_salaire - 177106, max_salaire, alpha=0.4, color=color
    )
)

fig.tight_layout()
fig.savefig("taxes/taxes.png", dpi=300, bbox_inches="tight")
