# KNN - Doenças Cardiovasculares

---

O KNN é um modelo baseado em instâncias, que classifica cada observação de acordo com as classes mais frequentes entre seus vizinhos mais próximos em um espaço multidimensional. Neste caso, optei por utilizar k = 3 vizinhos.

**O Pré-Processamento já foi feito e pode ser encontrado em: [Árvore de Decisão](https://bligui.github.io/Machine-Learning-Ana/roteiro1/main/#2-pre-processamento){:target='_blank'}**

---

### Objetivo
Avaliar a relação entre a idade e o colesterol dos pacientes e como essas variáveis podem ser utilizadas para prever risco de doença cardíaca (HeartDisease), utilizando o algoritmo de classificação K-Nearest Neighbors (KNN).

### Variáveis Utilizadas
Para gerar a fronteira de decisão e facilitar a interpretação dos resultados, escolhemos as variáveis:

`Age` (Idade): fator de risco importante e diretamente associado a doenças cardiovasculares.

`Cholesterol` (Colesterol sérico): medido em mg/dl. Níveis altos de colesterol podem indicar risco de acúmulo de placas nas artérias, levando à aterosclerose e maior chance de infarto.

Essas variáveis foram escolhidas porque idade e colesterol estão entre os indicadores mais relevantes na literatura médica para estimar risco cardíaco.

---

### Metodologia
No pré-processamento, foi necessário a normalização de `Age` e `Cholesterol` para trazer ambos para a mesma escala (0 e 1). Depois, fiz a separação e o teste.

A  aplicação do KNN foi com k=3. Ou seja, o modelo classifica um paciente conforme a classe mais frequente entre seus 3 vizinhos mais próximos.

### Resultados Obtidos
- **Doença cardíaca presente (1): 0.55 (55%)**
- **Doença cardíaca ausente (0): 0.44 (44%)**
- **Acurácia obtida: 0.89 (89%)**

=== "Result"

    ```python exec="1" html="1"
    --8<-- "docs/roteiro2/KNN.py"
    ```

=== "Code"

    ```python
    --8<-- "docs/roteiro2/KNN.py"
    ```
---

### Interpretação
- Não há uma separação linear clara entre idade, colesterol e risco de doença cardíaca.

- O KNN conseguiu aproveitar pequenas variações locais e capturar regiões de maior risco, mesmo com sobreposição de dados.

- A alta acurácia (0.89) sugere que, mesmo com apenas duas variáveis, já é possível obter uma predição relevante.

- Contudo, na prática clínica, idade e colesterol não são suficientes isoladamente para um diagnóstico: outros fatores como pressão arterial, diabetes, histórico familiar e estilo de vida devem ser considerados.

### Conclusões
O modelo KNN aplicado em Age vs Cholesterol obteve 89% de acurácia, mostrando que essas variáveis trazem informações relevantes, mas não são suficientes sozinhas para explicar completamente a ocorrência de doenças cardíacas.