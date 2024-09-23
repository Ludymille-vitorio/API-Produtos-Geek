from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade_estoque: int
    categoria: str
    franquia: str

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        orm_mode = True