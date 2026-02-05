# %%
import pandas as pd
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()


max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

# %%
# Ordenando os dados
# sort values retorna um novo DataFrame ordenado
(clientes.sort_values(by="qtdePontos", ascending=False)
            .head())
# Pegando só o id
(clientes.sort_values(by="qtdePontos", ascending=False)
        .head()["idCliente"] )

# %%
