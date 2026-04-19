import requests

def fetch_research(query: str):
    try:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"

        params = {
            "query": query,
            "limit": 3,
            "fields": "title,abstract,year,url"
        }

        res = requests.get(url, params=params)
        data = res.json()

        papers = data.get("data", [])

        results = []

        for p in papers:
            results.append({
                "title": p.get("title"),
                "year": p.get("year"),
                "abstract": p.get("abstract"),
                "url": p.get("url")
            })

        return results

    except Exception as e:
        print("RESEARCH ERROR:", e)
        return []