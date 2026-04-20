from fastapi import APIRouter
from services.gemini_service import generate_text
from agents.explanation_agent import explanation_agent_node

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    genome = data.get("genome", "")

    # 🔥 Step 1: Ask Gemini for risks (structured)
    prompt = f"""
    Analyze the following genome data and return ONLY JSON.

    Format:
    {{
      "risks": {{
        "Disease1": 0-1,
        "Disease2": 0-1
      }}
    }}

    Genome:
    {genome}
    """

    raw = generate_text(prompt)

    # 🔥 Step 2: Convert to Python dict safely
    try:
        import json
        parsed = json.loads(raw)
        risks = parsed.get("risks", {})
    except:
        risks = {"General Risk": 0.5}

    # 🔥 Step 3: Use YOUR explanation agent
    state = {"risks": risks}
    state = explanation_agent_node(state)

    return state