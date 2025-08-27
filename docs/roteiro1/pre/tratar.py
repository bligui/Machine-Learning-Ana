import pandas as pd
import numpy as np

def preprocess(df):
    df.fillna(df.median(numeric_only=True), inplace=True)
    num_df = df.select_dtypes(include=[np.number])
    z_scores = np.abs((num_df - num_df.mean()) / num_df.std())
    outliers = (z_scores > 3).sum().sum()
    # imprime só o número (sem quebrar a tabela depois)
    print(f"**Número de outliers detectados:** {outliers}\n")
    return df

df = pd.read_csv("https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/dados/heart.csv")
df = preprocess(df)

# imprime tabela em markdown (sem texto junto)
print(df.sample(n=10, random_state=42).to_markdown(index=False))
