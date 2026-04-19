from utils.parser import parse_genome

def input_agent_node(state):
    genome_text = state["input"]

    features = parse_genome(genome_text)

    return {**state, "features": features}