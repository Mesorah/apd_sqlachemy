from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///test.db")

Base = declarative_base()

class Test(Base):
    __tablename__ = 'testes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


novo_usuario = Test(nome='ga', sobrenome='ro')

session.add(novo_usuario)

session.commit()

session.close()