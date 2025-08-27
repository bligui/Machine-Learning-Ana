import pandas as pd
import numpy as np

def preprocess(df):
    # Preencher valores ausentes
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Detectar outliers (Z-Score)
    num_df = df.select_dtypes(include=[np.number])
    z_scores = np.abs((num_df - num_df.mean()) / num_df.std())
    outliers = (z_scores > 3).sum().sum()

    # Encoding categórico
    df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
    df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
    df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
    df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})

    return df

# Carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# Pré-processamento
df = preprocess(df)

# Exibir amostra (markdown)
print(df.sample(n=10, random_state=42).to_markdown(index=False))
