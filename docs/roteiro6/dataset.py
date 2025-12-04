
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
from scipy import stats

# ----------------------------------------------------------
# 1. Leitura do dataset diretamente da URL
# ----------------------------------------------------------

url = "https://raw.githubusercontent.com/bligui/Machine-Learning-Ana/refs/heads/main/docs/roteiro6/soc-Epinions1.txt"

df = pd.read_csv(
    url,
    sep="\s+",
    comment="#",
    header=None,
    names=["source", "target"]
)

print("Dataset carregado com sucesso!")
print(df.head())
print(df.shape)