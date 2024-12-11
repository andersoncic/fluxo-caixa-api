from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.date.today)
    type = Column(String, index=True)  # "credit" ou "debit"
    amount = Column(Float, nullable=False)

# Configuração do Banco
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
