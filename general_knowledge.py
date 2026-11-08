## Pandas Dataframes é uma forma de organização de dados dentro do python
import numpy as np

from repositorio import X,y

print("Conhecimento Geral da Base")
print("--------------------------")
print("O que deseja ver: ")
print("0. Sair do programa")
print("1. Verificar os dados de uma linha")
numero = int(input("Qual número voce quer?"))

if numero == 0:
    exit()
elif numero == 1:
    linha = int(input("Digite qual linha vc quer: "))
    print(X.iloc[linha])


# Mostrando os dados da primeira linha da tabela
print(X.iloc[0])
print(y.iloc[0])

# Verificar dimensões da base
print("Dimensões da base:")
print(X.shape)

# Verificar tipos de dados
print("\nTipos de dados:")
print(X.dtypes)