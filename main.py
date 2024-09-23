from fastapi import FastAPI
from routers import produtos
from database import init_db

app = FastAPI()

init_db()

app.include_router(produtos.router)
