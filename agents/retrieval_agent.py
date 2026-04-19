from rag.vectorstore import get_vectorstore

def retrieval_agent_node(state):
    try:
        vectorstore = get_vectorstore()

        query = str(state.get("risks", {}))

        docs = vectorstore.similarity_search(query, k=2)

        context = " ".join([d.page_content for d in docs])

    except Exception as e:
        print("RAG ERROR:", e)
        context = "Genetic variations may influence disease risks."

    return {**state, "context": context}