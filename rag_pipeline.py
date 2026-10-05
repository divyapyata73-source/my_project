from retriever import retrieve
from generator import generate_answer


def rag_pipeline(question, top_k=3):

    # Step 1: Retrieve relevant chunks
    documents = retrieve(question, top_k)

    # Step 2: Combine retrieved chunks into context
    context = "\n\n".join(documents)

    # Step 3: Generate answer using the context
    answer = generate_answer(question, context)

    return answer, documents