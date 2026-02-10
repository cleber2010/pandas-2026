# %%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# %%
clientes = pd.read_sql_table(table_name="clientes", con=engine)
# %%
clientes.head()
# %%
query = "SELECT * FROM clientes WHERE qtdePontos > 30"
clientes_30 = pd.read_sql_query(sql=query, con=engine)
# %%
clientes_30.head()
# %%
