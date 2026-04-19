from services.gemini_service import generate_text

def chat_response(question, context=""):
    prompt = f"""
    Answer the user question based on genomic knowledge.

    Context:
    {context}

    Question:
    {question}
    """

    return generate_text(prompt)