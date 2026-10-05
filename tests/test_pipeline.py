from rag_pipeline import rag_pipeline


question = "What places can I visit in Switzerland?"

answer, documents = rag_pipeline(question)


print("COMPLETE RAG PIPELINE SUCCESSFUL")
print("---------------------------------")

print("\nQuestion:")
print(question)

print("\nFinal Answer:")
print("================")
print(answer)

print("\nRetrieved Sources:")
print("==================")

for i, document in enumerate(documents, start=1):
    print(f"\n--- Source {i} ---")
    print(document)