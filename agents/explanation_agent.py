from services.gemini_service import generate_text

def explanation_agent_node(state):
    try:
        risks = state.get("risks", {})
        context = state.get("context", "")
        citations = state.get("citations", "")

        prompt = f"""
        You are a genomic health assistant.

        Risks:
        {risks}

        Context (from research):
        {context}

        External Research:
        {citations}

        Instructions:
        - Explain each disease clearly
        - Use exact risk values
        - Use context if useful
        - Keep it simple

        Output:
        Disease → risk → explanation
        """

        explanation = generate_text(prompt)

        if not explanation:
            explanation = "Explanation unavailable."

        return {
            "risks": risks,
            "explanation": explanation,
            "citations": citations
        }

    except Exception as e:
        print("EXPLANATION ERROR:", e)

        return {
            "risks": state.get("risks", {}),
            "explanation": "Explanation failed"
        }