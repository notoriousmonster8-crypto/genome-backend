from models.model import model

def risk_agent_node(state):
    features = state["features"]

    risks = model.predict(features)

    return {**state, "risks": risks}