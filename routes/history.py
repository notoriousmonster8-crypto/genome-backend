from fastapi import APIRouter
from database.db import SessionLocal
from database.models import History

router = APIRouter()

@router.get("/history")
def get_history():
    db = SessionLocal()
    data = db.query(History).all()
    return data