import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd

# pre processamento
def preprocess(df):
    df.fillna(df.median(numeric_only=True), inplace=True)

    df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
    df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
    df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
    df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})
    return df

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")
df = preprocess(df)

numeric_cols = df.select_dtypes(include=[np.number]).columns

# Normalização Min-Max
df_minmax = df.copy()
df_minmax[numeric_cols] = (df_minmax[numeric_cols] - df_minmax[numeric_cols].min()) / (
    df_minmax[numeric_cols].max() - df_minmax[numeric_cols].min()
)

X = df_minmax[numeric_cols].values

# k-means
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=42)
labels = kmeans.fit_predict(X)

# visualizacao
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
centers_pca = pca.transform(kmeans.cluster_centers_)

plt.figure(figsize=(12, 10))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="viridis", s=60, alpha=0.7, edgecolor="k")
plt.scatter(centers_pca[:, 0], centers_pca[:, 1], c="red", marker="*", s=250, label="Centroids")
plt.title("K-Means Clustering (Heart Dataset) - PCA 2D Projection")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()


# Print centroids and inertia 
# print("Final centroids:", kmeans.cluster_centers_) 
# print("Inertia (WCSS):", kmeans.inertia_)

buffer = StringIO()
plt.savefig(buffer, format="svg", transparent=True)
print(buffer.getvalue())