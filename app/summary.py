from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction
from sqlalchemy import func

router = APIRouter(prefix="/summary", tags=["summary"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_daily_summary(db: Session = Depends(get_db)):
    credits = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "credit").scalar() or 0
    debits = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "debit").scalar() or 0
    balance = credits - debits
    return {"credits": credits, "debits": debits, "balance": balance}
