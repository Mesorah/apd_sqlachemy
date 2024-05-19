import sqlalchemy as db

# Cria o objeto MetaData
metadata = db.MetaData()

# Cria a engine de conexão com o banco de dados
engine = db.create_engine('sqlite:///database.db')

# Carrega a tabela 'comments'
t = db.Table('comments', metadata, autoload_with=engine)

# Cria a consulta SQL
sql = db.select(t.c.id, t.c.name, t.c.comment).where(t.c.name == 'test')

# Exibe a consulta SQL
print(sql)

# Conecta ao banco de dados e executa a consulta
with engine.connect() as con:
    result = con.execute(sql)

    # Fetch and print the first 2 results
    rows = result.fetchmany(2)
    for row in rows:
        print(row)

# Código comentado para criar a tabela, se necessário
# metadata.create_all(engine)

# Inspeciona o banco de dados
inspect = db.inspect(engine)

# Exibe os nomes das tabelas e as colunas da tabela 'comments'
print(inspect.get_table_names())
print(inspect.get_columns('comments'))





# t = sqlalchemy.Table(
#     'comments',
#     metadata,
#     sqlalchemy.Column('id', sqlalchemy.Integer(), nullable=False),
#     sqlalchemy.Column('name', sqlalchemy.String(), nullable=False),
#     sqlalchemy.Column('comment', sqlalchemy.String(), nullable=False),
#     sqlalchemy.Column('live', sqlalchemy.String(), nullable=False),
#     sqlalchemy.Column('created_at', sqlalchemy.DateTime(), nullable=True),
#     sqlalchemy.PrimaryKeyConstraint('id')
# )


# metadata.create_all(engine)

# inspect = sqlalchemy.inspect(engine)

# print(inspect.get_table_names())
# print(inspect.get_columns('comments'))