# %%
import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()


# %%
transacoes.groupby(by=["IdCliente"]).count()
# %%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

# groupby retorna um objeto do tipo DataFrameGroupBy, que é um objeto intermediário que armazena as informações sobre como os dados estão agrupados. Para obter os resultados agregados, é necessário aplicar uma função de agregação, como count(), mean(), sum(), etc., ao objeto resultante do groupby.
# em resumo, o groupby é usado para agrupar os dados com base em uma ou mais colunas, e a função de agregação é usada para calcular estatísticas ou realizar operações nos grupos resultantes.

# %%
#qtde transações por cliente
#total de pontos por cliente
# pontos médios por cliente

summary = transacoes.groupby(by=["IdCliente"], as_index=False).agg({"IdTransacao": ["count"], "QtdePontos": ["sum", "mean"]})
summary

# %%
summary["QtdePontos"]

# %%
summary.columns = ["IdCliente", "QtdeTransacoes", "TotalPontos", "PontosMedios"]
summary
# resolvendo o problema de multiindex
# o resultado do groupby com múltiplas funções de agregação gera um DataFrame com multiindex nas colunas, onde cada coluna é representada por uma tupla (nome da coluna original, nome da função de agregação). Para resolver esse problema e obter um DataFrame com colunas simples, podemos renomear as colunas após a agregação.

# %%
