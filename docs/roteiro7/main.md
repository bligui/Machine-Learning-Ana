# SVM - Doenças Cardiovasculares

---

**A descrição dos dados já foi feita: [Árvore de Decisão](https://bligui.github.io/Machine-Learning-Ana/roteiro1/main/#2-pre-processamento){:target='_blank'}**

---

O objetivo deste estudo é construir e avaliar modelos de classificação utilizando Máquinas de Vetores de Suporte (SVM) aplicadas ao dataset de doença cardíaca. Além de treinar o modelo, foram geradas visualizações das fronteiras de decisão para diferentes kernels, permitindo comparar seu comportamento.

Consiste em prever a variável alvo HeartDisease, que indica se um indivíduo apresenta risco de doença cardíaca.

---
## Pré-processamento dos dados

Para que os modelos SVM funcionassem adequadamente, foram aplicados os seguintes passos:

### Tratamento de variáveis categóricas

As colunas de texto foram transformadas em variáveis numéricas com One-Hot Encoding, convertendo categorias em indicadores binários.

### Padronização das variáveis numéricas

Foi aplicada a técnica StandardScaler, que transforma cada feature para média 0 e desvio padrão 1. Isso é essencial em SVM, pois a distância entre pontos no espaço influencia fortemente o kernel.

### Divisão treino-teste

Os dados foram divididos em:

• 80 por cento para treino
• 20 por cento para teste
• Amostragem estratificada, preservando o equilíbrio entre classes

---

## Modelo SVM
Foi construída uma pipeline contendo:

- Pré-processamento (escala e one-hot encoding)

- Classificador SVM com ponderação automática das classes

Para seleção do melhor modelo, utilizou-se GridSearchCV com validação cruzada 5-fold.
Os parâmetros avaliados foram:

• kernel: linear, poly, rbf, sigmoid
• C: 0.1, 1, 10
• gamma: scale e auto

O critério de otimização foi a métrica F1, apropriada em classificações com classes potencialmente desbalanceadas.

---


=== "Result"

    ```python exec="1" html="1"
    --8<-- "docs/roteiro7/svm2.py"
    ```

=== "Code"

    ```python
    --8<-- "docs/roteiro7/svm2.py"
    ```
---

## Interpretação por kernel

### Linear

- O gráfico mostra uma região de separação quase plana entre classes. Isso indica que, considerando apenas Age e Cholesterol em escala padronizada, existe uma tendência global em que uma combinação linear dessas duas variáveis ajuda a separar indivíduos com e sem HeartDisease.

- Observação importante: muitos pontos estão muito próximos da linha de separação. Esses pontos próximos ao limiar são os mais sujeitos a erros de classificação.

- Implicação: se o comportamento real for aproximadamente linear nessa projeção 2D, um modelo linear pode ser mais simples e interpretável. Caso contrário, ele pode subestimar relações não lineares que aparecem quando se usam mais features.

### Sigmoid

- As regiões parecem fragmentadas, quase cruzadas. O kernel sigmoid pode se comportar de forma similar a uma rede neural de camada única, criando múltiplas regiões.

- Aqui o resultado sugere que o kernel sigmoid está sendo sensível a pontos extremos e ruído, gerando cortes não intuitivos.

- Implicação: normalmente o kernel sigmoid não é a primeira escolha para a maioria dos problemas tabulares. Se ele produzir boas métricas com validação, vale investigar; mas cuidado com instabilidade e sensibilidade a escala e hiperparâmetros.

### Poly (polinomial)

- As fronteiras ficam mais curvas, capturando relações não lineares moderadas. É visível que o poly aproxima regiões onde a classe positiva ocupa um “canto” dos dados.

- Observação: dependendo do grau do polinômio, pode surgir sobreajuste, especialmente em projeções mais ruidosas.

- Implicação: poly dá flexibilidade extra, mas precisa de regularização (C) e escolha do grau com validação.

### RBF

- O kernel rbf formou regiões isoladas e não-convexas, inclusive “bolhas” que capturam aglomerados localizados da classe positiva. Isso é típico do rbf ao modelar relações complexas.

- No gráfico aparece pelo menos uma “ilha” isolada em que o modelo classifica como positivo apesar de estar afastada, possivelmente resultado de poucos pontos e sensibilidade local.

- Implicação: rbf costuma ter melhor desempenho quando a verdadeira separação é não linear, mas é também o que mais corre risco de sobreajuste se gamma for alto.

### Padrões observáveis e suas causas prováveis

- Muitos pontos alinhados na parte inferior (Cholesterol padronizado ~ -2 a -3)
    - Isso indica valores discretos ou agrupados na feature Cholesterol no dataset original (por exemplo, registros com valor 0 ou limites). Pode ser artefato de coleta/limpeza. Verificar distribuição bruta em df["Cholesterol"].value_counts().

- Regiões de alta sobreposição entre classes
    - Há uma faixa central onde os dois classes coexistem bastante. Isso sugere que Age e Cholesterol sozinhos não são suficientes para separação perfeita. Outras features (ex.: ChestPainType, MaxHR, ExerciseAngina) provavelmente carregam sinal discriminativo relevante.

- Pontos próximos às fronteiras = candidatos a erro
    - Pontos na vizinhança das linhas de decisão tendem a ser confundidos. Identificá-los ajuda a explicar falsos positivos e falsos negativos.

- “Ilhas” do kernel RBF
    - Podem sinalizar grupos locais relevantes ou overfitting devido a gamma alto. Necessário checar CV e valores de gamma.

### Consequências para o modelo e para o uso clínico

A projeção mostra que Age e Cholesterol contribuem, mas não resolvem completamente o problema. Portanto, confiar apenas nessa visualização para decisões clínicas seria arriscado.

O modelo deve ser avaliado por métricas além da acurácia: F1, recall (sensibilidade) e especificidade, pois em contexto médico recall alto pode ser prioritário.

---
## Conclusão

O classificador SVM, especialmente com kernel RBF, mostrou capacidade de separar regiões de maior risco cardíaco a partir das variáveis analisadas. O pré-processamento adequado das variáveis categóricas e a padronização das numéricas foram fundamentais para o bom desempenho do modelo.

As visualizações reforçam que kernels diferentes produzem fronteiras muito distintas, deixando claro que a escolha do kernel deve ser baseada tanto na interpretação quanto no desempenho estatístico.

O modelo otimizado via GridSearchCV oferece uma solução sólida para previsão de risco cardíaco, podendo ser usado como base para aplicações mais avançadas em saúde preditiva.