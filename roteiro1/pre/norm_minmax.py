import pandas as pd
import numpy as np

def preprocess(df):
    # Preencher valores ausentes
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Detectar outliers com Z-Score
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

# Selecionar colunas numéricas
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Min-Max Normalization
df_minmax = df.copy()
df_minmax[numeric_cols] = (df_minmax[numeric_cols] - df_minmax[numeric_cols].min()) / (df_minmax[numeric_cols].max() - df_minmax[numeric_cols].min())

# Standardization (Z-score)
df_standard = df.copy()
df_standard[numeric_cols] = (df_standard[numeric_cols] - df_standard[numeric_cols].mean()) / df_standard[numeric_cols].std()

# Mostrar resultados em tabelas markdown
print("### Min-Max Normalized\n")
print(df_minmax.sample(n=10, random_state=42).to_markdown(index=False))
