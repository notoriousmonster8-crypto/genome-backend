from langgraph.graph import StateGraph

from agents.input_agent import input_agent_node
from agents.risk_agent import risk_agent_node
from agents.retrieval_agent import retrieval_agent_node
from agents.explanation_agent import explanation_agent_node


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("input", input_agent_node)
    graph.add_node("risk", risk_agent_node)
    graph.add_node("retrieval", retrieval_agent_node)
    graph.add_node("explanation", explanation_agent_node)

    graph.set_entry_point("input")

    graph.add_edge("input", "risk")
    graph.add_edge("risk", "retrieval")
    graph.add_edge("retrieval", "explanation")

    graph.set_finish_point("explanation")

    return graph.compile()