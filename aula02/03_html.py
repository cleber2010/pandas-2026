# %%
from operator import le
from urllib import response
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

dfs = pd.read_html(response.text)
dfs
# %%
len(dfs)
# %%
type(dfs)
# %%
df_uf = dfs[1]
df_uf
# %%
df_uf.to_csv("unidades_federativas.csv", index=False)
# %%
