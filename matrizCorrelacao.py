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
