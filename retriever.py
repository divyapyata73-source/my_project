from embeddings import generate_query_embedding
from vector_store import search


def retrieve(question, top_k=3):
    # Convert user's question into an embedding
    query_embedding = generate_query_embedding(question)

    # Search ChromaDB
    results = search(query_embedding, top_k)

    # Get the retrieved document chunks
    documents = results["documents"][0]

    return documents