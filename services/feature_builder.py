def build_features(data, data_type):
    if data_type == "genome":
        return data  # already features

    if data_type == "vcf":
        return {
            "variant_count": len(data),
            "mutation_score": len(data) * 0.01
        }

    if data_type == "snp":
        return {
            "snp_count": len(data),
            "risk_score": len(data) * 0.005
        }

    if data_type == "pdf":
        return data  # already structured

    return {}