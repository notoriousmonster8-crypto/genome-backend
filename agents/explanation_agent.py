from services.chat_service import generate_text
def explanation_agent_node(state):
    risks = state.get("risks", {})
    context = state.get("context", "")
    citations = state.get("citations", [])

    citation_text = "\n".join([
        f"{c['title']} ({c['year']})"
        for c in citations
    ])

    prompt = f"""
    Explain genome-based disease risks.

    Risks:
    {risks}

    Context:
    {context}

    Scientific References:
    {citation_text}

    Keep it simple but credible.
    """

    explanation = generate_text(prompt)

    return {**state, "explanation": explanation, "citations": citations}