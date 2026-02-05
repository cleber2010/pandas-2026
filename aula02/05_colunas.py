# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
df = df.rename(columns={"QtdePontos": "qtPontos", 
                        "DescSistemaOrigem": "sistemaOrigem"} )
# %%
df.rename(columns={"QtdePontos": "qtPontos", 
                        "DescSistemaOrigem": "SistemaOrigem"}, inplace=True)

# %%
df.columns

# %%
df[["IdCliente", "qtPontos"]]
# %%
df[['idCliente']]

# %%
df[['idCliente', 'qtPontos']].head(5)
# %%
df[['idCliente', 'idTransacao', 'qtPontos']].head(5)

# %%
colunas = df.columns.tolist()
colunas
colunas.sort()
colunas
# %%
df = df[colunas]
df.head()
