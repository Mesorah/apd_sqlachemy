from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime)

engine = create_engine('sqlite:///example.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Criar um novo usuário
user = User(nome='John Doe', email='john@example.com')
session.add(user)
session.commit()

# Consultar usuários
users = session.query(User).all()

# Atualizar um usuário
user = session.query(User).filter_by(nome='John Doe').first()
user.email = 'john.doe@example.com'
session.commit()

# Excluir um usuário
user = session.query(User).filter_by(nome='John Doe').first()
session.delete(user)
session.commit()
