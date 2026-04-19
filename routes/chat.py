from fastapi import APIRouter
from services.chat_service import chat_response

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    answer = chat_response(data["question"])
    return {"answer": answer}