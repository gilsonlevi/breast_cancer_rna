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

Para pegar os dados do repositorio em python no command prompt:
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


