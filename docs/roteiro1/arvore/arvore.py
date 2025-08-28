import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# pré processamento
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

# dividir variáveis
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# limitar profundidade da árvore
classifier = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
classifier.fit(X_train, y_train)

# avaliar modelo
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Validation Accuracy: {accuracy:.4f}")

# plotar árvore mais compacta
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=X.columns, class_names=["No Disease", "Disease"], filled=True, fontsize=9)

buffer = StringIO()
plt.savefig(buffer, format="svg", transparent=True)
print(buffer.getvalue())
