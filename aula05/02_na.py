# %%
import pandas as pd

clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
clientes.isna().sum()

# %%
#criterio é que todas as colunas sejam NA
clientes.dropna(how='all')

clientes.isna().sum()

# %%
df = pd.DataFrame({
    "nome": ["Alice", "Bob", "João", "Maria", "Carlos", "Ana", "Pedro", "Luiza"],
    "idade": [28, 35, None, 42, None, 30, 25, None],
    "salario": [3000, 4500, 3003, None, 4000, 3500, None, 5000]
})
dfSemNa = df.dropna(how='all', subset=['idade'])
dfSemNa
# %%
dfSemNa['salario'] = dfSemNa['salario'].fillna(0)
dfSemNaSal = dfSemNa
dfSemNaSal
# %%
