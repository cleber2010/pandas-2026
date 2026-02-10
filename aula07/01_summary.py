# %% 
import pandas as pd

idades = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

idades_series = pd.Series(idades)
idades_series
# %%
idades_series.mean()# %%
idades_series.median()# %%
idades_series.mode()# %%        
idades_series.std()# %%
idades_series.var()# %% 
idades_series.min()# %%
idades_series.max()# %%
idades_series.describe()# %%
# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
# %%
redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flInstagram", "flBlueSky"]
# %%
clientes[redes_sociais].mean()
clientes[redes_sociais].sum()
# %%
filtro = clientes.dtypes == "object"
# %%
filtro
# %%
num_cols = clientes.dtypes[~filtro].index.to_list()
num_cols
clientes[num_cols]
# %%
clientes[num_cols].mean()
# %%
clientes[num_cols].describe()