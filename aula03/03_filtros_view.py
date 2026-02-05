# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
#filtros não são copias, são visões (views)