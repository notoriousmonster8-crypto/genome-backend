def detect_input_type(content: str, filename: str = ""):
    if filename.endswith(".vcf"):
        return "vcf"

    if "rs" in content[:100]:
        return "snp"

    if filename.endswith(".pdf"):
        return "pdf"

    return "genome"