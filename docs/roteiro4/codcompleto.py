import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, balanced_accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# preprocessamento
def preprocess(df):
    df = df.copy()
    if df["HeartDisease"].dtype != int:
        df["HeartDisease"] = df["HeartDisease"].astype(int)
    
    df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
    df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
    df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
    df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})
    
    return df

# knn
def run_knn(df):
    df = preprocess(df)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())

    X = df.drop("HeartDisease", axis=1)
    y = df["HeartDisease"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    y_prob = knn.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, predictions)
    balanced_acc = balanced_accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    report = classification_report(y_test, predictions, digits=2)
    auc = roc_auc_score(y_test, y_prob)

    # Curva ROC
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.figure(figsize=(6,4))
    plt.plot(fpr, tpr, label=f"KNN (AUC={auc:.2f})")
    plt.plot([0,1], [0,1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Curva ROC - KNN")
    plt.legend()
    plt.show()

    # Matriz de confusão
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.xlabel("Predito")
    plt.ylabel("Real")
    plt.title("Matriz de Confusão - KNN")
    plt.show()

    print("\n🔹 Resultados KNN")
    print(f"Accuracy: {acc:.2f}")
    print(f"Balanced Accuracy: {balanced_acc:.2f}")
    print(f"AUC-ROC: {auc:.2f}")
    print("\nClassification Report:")
    print(report)

# kmeans
def run_kmeans(df, n_clusters=3):
    df = preprocess(df)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())

    X = df[numeric_cols].values

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", max_iter=300, random_state=42)
    labels = kmeans.fit_predict(X)

    inertia = kmeans.inertia_
    sil_score = silhouette_score(X, labels)

    df_clusters = df.copy()
    df_clusters["Cluster"] = labels
    cluster_vs_target = pd.crosstab(df_clusters["Cluster"], df_clusters["HeartDisease"], normalize="index") * 100

    # Plot distribuição clusters
    cluster_vs_target.plot(kind="bar", stacked=True, figsize=(6,4), colormap="coolwarm")
    plt.ylabel("% Pacientes")
    plt.title("Distribuição de HeartDisease por Cluster (K-Means)")
    plt.legend(title="HeartDisease", loc="upper right")
    plt.show()

    print("\n🔹 Resultados K-Means")
    print(f"Inércia (WSS): {inertia:.2f}")
    print(f"Silhouette Score: {sil_score:.2f}")
    print("\nDistribuição (%) de HeartDisease por cluster:")
    print(cluster_vs_target)


if __name__ == "__main__":
    df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

    # Rodar KNN
    run_knn(df)

    # Rodar K-Means
    run_kmeans(df, n_clusters=3)
