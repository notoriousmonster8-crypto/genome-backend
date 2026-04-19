def parse_vcf(text: str):
    variants = []

    for line in text.split("\n"):
        if line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) > 4:
            variants.append({
                "chrom": parts[0],
                "pos": parts[1],
                "ref": parts[3],
                "alt": parts[4]
            })

    return variants