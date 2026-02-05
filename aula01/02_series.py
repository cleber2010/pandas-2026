# %%

idades = [15, 22, 35, 45, 52, 67, 80]
media = sum(idades) / len(idades)
print("Média das idades:", media)

# %%
import pandas as pd

series_idades = pd.Series(idades)
print("Série de idades:")
print(series_idades)

# %%

media_idades = series_idades.mean()
print("Média das idades (pandas):", media_idades)   

var_idades = series_idades.var()
print("Variância das idades (pandas):", var_idades)

summary_idades = series_idades.describe()
print("Resumo estatístico das idades (pandas):")
print(summary_idades)
