# Análise de dados de Câncer de Mama

O objetivo deste repositório é demonstrar a análise realizada em uma base de dados da Universidade da California - Irvine (UC - Irvine)
que apresenta amostra de células mamarias e suas características como tamanho, espessura e entre outras para averiguar a sua relação
com a existência de câncer de mama.

Os dados escolhidos estão disponeis em python.

A base escolhida tem um total de 569 amostras/linhas que são exames feitos em células mamarias para averiguar certas características 
das células. A base contem 30 características/colunas que são as entradas da nossa rede neural. 

As características são: 

Raio, Textura, Perimetro, Área, Suavidade, Compacidade, Pontos Côncavos, Simetria, Dimensão Factral

Essas características são divididas em 3 tipos:

### Média
### Erro Padrão
### Valor mais elevado

totalizando 30 entradas.

As saídas são o que foi diagnosticado:

### B ou Benigno
### M ou Maligno

## Importação dos dados

Para pegar os dados do repositorio precisamos fazer uma instalação da base de dados. Para isso podemos 
escrever no command prompt:
```bash
pip install ucimlrepo
```

e depois usamos o seguinte código:

```py
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17) 
  
# data (as pandas dataframes) 
X = breast_cancer_wisconsin_diagnostic.data.features 
y = breast_cancer_wisconsin_diagnostic.data.targets 
  
# metadata 
print(breast_cancer_wisconsin_diagnostic.metadata) 
  
# variable information 
print(breast_cancer_wisconsin_diagnostic.variables) 
```

onde a variável X representa os dados das características (entradas) e a variável y representa os diagnósticos (saídas)

Esse código do repositório foi colocado em um arquivo com o nome de (repositorio.py). A partir dele, foram importados os
dados para os outros arquivos usando o código:

```py
from repositorio import X,y
```

## Qualidade e integridade dos dados

A primeira verificação foi analisar se algum valor ausente na tabela. O arquivo (integridadeDados.py) contém os código que foram usados
para determinar esse tôpico:

```py
## Qualidade e Integridade dos dados

#1 Verificar valores ausentes
print("\nValores ausentes:")
print(X.isnull().sum())

#2 Verificar registros duplicados
print("\nRegistros duplicados:")
print(X.duplicated().sum())

# Estatísticas descritivas
print("\nEstatísticas:")
print(X.describe().T)

#3 Verificar valores negativos nas variáveis numéricas
colunas_numericas = X.select_dtypes(include=np.number).columns

print("\nVALORES NEGATIVOS:")

for coluna in colunas_numericas:
    quantidade = (X[coluna] < 0).sum()

    if quantidade > 0:
        print(f"{coluna}: {quantidade} valores negativos")
```

## Matriz de Correlação

A matriz de correlação tem como objetivo analisar se existe algum relacionamento entre as colunas para
que seja possível haver a exclusão de alguma delas. 

Isso pode ser feito da seguinte maneira

Primeiramente devesse instalar a biblioteca seaborn através de:

```bash
python -m pip install seaborn
```

```py
# Importações
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importa a base da UCI
from ucimlrepo import fetch_ucirepo

# Carrega a base
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17)

# Features
X = breast_cancer_wisconsin_diagnostic.data.features

# Target
y = breast_cancer_wisconsin_diagnostic.data.targets

# ==========================================================
# MATRIZ DE CORRELAÇÃO
# ==========================================================

# Calcula a correlação de Pearson
corr = X.corr()

# Configuração da figura
plt.figure(figsize=(18, 15))

# Plota o mapa de calor
sns.heatmap(
    corr,
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink":0.8}
)

plt.title("Matriz de Correlação - Breast Cancer Wisconsin", fontsize=18)
plt.tight_layout()
plt.show()

# ==========================================================
# ENCONTRANDO PARES MUITO CORRELACIONADOS
# ==========================================================

# Considerar apenas metade da matriz
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))

# Limite para considerar alta correlação
limite = 0.90

# Lista os pares altamente correlacionados
print(f"\nPares com correlação maior que {limite}:\n")

for coluna in upper.columns:
    for indice in upper.index:
        valor = upper.loc[indice, coluna]
        if pd.notna(valor) and abs(valor) > limite:
            print(f"{indice:30s} <-> {coluna:30s} = {valor:.3f}")
```

Para remover as colunas que não são necessárias é possível fazer isso: 

```py
# Colunas a remover
colunas_remover = [
    coluna for coluna in upper.columns
    if any(abs(upper[coluna]) > limite)
]

print("\nColunas sugeridas para remoção:")
print(colunas_remover)

# Nova base sem as colunas altamente correlacionadas
X_reduzido = X.drop(columns=colunas_remover)

print("\nDimensão original :", X.shape)
print("Dimensão reduzida :", X_reduzido.shape)
```
