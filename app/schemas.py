from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Schema para um lançamento (débito ou crédito)
class TransactionBase(BaseModel):
    date: date
    type: str  # "credit" ou "debit"
    amount: float

# Schema para criar um lançamento (entrada do usuário)
class TransactionCreate(TransactionBase):
    pass

# Schema para retorno de um lançamento (com ID)
class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True  # Habilita compatibilidade com ORM (ex.: SQLAlchemy)

# Schema para o saldo consolidado diário
class DailySummary(BaseModel):
    date: date
    total_credit: float
    total_debit: float
    balance: float
