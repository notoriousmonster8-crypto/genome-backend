from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    genome = Column(String)
    result = Column(String)