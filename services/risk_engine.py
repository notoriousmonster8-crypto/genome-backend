import math

# 🔥 Feature weights (like trained coefficients)
GENE_WEIGHTS = {
    "BRCA1": {"Breast Cancer": 2.5},
    "BRCA2": {"Breast Cancer": 2.0},
    "APOE": {"Alzheimer": 1.8},
    "TCF7L2": {"Diabetes": 1.6},
}

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def compute_risk(genome_text: str):
    scores = {}

    genome_text = genome_text.lower()

    # 🔥 accumulate weighted scores
    for gene, diseases in GENE_WEIGHTS.items():
        if gene.lower() in genome_text:
            for disease, weight in diseases.items():
                scores[disease] = scores.get(disease, 0) + weight

    # 🔥 convert to probabilities (ML-style)
    risks = {}
    for disease, score in scores.items():
        risks[disease] = round(sigmoid(score), 2)

    # fallback
    if not risks:
        risks["General Risk"] = 0.3

    return risks