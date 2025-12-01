from snowflake.cortex import complete

def doc_rag_search(query: str):
    """Demo RAG: ejects placeholder text."""
    prompt = f"Search staged documents for relevant content.\nQuery: {query}"
    result = complete(model="llama3.2-vision", prompt=prompt)
    return {"document_context": result.text}
