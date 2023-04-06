import psycopg2
import pandas as pd

# Lendo os dados da planilha database.xlsx
df = pd.read_excel('C:/Users/joze.junior.ext/Documents/teste.xlsx', sheet_name='Plan1')

# Conexao com o Postgre
conn = psycopg2.connect(
    host="localhost",
    database="teste",
    user="postgres",
    password="123"
)

# Inserindo os dados no banco
cur = conn.cursor()
cols = ",".join([str(i) for i in df.columns.tolist()])
for index, row in df.iterrows():
    values = ",".join(["'{}'".format(str(i)) for i in row.tolist()])
    sql = f'INSERT INTO "DATABASE_PRODUCAO_VF"."TESTE" ({cols}) VALUES ({values}) ON CONFLICT DO NOTHING'
    cur.execute(sql)


conn.commit()
cur.close()
conn.close()
