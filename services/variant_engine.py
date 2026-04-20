import json

with open("database/variant_db.json") as f:
    VARIANT_DB = json.load(f)

def odds_to_prob(or_value):
    return round(or_value / (1 + or_value), 2)

def compute_variant_risk(rsids):
    risks = {}

    for rsid in rsids:
        if rsid in VARIANT_DB:
            info = VARIANT_DB[rsid]
            disease = info["disease"]
            prob = odds_to_prob(info["odds_ratio"])

            risks[disease] = max(risks.get(disease, 0), prob)

    return risks