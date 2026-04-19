import re

def extract_health_features(text: str):
    cholesterol = re.findall(r'cholesterol.*?(\d+)', text.lower())
    glucose = re.findall(r'glucose.*?(\d+)', text.lower())

    return {
        "cholesterol": int(cholesterol[0]) if cholesterol else 0,
        "glucose": int(glucose[0]) if glucose else 0
    }