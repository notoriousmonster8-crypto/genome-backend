from services.research_service import fetch_research

def research_agent_node(state):
    risks = state.get("risks", {})

    query = f"genetic disease risk {list(risks.keys())}"

    papers = fetch_research(query)

    return {**state, "citations": papers}