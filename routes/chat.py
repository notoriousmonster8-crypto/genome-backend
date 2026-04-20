from fastapi import APIRouter
from services.gemini_service import generate_text

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    question = data.get("question", "")
    context = data.get("context")

    # 🔥 NEVER BLOCK ON CONTEXT
    if not context:
        context_text = "No prior genome analysis available."
    else:
        context_text = str(context)

    prompt = f"""
    You are a genomic health assistant.

    Context:
    {context_text}

    Question:
    {question}

    Answer clearly.
    """

    answer = generate_text(prompt)

    return {"answer": answer}