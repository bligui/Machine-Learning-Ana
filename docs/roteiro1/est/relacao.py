import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()

# --- PLOT: ChestPainType vs HeartDisease ---
fig, ax = plt.subplots(figsize=(8, 5))

# contar combinações
counts = df.groupby(["ChestPainType", "HeartDisease"]).size().unstack(fill_value=0)

# pegar as classes de HeartDisease dinamicamente (0 e 1)
cols = counts.columns.tolist()

# posições das barras
x = np.arange(len(counts.index))
width = 0.35

# barras
bars1 = ax.bar(x - width/2, counts[cols[0]], width, label="Não", color="pink", edgecolor="darkred")
bars2 = ax.bar(x + width/2, counts[cols[1]], width, label="Sim", color="salmon", edgecolor="darkred")

# adicionar valores de contagem acima das barras
for bar in list(bars1) + list(bars2):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)),
            ha="center", va="bottom", fontsize=9)

ax.set_title("Relação entre ChestPainType e HeartDisease")
ax.set_xlabel("Tipo de Dor no Peito")
ax.set_ylabel("Contagem")
ax.set_xticks(x)
ax.set_xticklabels(counts.index)  # usa os nomes originais (TA, ATA, NAP, ASY)
ax.legend(title="HeartDisease")
ax.grid(axis="y", linestyle="--", alpha=0.6)

# salvar em buffer como SVG
buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
