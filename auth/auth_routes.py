from fastapi import APIRouter
from auth.jwt_handler import create_token

router = APIRouter()

@router.post("/login")
def login(data: dict):
    username = data.get("username")
    token = create_token({"user": username})
    return {"token": token}