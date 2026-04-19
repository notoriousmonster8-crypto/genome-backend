def parse_snp(text: str):
    data = []

    for line in text.split("\n"):
        if line.startswith("#") or not line.strip():
            continue

        parts = line.split()
        if len(parts) >= 4:
            data.append({
                "rsid": parts[0],
                "genotype": parts[3]
            })

    return data