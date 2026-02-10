# %%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers, timeout=30)
resp.raise_for_status()

df = pd.read_html(resp.text, decimal=",", thousands=".")[1]
df.head()
uf = df
uf.head()


# %%
uf.dtypes
# %%
def converte_numero(numero):
    numero = float(numero.replace(" ", "").replace(",", ".").replace("\xa0", ""))
    return numero
# %%


# %%
uf.head()

# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(converte_numero)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(converte_numero)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(converte_numero)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(converte_numero)
# %%

uf["Expectativa de vida (2016)"]

def converte_expectativa_float(numero):
    numero = float(numero.replace(",", ".").replace(" anos", ""))
    return numero
# %%
uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(converte_expectativa_float)
# %%
uf.dtypes
# %%
uf.head()