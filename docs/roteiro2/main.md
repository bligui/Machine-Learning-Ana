# KNN - Doenças Cardiovasculares

---

O KNN é um modelo baseado em instâncias, que classifica cada observação de acordo com as classes mais frequentes entre seus vizinhos mais próximos em um espaço multidimensional. Neste caso, optei por utilizar k = 3 vizinhos.

**O Pré-Processamento já foi feito e pode ser encontrado em: [Árvore de Decisão](https://bligui.github.io/Machine-Learning-Ana/roteiro1/main/#2-pre-processamento){:target='_blank'}**

---

### Seleção de Variáveis para Visualização

Para gerar a fronteira de decisão e facilitar a interpretação dos resultados, escolhemos as variáveis:

`Age` (Idade): fator de risco importante e diretamente associado a doenças cardiovasculares.

`Oldpeak` (Depressão do Segmento ST): medida obtida no eletrocardiograma (ECG) que indica a diferença entre o nível de repouso e o nível durante o exercício. Valores alterados podem sugerir isquemia miocárdica, ou seja, redução do fluxo sanguíneo para o coração, sendo altamente relevantes no diagnóstico de doenças cardíacas.

A escolha dessas duas variáveis se justifica porque elas apresentam boa variação na base de dados, não sofrem tanto com valores artificiais como ocorre em colesterol e pressão, e têm forte relevância clínica.

---

### Treinamento e Avaliação

O modelo foi treinado com a mesma divisão de dados da Árvore de Decisão:

- **Treino (70%)**
- **Teste (30%)**

O desempenho do modelo foi medido com a acurácia (accuracy), que representa a proporção de classificações corretas no conjunto de teste.

- **Acurácia obtida: 0.84 (84%)**


=== "Result"

    ```python exec="1" html="1"
    --8<-- "docs/roteiro2/KNN.py"
    ```

=== "Code"

    ```python
    --8<-- "docs/roteiro2/KNN.py"
    ```
---

### Conclusões
O modelo KNN apresentou um desempenho semelhante ao da Árvore de Decisão, com acurácia em torno de 84%. Isso reforça a consistência dos padrões encontrados no dataset, independentemente do algoritmo utilizado.
No entanto, como o KNN classifica novos exemplos com base na distância em relação aos dados de treino, ele pode ser mais sensível a ruídos e outliers. Além disso, a escolha do valor de `k` influencia diretamente o resultado, sendo necessário avaliar diferentes valores para identificar o melhor ajuste.