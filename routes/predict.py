from fastapi import APIRouter
from services.variant_parser import extract_rsids
from services.variant_engine import compute_variant_risk
from services.family_parser import extract_family_history
from services.risk_fusion import combine_risks
from agents.explanation_agent import explanation_agent_node

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    genome = data.get("genome", "")
    family = data.get("family_history", "")

    # 🔹 Step 1: Extract variants
    rsids = extract_rsids(genome)

    # 🔹 Step 2: Genetic risk
    genetic_risk = compute_variant_risk(rsids)

    # 🔹 Step 3: Family risk
    family_data = extract_family_history(family)

    # 🔹 Step 4: Combine
    final_risk = combine_risks(genetic_risk, family_data)

    # 🔹 Step 5: Explanation (LLM)
    state = {"risks": final_risk}
    state = explanation_agent_node(state)

    return state