# %%
import pandas as pd

df =pd.read_csv("../data/clientes.csv")
df


# %%
df.to_csv("clientes.csv", index=False)


# %%
df.to_parquet("clientes.parquet", index=False)


# %%
de_2 = pd.read_parquet("clientes.parquet")
de_2



# %%
df.to_excel("clientes.xlsx", index=False)

# %%
df_2 = pd.read_excel("clientes.xlsx")
df_2
# %%
