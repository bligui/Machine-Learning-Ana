# Projeto de Predição de Doenças Cardiovasculares

Este projeto tem como objetivo aplicar técnicas de **Machine Learning** para prever a presença de doenças cardiovasculares a partir de variáveis clínicas. O desenvolvimento segue etapas bem definidas, cada uma com critérios e pontuação, conforme especificado na rubrica do projeto.

---

## Etapas do Projeto

### 1. Exploração dos Dados

#### Descrição do Conjunto de Dados
O dataset utilizado foi obtido no [Kaggle](https://www.kaggle.com/fedesoriano/heart-failure-prediction) e reúne informações provenientes de cinco bases distintas do **UCI Machine Learning Repository**.  
Após a remoção de duplicatas, o conjunto final contém **918 observações** e **12 variáveis**, sendo **11 atributos preditores** e **1 variável alvo** (*HeartDisease*).

#### Variáveis
- **Age**: idade do paciente (anos)  
- **Sex**: sexo (M = Masculino, F = Feminino)  
- **ChestPainType**: tipo de dor no peito  
  - TA: Angina Típica  
  - ATA: Angina Atípica  
  - NAP: Dor Não-Anginosa  
  - ASY: Assintomático  
- **RestingBP**: pressão arterial em repouso (mm Hg)  
- **Cholesterol**: colesterol sérico (mg/dl)  
- **FastingBS**: glicemia em jejum (>120 mg/dl = 1, caso contrário = 0)  
- **RestingECG**: resultados do eletrocardiograma em repouso  
- **MaxHR**: frequência cardíaca máxima atingida  
- **ExerciseAngina**: angina induzida por exercício (Y/N)  
- **Oldpeak**: depressão do segmento ST  
- **ST_Slope**: inclinação do segmento ST (Up, Flat, Down)  
- **HeartDisease**: variável alvo (0 = normal, 1 = presença de doença)  

#### Estatísticas Descritivas e Visualizações
- **Idade**: varia entre ~28 e 77 anos, com média em torno de 53 anos.
=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/idadedesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/idadedesc.py"
    ```

- **Sexo**: há predominância do sexo masculino no conjunto.
=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/generodesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/generodesc.py"
    ```
- **Colesterol**: grande variabilidade, com valores fora da faixa esperada em alguns casos.
=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/coldesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/coldesc.py"
    ```
- **Pressão Arterial em Repouso**: média próxima de 130 mm Hg, condizente com casos de hipertensão.

=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/pressaodesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/pressaodesc.py"
    ```
- **MaxHR**: varia entre 60 e 202, indicando ampla faixa de condicionamento físico.

=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/maxhrdesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/maxhrdesc.py"
    ```
- **Distribuição da Variável Alvo (HeartDisease)**: aproximadamente **55% dos pacientes apresentam diagnóstico positivo**, o que gera uma base relativamente balanceada para treinamento.
=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/heartdesc.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/heartdesc.py"
    ```

#### Conclusões
- **Distribuição da idade** mostra maior concentração entre 45 e 60 anos.  
- **Proporção por sexo** evidencia predominância masculina.  
- **Boxplots de colesterol e pressão arterial** revelam a presença de outliers que devem ser tratados no pré-processamento.
- **Relação entre ChestPainType e HeartDisease** indica que pacientes assintomáticos (ASY) têm maior probabilidade de diagnóstico positivo.
=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/roteiro1/est/relacao.py"
    ``` 

=== "Code"

    ```python
    --8<-- "docs/roteiro1/est/relacao.py"
    ```

---

### 2. Pré-processamento
(Em desenvolvimento)

---

### 3. Divisão dos Dados
(Em desenvolvimento)

---

### 4. Treinamento do Modelo
(Em desenvolvimento)

---

### 5. Avaliação do Modelo
(Em desenvolvimento)

---

### 6. Relatório Final
(Em desenvolvimento)
