import pandas as pd
import numpy as np

df = pd.read_csv("")

# missing
df.fillna(df.median(numeric_only=True), inplace=True)

# outliers
z_scores = np.abs((df - df.mean()) / df.std())
outliers = (z_scores > 3).sum().sum()
print("Número de outliers detectados:", outliers)


print(df.head().to_markdown(index=False))