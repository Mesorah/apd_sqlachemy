from sqlalchemy import create_engine

engine = create_engine('sqlite://')

print(engine)
print(engine.dialect)