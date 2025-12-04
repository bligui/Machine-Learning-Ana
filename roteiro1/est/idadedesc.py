import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)
df = df.drop_duplicates()


# --- PLOT ---
fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# histograma normalizado
ax.hist(df["Age"], bins=20, color="pink", edgecolor="lightcoral", alpha=0.6, density=True)

# curva de densidade (gaussiana simples)
x_vals = np.linspace(df["Age"].min(), df["Age"].max(), 200)
mean = df["Age"].mean()
std = df["Age"].std()
pdf = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - mean) / std) ** 2)

ax.plot(x_vals, pdf, color="darkred", linewidth=2, label="Curva de densidade")

ax.set_title("Distribuição da Idade")
ax.set_xlabel("Idade")
ax.set_ylabel("Densidade")
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.legend()

buffer = BytesIO()
plt.savefig(buffer, format="svg", bbox_inches="tight")
buffer.seek(0)
print(buffer.getvalue().decode("utf-8"))
