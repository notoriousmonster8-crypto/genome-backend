

import json

with open("database/family_risk.json") as f:
    FAMILY_DB = json.load(f)

def combine_risks(genetic_risks, family_data):
    final = genetic_risks.copy()

    for disease, level in family_data:
        if disease in FAMILY_DB:
            extra = FAMILY_DB[disease].get(level, 0)

            final[disease] = round(
                min(1.0, final.get(disease, 0) + extra),
                2
            )

    return final