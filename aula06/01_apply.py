# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
idCliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"


def get_last_id(idCliente):
    return idCliente.split("-")[-1]


# %%
get_last_id(idCliente)
# %%

df.head()

id_novo = []

for i in df["idCliente"]:
    id_novo.append(get_last_id(i))
# %%
id_novo
# %%
df["novo_id"] = id_novo
df.head()
# %%

df["idCliente"].apply(get_last_id)