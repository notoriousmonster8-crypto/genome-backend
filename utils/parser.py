def parse_genome(text: str):
    return {
        "A_count": text.count("A"),
        "T_count": text.count("T"),
        "G_count": text.count("G"),
        "C_count": text.count("C"),
        "length": len(text),
    }