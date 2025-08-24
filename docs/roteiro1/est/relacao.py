import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()

# ENCODING
df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})

# NORMALIZAÇÃO
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

# --- PLOT: ChestPainType vs HeartDisease ---
fig, ax = plt.subplots(figsize=(8, 5))

# contar combinações
counts = df.groupby(["ChestPainType", "HeartDisease"]).size().unstack(fill_value=0)

# pegar os nomes das colunas dinamicamente (resolve problema com float/int)
cols = counts.columns.tolist()  # ex: [0.0, 1.0]

# posições das barras
x = np.arange(len(counts.index))
width = 0.35

# barras
bars1 = ax.bar(x - width/2, counts[cols[0]], width, label="Não", color="pink", edgecolor="darkred")
bars2 = ax.bar(x + width/2, counts[cols[1]], width, label="Sim", color="salmon", edgecolor="darkred")

# adicionar valores de contagem acima das barras
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)),
            ha="center", va="bottom", fontsize=9)

ax.set_title("Relação entre ChestPainType e HeartDisease")
ax.set_xlabel("Tipo de Dor no Peito")
ax.set_ylabel("Contagem")
ax.set_xticks(x)
ax.set_xticklabels(["TA", "ATA", "NAP", "ASY"])
ax.legend(title="HeartDisease")
ax.grid(axis="y", linestyle="--", alpha=0.6)

# salvar em buffer como SVG
buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
