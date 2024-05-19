from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:senha@localhost:3306/base_de_dados', echo=True)

with engine.connect() as con:
    with con.begin():
        sql = text('SELECT * FROM filmes')

        result = (con.execute(sql))
        print(result.fetchall())

    

