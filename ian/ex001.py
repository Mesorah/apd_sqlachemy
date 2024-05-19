from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Criando o motor de banco de dados
engine = create_engine("sqlite:///exemplo.db")

# Criando a metadados
Base = declarative_base()

# Declarando a classe Usuário
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

# Criando a tabela no banco de dados
Base.metadata.create_all(engine)
    