from langgraph.graph import StateGraph

# 🔹 Existing logic
from services.variant_parser import extract_rsids
from services.variant_engine import compute_variant_risk
from services.family_parser import extract_family_history
from services.risk_fusion import combine_risks

# 🔹 Agents
from agents.explanation_agent import explanation_agent_node
from agents.retrieval_agent import retrieval_agent_node
from agents.research_agent import research_agent_node
from agents.input_agent import input_agent_node

# ============================================
# 🧬 STATE
# ============================================
class GraphState(dict):
    pass


# ============================================
# 🧬 VARIANT AGENT
# ============================================
def variant_node(state: GraphState):
    genome = state.get("genome", "")

    rsids = extract_rsids(genome)
    genetic_risk = compute_variant_risk(rsids)

    return {**state, "genetic_risk": genetic_risk}


# ============================================
# 👨‍👩‍👧 FAMILY AGENT
# ============================================
def family_node(state: GraphState):
    family = state.get("family_history", "")

    family_data = extract_family_history(family)

    return {**state, "family_data": family_data}


# ============================================
# ⚖️ RISK AGENT
# ============================================
def risk_node(state: GraphState):
    genetic = state.get("genetic_risk", {})
    family = state.get("family_data", [])

    final_risk = combine_risks(genetic, family)

    return {**state, "risks": final_risk}


# ============================================
# 🔗 BUILD GRAPH
# ============================================
def build_graph():
    graph = StateGraph(GraphState)

    # Nodes
    graph.add_node("input", input_agent_node)
    graph.add_node("variant", variant_node)
    graph.add_node("family", family_node)
    graph.add_node("risk", risk_node)
    graph.add_node("retrieval", retrieval_agent_node)
    graph.add_node("research", research_agent_node)
    graph.add_node("explanation", explanation_agent_node)
    
    # Flow
    graph.set_entry_point("input")

    graph.add_edge("input", "variant")
    graph.add_edge("variant", "family")
    graph.add_edge("family", "risk")
    graph.add_edge("risk", "retrieval")
    graph.add_edge("retrieval", "research")
    graph.add_edge("research", "explanation")

    return graph.compile()


# 🔥 COMPILED GRAPH
graph = build_graph()