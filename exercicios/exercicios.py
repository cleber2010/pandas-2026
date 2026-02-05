# %%
import pandas as pd

# selecione a primeira transação de cada cliente em cada dia

transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
# %%
# Manter apenas a primeira transação por cliente em cada dia
transacoes = transacoes.sort_values("DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes.drop_duplicates(subset=['IdCliente', 'data'], keep='first')

# %%
first = (transacoes.sort_values("DtCriacao")
         .drop_duplicates(subset=['IdCliente', 'data'], keep='first'))

last = (transacoes.sort_values("DtCriacao")
         .drop_duplicates(subset=['IdCliente', 'data'], keep='last'))

pd.concat([last, first])
