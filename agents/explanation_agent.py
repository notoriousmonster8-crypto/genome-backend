from services.gemini_service import generate_text

def explanation_agent_node(state):
    prompt = f"""
    You are a genomic health assistant.

    Risks:
    {state['risks']}

    Explain:
    - What these risks mean
    - Genetic influence
    - Keep it simple
    """

    explanation = generate_text(prompt)

    return {**state, "explanation": explanation}