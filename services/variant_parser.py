import re

def extract_rsids(text: str):
    return re.findall(r'rs\d+', text.lower())