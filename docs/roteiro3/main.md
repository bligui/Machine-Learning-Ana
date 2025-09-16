# K-Means - Doenças Cardiovasculares
Aplicar o algoritmo de K-Means ao dataset de doenças cardíacas para verificar se é possível identificar grupos de pacientes com perfis semelhantes, sem utilizar a variável alvo (HeartDisease). O objetivo aqui não é prever, mas descobrir padrões ocultos (aprendizado não supervisionado).

**O Pré-Processamento já foi feito e pode ser encontrado em: [Árvore de Decisão](https://bligui.github.io/Machine-Learning-Ana/roteiro1/main/#2-pre-processamento){:target='_blank'}**

### Algoritmo
K-Means configurado com:
- `n_clusters=3` (três grupo)
- `init="k-means++"` (boa inicialização dos centróides)
- `max_iter=300` (número máximo de iterações)

### Visualização
Como os dados têm múltiplas dimensões, aplicou-se PCA (Análise de Componentes Principais) para reduzir para 2 dimensões (PC1 e PC2), permitindo representar os clusters graficamente.

### Resultados Obtidos
**Centroides finais (em espaço normalizado):**
- Foram obtidos 3 centróides representando os "perfis médios" de cada grupo de pacientes.
(valores mostrados no código, em escala normalizada entre 0 e 1).

**Inércia (WCSS - Within-Cluster Sum of Squares):**
- Valor: **712.73**
- Esse número representa a soma das distâncias quadráticas dos pontos em relação ao seu centróide. Quanto menor, mais compactos e coesos são os clusters.

**Visualização dos Clusters (via PCA):**
- O gráfico mostra os pacientes distribuídos em três grupos.
- Cada cor representa um cluster.
- Os pontos vermelhos em formato de estrela representam os centróides (pontos médios dos clusters).
- Observa-se que os grupos são relativamente bem definidos, mas ainda com algumas sobreposições.

=== "Result"

    ```python exec="1" html="1"
    --8<-- "docs/roteiro3/Kmeans.py"
    ```

=== "Code"

    ```python
    --8<-- "docs/roteiro3/Kmeans.py"
    ```
---

### Interpretação
- O algoritmo conseguiu separar a população em três grupos principais, possivelmente relacionados a perfis de risco cardiovascular diferentes.

- Como a variável HeartDisease não foi usada, o modelo não sabe quem tem ou não a doença, mas pode ser interessante comparar depois os clusters com a variável alvo para verificar se existe relação entre eles e a presença da doença.

- O PCA reduziu a dimensionalidade para 2 componentes, o que ajuda na visualização, mas simplifica a informação original. Mesmo assim, os clusters mostraram certa estrutura.

### Conclusão
O algoritmo K-Means (k=3) conseguiu identificar três grupos distintos de pacientes, mesmo sem utilizar a variável alvo. A inércia encontrada (712,73) indica um nível razoável de coesão interna. Esse tipo de análise pode ser útil para segmentar pacientes em grupos de risco e auxiliar em análises médicas exploratórias.