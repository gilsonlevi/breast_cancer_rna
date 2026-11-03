# Análise de dados de Câncer de Mama

O objetivo deste repositório é demonstrar a análise realizada em uma base de dados da Universidade da California - Irvine (UC - Irvine)
que apresenta amostra de células mamarias e suas características como tamanho, espessura e entre outras para averiguar a sua relação
com a existência de câncer de mama.

Os dados escolhidos estão disponeis em python.

A base escolhida tem um total de 569 amostras/linhas que são exames feitos em células mamarias para averiguar certas características 
das células. A base contem 30 características/colunas que são as entradas da nossa rede neural. 

As características são: 

### Raio
### Textura
### Perimetro
### Área
### Suavidade
### Compacidade
### Pontos Côncavos
### Simetria
### Dimensão Factral

Essas características são divididas em 3 tipos:

### Média
### Erro Padrão
### Valor mais elevado

totalizando 30 entradas.

As saídas são o que foi diagnosticado:

### B ou Benigno
### M ou Maligno

## Importação dos dados

Para pegar os dados do repositorio em python usamos:
```py
pip install ucimlrepo
```
## Qualidade e integridade dos dados

A primeira verificação foi analisar se algum valor ausente na tabela 

