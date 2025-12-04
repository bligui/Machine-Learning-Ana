import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay

# carregar df (se já tem df carregado, remova esta linha)
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# preparar dados para visualização 2D
X_vis = df[["Age", "Cholesterol"]].values
y_vis = df["HeartDisease"].values
X_vis_scaled = StandardScaler().fit_transform(X_vis)

# criar 2x2 subplots igual ao prof
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.ravel()
kernels = ["linear", "sigmoid", "poly", "rbf"]

for ax, k in zip(axes, kernels):
    svm_vis = SVC(kernel=k, C=1)
    svm_vis.fit(X_vis_scaled, y_vis)

    DecisionBoundaryDisplay.from_estimator(
        svm_vis,
        X_vis_scaled,
        response_method="predict",
        alpha=0.8,
        cmap="Pastel1",
        ax=ax
    )

    ax.scatter(
        X_vis_scaled[:, 0],
        X_vis_scaled[:, 1],
        c=y_vis,
        s=40,
        edgecolors="k",   # borda preta igual ao exemplo do prof
        linewidths=0.5,
        cmap="viridis"    # só para garantir a coloração dos pontos
    )
    ax.set_title(k)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
