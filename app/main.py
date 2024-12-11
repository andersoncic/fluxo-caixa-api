from fastapi import FastAPI
from app.routers import transactions, summary

app = FastAPI()

# Rotas
app.include_router(transactions.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Sistema de Fluxo de Caixa"}
