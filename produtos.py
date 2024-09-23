from fastapi import APIRouter, HTTPException
from typing import List
from models import Produto
from services import ProdutoService

router = APIRouter()
service = ProdutoService()

@router.post("/produtos/", response_model=Produto)
def create_produto(produto: Produto):
    return service.create_produto(produto)

@router.get("/produtos/", response_model=List[Produto])
def read_produtos(nome: str = None, categoria: str = None):
    return service.read_produtos(nome, categoria)

@router.put("/produtos/{produto_id}", response_model=Produto)
def update_produto(produto_id: int, produto: Produto):
    updated_produto = service.update_produto(produto_id, produto)
    if not updated_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_produto

@router.delete("/produtos/{produto_id}")
def delete_produto(produto_id: int):
    if not service.delete_produto(produto_id):
        raise HTTPException(status_code=400, detail="Produto não pode ser excluído")
    return {"message": "Produto excluído com sucesso"}

@router.patch("/produtos/{produto_id}/estoque/")
def update_estoque(produto_id: int, quantidade: int):
    updated_produto = service.update_estoque(produto_id, quantidade)
    if not updated_produto:
        raise HTTPException(status_code=400, detail="Atualização de estoque inválida")
    return updated_produto
