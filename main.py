## Pandas Dataframes é uma forma de organização de dados dentro do python


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

  
# metadata 
# print(breast_cancer_wisconsin_diagnostic.metadata) 
  
# variable information 
# print(breast_cancer_wisconsin_diagnostic.variables) 
