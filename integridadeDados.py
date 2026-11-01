## Pandas Dataframes é uma forma de organização de dados dentro do python
import numpy as np

from repositorio import X,y


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