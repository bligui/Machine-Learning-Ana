# Page Rank - Rede Social
---

O objetivo deste trabalho é aplicar o algoritmo PageRank em uma rede social real de grande escala, avaliando sua capacidade de identificar usuários influentes em um sistema de confiança. Para isso, utilizamos o dataset soc-Epinions1, uma base pública amplamente usada em pesquisas sobre redes complexas. Ela representa relações de confiança entre usuários do site de reviews Epinions, onde uma aresta dirigida A → B significa que A confia em B.

Trata-se de uma rede dirigida, realista, com alta densidade e grande assimetria de graus, com:

- 75.879 nós (usuários)

- 508.837 arestas dirigidas (relações de confiança)
---

## Metodologia
- Arquivo: soc-Epinions1.txt
- Formato: “FromNodeID ToNodeID”
- Interpretação: A → B → “A confia em B”
- Fonte original: SNAP – Stanford Network Analysis Project

