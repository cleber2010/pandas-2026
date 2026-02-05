# %%
import pandas as pd
import numpy as np


df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
# Adiciona 100 pontos a cada cliente
#nao precisa usar o for para isso

df["qtdePontosNovos"] = df["qtdePontos"] + 100
df.head()
# %%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head(20)
# %%
df["flEmail"] * df["flTwitch"]


# %%
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flBlueSky"] + df["flInstagram"] + df["flYouTube"]
df.head(10)

# %%
df["qtdePontos"].describe()

# %%

df["qtdePontosLog"] = np.log(df["qtdePontos"] + 1)
df["qtdePontosLog"].describe()

# %%
import matplotlib.pyplot as plt
plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()
# %%
plt.hist(df["qtdePontosLog"])
plt.grid(True)
plt.show()
# %%
