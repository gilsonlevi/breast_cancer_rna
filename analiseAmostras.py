from repositorio import X,y


import pandas as pd
import matplotlib.pyplot as plt

# Identifica a coluna que contém os diagnósticos
coluna_alvo = y.columns[0]

# Conta a quantidade de amostras por classificação
quantidade = y[coluna_alvo].value_counts()

# Calcula o percentual de cada classificação
percentual = y[coluna_alvo].value_counts(normalize=True) * 100

# Organiza os resultados em uma tabela
distribuicao = pd.DataFrame({
    "Quantidade": quantidade,
    "Percentual (%)": percentual
})

# Renomeia as classificações
distribuicao = distribuicao.rename(
    index={"B": "Benigno", "M": "Maligno"}
)

# Exibe os resultados
print("DISTRIBUIÇÃO DAS CLASSIFICAÇÕES")
print(distribuicao.round(2))

print("\nTotal de amostras:", len(y))


# Gráfico de barras
plt.figure(figsize=(8, 5))

quantidade.rename(
    index={"B": "Benigno", "M": "Maligno"}
).plot(kind="bar")

plt.title("Quantidade de amostras por diagnóstico")
plt.xlabel("Diagnóstico")
plt.ylabel("Quantidade de amostras")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


# Gráfico de distribuição percentual
plt.figure(figsize=(7, 7))

plt.pie(
    percentual,
    labels=["Benigno" if classe == "B" else "Maligno"
            for classe in percentual.index],
    autopct="%1.2f%%",
    startangle=90
)

plt.title("Distribuição percentual dos diagnósticos")
plt.tight_layout()
plt.show()
