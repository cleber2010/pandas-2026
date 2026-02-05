# %%
import pandas as pd

# %%
df = pd.DataFrame( {
    "nome": ["Ana", "Bruno", "Carlos", "Ana", "Daniel", "Bruno", "Eva"],
    "sobrenome": ["Silva", "Souza", "Oliveira", "Silva", "Pereira", "Souza", "Costa"],
    "salario": [3000, 4020, 5000, 3030, 6000, 40020, 7000]
}
)
# %%
# %%
dfOrdenado = df.sort_values("salario", ascending=False)

dfSemDuplicatas = dfOrdenado.drop_duplicates(subset=['nome', 'sobrenome'])
dfSemDuplicatas
# %%
