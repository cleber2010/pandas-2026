# %%
import pandas as pd
idades = [15, 22, 35, 45, 52, 67, 80]


series_idades = pd.Series(idades)
print("Série de idades:")
print(series_idades)

# %%
print("Acessando elementos da série por índice:")
print("Idade no índice 0:", series_idades[0])

series_idades[0]

series_idades.iloc[0]

# %%
print("Idade no último índice:", series_idades.iloc[-1])    
series_idades.iloc[:3]

series_idades.iloc[::-1]
# %%

idades = [15, 22, 35, 45, 52, 67, 80]

indexs = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo']

series_idades = pd.Series(idades, index=indexs)
print("Série de idades com índices personalizados:")
print(series_idades)
# %%
series_idades['Ana']
# %%
series_idades.loc['Ana']