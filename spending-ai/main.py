import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("spending-ai/data.csv")
df["average_user"] = df["spending"] / df["download"]


fig, ax = plt.subplots(figsize=(8, 6))

sns.barplot(y="provider", x="download", hue="platform", data=df, gap=0.2, ax=ax)

fig.savefig("spending-ai/output.png", dpi=300, bbox_inches="tight")
