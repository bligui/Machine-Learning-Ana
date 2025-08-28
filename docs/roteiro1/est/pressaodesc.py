import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()


# --- PLOT: Boxplot da Pressão Arterial em Repouso ---
fig, ax = plt.subplots(figsize=(7, 5))

bp = ax.boxplot(df["RestingBP"], patch_artist=True, widths=0.5)

# customização
for box in bp["boxes"]:
    box.set(facecolor="pink", edgecolor="lightcoral", linewidth=1.2)
for whisker in bp["whiskers"]:
    whisker.set(color="lightcoral", linewidth=1.2)
for cap in bp["caps"]:
    cap.set(color="lightcoral", linewidth=1.2)
for median in bp["medians"]:
    median.set(color="darkred", linewidth=1.5)

ax.set_title("Boxplot da Pressão Arterial em Repouso")
ax.set_xlabel("Pressão Arterial (mm Hg)")
ax.set_xticks([])  # remove eixo X categórico
ax.grid(axis="y", linestyle="--", alpha=0.6)

# salvar em buffer como SVG
buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
