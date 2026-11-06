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