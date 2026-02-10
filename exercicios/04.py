# %% 
import pandas as pd
# quem teve mais transações de Streak

# %%
transacoes = pd.read_csv('../data/transacoes.csv', sep=';')
transacoes.head()
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.head()
transacoes = transacoes.rename(columns={"IdCliente": "idCliente"})  
transacoes.head()
# %%
transacoes_produto = pd.read_csv('../data/transacao_produto.csv', sep=';')
transacoes_produto.head()

produtos = pd.read_csv('../data/produtos.csv', sep=';')
produtos.head()
# %%
cliente_trasacao_produto = transacoes.merge( transacoes_produto, on="IdTransacao", how="left")[["IdTransacao", "idCliente", "IdProduto"]]
df_full = cliente_trasacao_produto.merge(produtos, on="IdProduto", how="left")
df_full.head(100)
# %%
df_full = df_full[df_full["DescDescricaoProduto"] == "Presença Streak"]

df_full.head()