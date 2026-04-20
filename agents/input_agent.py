from utils.parser import parse_genome

def input_agent_node(state):
    try:
        genome_text = state.get("genome", "")
        family_text = state.get("family_history", "")

        # 🔹 Extract features (optional, for future ML use)
        features = parse_genome(genome_text)

        return {
            **state,
            "genome": genome_text,
            "family_history": family_text,
            "features": features
        }

    except Exception as e:
        print("INPUT AGENT ERROR:", e)

        return {
            **state,
            "features": {}
        }