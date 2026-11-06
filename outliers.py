
import pandas as pd
from ucimlrepo import fetch_ucirepo

# ==================================================
# 1. CARREGAMENTO DA BASE
# ==================================================

breast_cancer = fetch_ucirepo(id=17)

X = breast_cancer.data.features

# ==================================================
# 2. IDENTIFICAÇÃO DOS OUTLIERS PELO MÉTODO IQR
# ==================================================

print("\n========== ANÁLISE DE OUTLIERS ==========\n")

total_outliers = 0

for coluna in X.columns:

    # Cálculo dos quartis
    Q1 = X[coluna].quantile(0.25)
    Q3 = X[coluna].quantile(0.75)

    # Intervalo interquartil
    IQR = Q3 - Q1

    # Limites
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    # Identificação dos outliers
    mascara = (
        (X[coluna] < limite_inferior) |
        (X[coluna] > limite_superior)
    )

    valores = X.loc[mascara, coluna]

    quantidade = len(valores)
    percentual = (quantidade / len(X)) * 100

    total_outliers += quantidade

    # Exibição dos resultados
    if quantidade > 0:
        print(f"Coluna: {coluna}")
        print(f"Quantidade: {quantidade}")
        print(f"Percentual: {percentual:.2f}%")
        print("Valores encontrados:")
        print(valores.values)
        print("-" * 50)

print("\n========== RESUMO ==========")
print(f"Total de ocorrências de outliers: {total_outliers}")
