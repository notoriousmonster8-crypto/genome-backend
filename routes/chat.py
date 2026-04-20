from fastapi import APIRouter

router = APIRouter()
from services.gemini_service import generate_text

@router.post("/chat")
def chat(data: dict):
    question = data["question"]
    context = data.get("context", "")

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer clearly based on the context.
    """

    answer = generate_text(prompt)

    return {"answer": answer}