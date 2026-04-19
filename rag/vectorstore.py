def get_vectorstore():
    class VectorStore:
        def similarity_search(self, query, k=2):
            return [
                type("Doc", (), {
                    "page_content": "Studies show high GC regions correlate with mutation hotspots."
                })(),
                type("Doc", (), {
                    "page_content": "Diabetes risk is linked with metabolic gene variations."
                })(),
            ]

    return VectorStore()