## Pandas Dataframes é uma forma de organização de dados dentro do python
import numpy as np
# Importa os dados do repositório oficial da UC - Irvine (Universidade da California - Irvine)
from ucimlrepo import fetch_ucirepo 
# Busca os dados do repositório sobre Cancer de Mama
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17) 
  
# Dados propriamente ditos (na forma de "pandas dataframes") 

# Features: são as características ou entradas
X = breast_cancer_wisconsin_diagnostic.data.features 

# Targets: são os diagnosticos ou saídas
y = breast_cancer_wisconsin_diagnostic.data.targets 



# Mostrando os dados da primeira linha da tabela
#print(X.iloc[0])

# Verificar dimensões da base
print("Dimensões da base:")
print(X.shape)

# Verificar tipos de dados
print("\nTipos de dados:")
print(X.dtypes)


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


# metadata 
# print(breast_cancer_wisconsin_diagnostic.metadata) 
  
# variable information 
# print(breast_cancer_wisconsin_diagnostic.variables) 
