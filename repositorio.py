
# Importa os dados do repositório oficial da UC - Irvine (Universidade da California - Irvine)
from ucimlrepo import fetch_ucirepo 
# Busca os dados do repositório sobre Cancer de Mama
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17) 
  
# Dados propriamente ditos (na forma de "pandas dataframes") 

# Features: são as características ou entradas
X = breast_cancer_wisconsin_diagnostic.data.features 

# Targets: são os diagnosticos ou saídas
y = breast_cancer_wisconsin_diagnostic.data.targets 