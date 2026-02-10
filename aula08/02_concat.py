# %%
import pandas as pd

df_1 = pd.DataFrame({ 
    "cliente": ["João", "Maria", "Pedro"],
    "idade": [30, 25, 35]
})

df_2 = pd.DataFrame({
    "cliente": ["Ana", "Carlos"],
    "idade": [28, 40],
    "salario": [5000, 6000]
})

df_1


# %%
# ele espera uma lista de dataframes, por isso os colchetes
pd.concat([df_1, df_2], ignore_index=True)
# %%

df_03 = pd.DataFrame({
    "idade": [22, 27, 32,   37, 42]
    })

df_03 = df_03.sort_values(by="idade", inplace=False)
df_03
# %%
pd.concat([df_1, df_2, df_03], axis=1)