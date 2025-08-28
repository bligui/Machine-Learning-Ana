import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()

# --- PLOT: Distribuição da Variável Alvo ---
fig, ax = plt.subplots(figsize=(6, 4))

counts = df["HeartDisease"].value_counts().sort_index()
ax.bar(counts.index, counts.values, color=["pink", "lightcoral"], edgecolor="darkred")

ax.set_title("Distribuição da Variável Alvo (HeartDisease)")
ax.set_xlabel("HeartDisease (0 = Não, 1 = Sim)")
ax.set_ylabel("Contagem")
ax.set_xticks([0, 1])
ax.set_xticklabels(["Não", "Sim"])
ax.grid(axis="y", linestyle="--", alpha=0.6)

# salvar em buffer como SVG
buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
