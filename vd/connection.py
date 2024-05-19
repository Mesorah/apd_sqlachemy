from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from sqlalchemy import Column, String, Integer

# Configurações
engine = create_engine('mysql+pymysql://root:senha@localhost:3306/base_de_dados')

mapper_registy = registry()
Base = mapper_registy.generate_base()
Session = sessionmaker(bind=engine)
Session = Session()

class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme (titulo={self.titulo}, ano={self.ano})'