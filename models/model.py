class RiskModel:
    def predict(self, features):

        score = sum([
            v for v in features.values() if isinstance(v, (int, float))
        ])

        base = min(score / 100, 1)

        return {
            "Heart Disease": round(base, 2),
            "Diabetes": round(1 - base, 2),
            "Cancer": round(base * 0.8, 2)
        }
model=RiskModel()