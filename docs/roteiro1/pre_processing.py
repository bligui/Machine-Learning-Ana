import pandas as pd
import numpy as np

# carregar dataset
df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")

# tratar dados
df.fillna(df.median(numeric_only=True), inplace=True)

# outliers
num_df = df.select_dtypes(include=[np.number])

# z-score
z_scores = np.abs((num_df - num_df.mean()) / num_df.std())
outliers = (z_scores > 3).sum().sum()
print("Número de outliers detectados:", outliers)

# mostrar
print(df.head())

# ENCODING

df["Sex"] = df["Sex"].map({"M": 1, "F": 0})
df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
df["RestingECG"] = df["RestingECG"].map({"Normal": 0, "ST": 1, "LVH": 2})
df["ExerciseAngina"] = df["ExerciseAngina"].map({"Y": 1, "N": 0})
df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})


print(df.head())

# NORMALIZACAO

numeric_cols = df.select_dtypes(include=[np.number]).columns


df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())


df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()


print("Min-Max Normalized:")
print(df.head())

print("\nStandardized:")
print(df.head())