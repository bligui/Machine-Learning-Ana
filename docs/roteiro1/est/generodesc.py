import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()


# --- PLOT: Distribuição por Sexo ---
fig, ax = plt.subplots(1, 1, figsize=(6, 4))

counts = df["Sex"].value_counts().sort_index()
ax.bar(counts.index, counts.values, color=["pink", "skyblue"], edgecolor="lightcoral")

ax.set_title("Distribuição por Sexo")
ax.set_xlabel("Sexo (F=0, M=1)")
ax.set_ylabel("Contagem")
ax.set_xticks([0, 1])
ax.set_xticklabels(["Feminino", "Masculino"])
ax.grid(axis="y", linestyle="--", alpha=0.6)

# salvar em buffer como SVG
buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
