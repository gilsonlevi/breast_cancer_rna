## Pandas Dataframes é uma forma de organização de dados dentro do python
import numpy as np

from repositorio import X,y

# Mostrando os dados da primeira linha da tabela
print(X.iloc[0])
print(y.iloc[0])

# Verificar dimensões da base
print("Dimensões da base:")
print(X.shape)

# Verificar tipos de dados
print("\nTipos de dados:")
print(X.dtypes)