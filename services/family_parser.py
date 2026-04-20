def extract_family_history(text: str):
    text = text.lower()
    results = []

    if "father" in text and "diabetes" in text:
        results.append(("Diabetes", "parent"))

    if "mother" in text and "heart" in text:
        results.append(("Heart Disease", "parent"))

    if "grandmother" in text and "cancer" in text:
        results.append(("Cancer", "grandparent"))

    return results