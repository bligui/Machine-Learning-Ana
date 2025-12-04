import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from io import StringIO

df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

X_vis = df[["Age", "Cholesterol"]].values
y_vis = df["HeartDisease"].values
X_vis_scaled = StandardScaler().fit_transform(X_vis)

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
        edgecolors="k",
        linewidths=0.5,
    )
    ax.set_title(k)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()

buffer = StringIO()
plt.savefig(buffer, format="svg", transparent=True)
print(buffer.getvalue())
# não chamar plt.show() nem plt.close() aqui para garantir que o RMarkdown capture o SVG
