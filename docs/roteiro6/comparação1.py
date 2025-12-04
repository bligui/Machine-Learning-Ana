
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

# print("Dataset carregado com sucesso!")
# print(df.head())
# print(df.shape)

# ----------------------------------------------------------
# 2. Construção do grafo
# ----------------------------------------------------------

G = nx.DiGraph()
G.add_edges_from(df.values.tolist())

# print(f"Grafo criado: {G.number_of_nodes():,} nós, {G.number_of_edges():,} arestas")

# ----------------------------------------------------------
# 3. Implementação do PageRank do zero
# ----------------------------------------------------------

def pagerank_scratch(G, d=0.85, tol=1e-6, max_iter=200):
    nodes = list(G.nodes())
    N = len(nodes)
    idx = {n: i for i, n in enumerate(nodes)}

    pr = np.ones(N) / N
    out_deg = np.array([G.out_degree(n) for n in nodes], dtype=float)
    teleport = (1 - d) / N

    incoming = [[] for _ in range(N)]
    for u, v in G.edges():
        incoming[idx[v]].append(idx[u])

    for iteration in range(max_iter):
        pr_new = np.zeros(N)

        # soma das contribuições
        for i in range(N):
            s = 0
            for j in incoming[i]:
                if out_deg[j] > 0:
                    s += pr[j] / out_deg[j]
            pr_new[i] = teleport + d * s

        # tratamento de dangling nodes
        dangling = pr[out_deg == 0].sum()
        if dangling > 0:
            pr_new += d * dangling / N

        # erro L1
        err = np.abs(pr_new - pr).sum()
        if err < tol:
            return {nodes[i]: float(pr_new[i]) for i in range(N)}, iteration, err

        pr = pr_new

    return {nodes[i]: float(pr[i]) for i in range(N)}, max_iter, err

# ----------------------------------------------------------
# 4. Execução do PageRank do zero
# ----------------------------------------------------------

# print("Rodando PageRank do zero...")
start = time.time()
pr_scratch, iters, err = pagerank_scratch(G, d=0.85)
end = time.time()

# print(f"Convergiu em {iters} iterações, erro final {err:.2e}")
# print(f"Tempo total: {end - start:.2f}s")

# ----------------------------------------------------------
# 5. PageRank do NetworkX
# ----------------------------------------------------------

# print("Rodando networkx.pagerank...")
pr_nx = nx.pagerank(G, alpha=0.85, tol=1e-8)

# ----------------------------------------------------------
# 6. Comparação e Top-10
# ----------------------------------------------------------

def topk(d, k=10):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]

top10_scratch = topk(pr_scratch, 10)
top10_nx = topk(pr_nx, 10)

print("\nTOP 10 (scratch):")
for r, (n, s) in enumerate(top10_scratch, 1):
    print(r, n, s)

# print("\nTOP 10 (networkx):")
# for r, (n, s) in enumerate(top10_nx, 1):
    # print(r, n, s)
