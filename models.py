from sqlmodel import SQLModel, Field

class Produto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    preco: float = Field(gt=0) 
    quantidade_estoque: int = Field(ge=0)  
    categoria: str
    franquia: str