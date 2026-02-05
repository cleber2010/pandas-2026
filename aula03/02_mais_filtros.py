# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df.head()

# %%
df["IdProduto"] 
df.dtypes
df["IdProduto"] = pd.to_numeric(df["IdProduto"], errors="coerce")
df.dtypes

# %%
filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 100)
df[filtro]
# %%

filtro = df["IdProduto"].isin([5, 11])
df[filtro]

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head(100)

# %%
filtro = clientes["DtCriacao"].notnull()
filtro
clientes[filtro]
# %%
