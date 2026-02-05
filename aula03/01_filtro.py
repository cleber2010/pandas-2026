# %%
import pandas as pd



# %%
pontos = [10, 50, 100, 500, 1000,1,500, 2000,50,400]

valor_50_mais = []
for i in pontos:
    if i > 50:
        valor_50_mais.append(i)

valor_50_mais
# %%
brinquedo = pd.DataFrame({
    "nome": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "preco": [20, 60, 150, 500, 1200, 15, 700, 2500, 80, 400]
})
brinquedo
# %%
filtro = brinquedo["preco"] >= 60
filtro
brinquedo[filtro]

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%
filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
filtro
df[filtro]

# %%
filtro = (df["QtdePontos"]  == 1) | (df["QtdePontos"] == 100)
df[filtro]


# %%
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <=50) & (df["DtCriacao"] >= '2025-01-01')
df[filtro]

# %%
