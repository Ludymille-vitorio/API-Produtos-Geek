from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./produtos.db" 
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
