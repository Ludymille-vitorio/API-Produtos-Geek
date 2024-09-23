from typing import List, Optional
from sqlmodel import Session, select
from models import Produto
from database import engine

class ProdutoService:
    def __init__(self):
        self.session = Session(engine)

    def create_produto(self, produto: Produto) -> Produto:
        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto

    def read_produtos(self, nome: Optional[str] = None, categoria: Optional[str] = None) -> List[Produto]:
        query = select(Produto)
        if nome:
            query = query.where(Produto.nome.contains(nome))
        if categoria:
            query = query.where(Produto.categoria == categoria)
        return self.session.exec(query).all()

    def update_produto(self, produto_id: int, produto: Produto) -> Produto:
        db_produto = self.session.get(Produto, produto_id)
        if not db_produto:
            return None
        db_produto.nome = produto.nome
        db_produto.descricao = produto.descricao
        db_produto.preco = produto.preco
        db_produto.quantidade_estoque = produto.quantidade_estoque
        db_produto.categoria = produto.categoria
        db_produto.franquia = produto.franquia
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def delete_produto(self, produto_id: int) -> bool:
        db_produto = self.session.get(Produto, produto_id)
        if db_produto and db_produto.quantidade_estoque == 0:
            self.session.delete(db_produto)
            self.session.commit()
            return True
        return False

    def update_estoque(self, produto_id: int, quantidade: int) -> Produto:
        db_produto = self.session.get(Produto, produto_id)
        if not db_produto or db_produto.quantidade_estoque + quantidade < 0:
            return None
        db_produto.quantidade_estoque += quantidade
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto
