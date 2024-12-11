from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction
from app.schemas import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(type=transaction.type, amount=transaction.amount)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
