from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:senha@localhost:3306/base_de_dados')
conn = engine.connect()

query = text('SELECT * FROM filmes')
result = conn.execute(query)

# Processar o resultado
for row in result:
    print(row)
    print(row.titulo)

# Fechar a conexão
conn.close()