# Page Rank - Rede Social
---

Redes sociais são estruturas compostas por entidades que interagem entre si por meio de conexões que podem representar amizade, influência, comunicação ou confiança. Quando lidamos com redes de reputação, como a Epinions, entender quem são os indivíduos mais influentes significa identificar quais usuários são vistos como referências confiáveis pelos demais.

O dataset soc-Epinions1 representa uma rede de confiança onde cada aresta dirigida A → B significa que o usuário A confia em B. É um grafo grande, com aproximadamente 75 mil usuários e mais de 500 mil conexões, que captura interações reais entre produtores e consumidores de reviews.

O objetivo deste relatório é aplicar o algoritmo PageRank para identificar usuários influentes, analisando como diferentes valores do fator de amortecimento afetam os resultados, comparando uma implementação manual com a função nativa do NetworkX e interpretando o papel dos usuários de maior relevância dentro da dinâmica da rede.

---

## Fundamentos Teóricos
A rede soc-Epinions1 é dirigida porque a confiança é assimétrica. A confiar em B não implica que B confia em A.
Chamamos os nós de usuários e as arestas dirigidas de relações de confiança.

---

## Dataset
O dataset está disponível publicamente e foi acessado pelo link direto: https://snap.stanford.edu/data/soc-Epinions1.html

Características principais:
• aproximadamente 75.879 usuários
• aproximadamente 508.837 arestas dirigidas
• cada linha contém dois IDs indicando uma relação de confiança A B

Este é um dos maiores e mais tradicionais datasets de confiança presentes no repositório SNAP da Universidade Stanford. Ele possui estrutura típica de redes sociais reais: distribuição de grau em cauda longa, hubs, componentes densas e grande conectividade.

---


