# %%
import pandas as pd
idades = [15, 22, 35, 45, 52, 67, 80]

nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 
          'Eduardo', 'Fernanda', 'Gustavo']
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%
df = pd.DataFrame()
df["Idades"] = series_idades
df["Nomes"] = series_nomes
print("DataFrame de idades e nomes:")
print(df)
# %%
df['Nomes']
# %%
df['Idades']
# %%
df.iloc[0]['Nomes']
# %%
df.loc[0]
# %%
df.iloc[-1]['Idades']

# %%
#pra que serve o iloc e o loc
#iloc é usado para acessar linhas e colunas por posição (índice inteiro)
#loc é usado para acessar linhas e colunas por rótulo (nome)