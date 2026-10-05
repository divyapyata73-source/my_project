from retriever import retrieve


question = "What places can I visit in Switzerland?"

documents = retrieve(question, top_k=3)


print("RETRIEVER TEST SUCCESSFUL")
print("--------------------------")
print("Question:")
print(question)

print("\nRelevant chunks:")
print("================")

for i, document in enumerate(documents, start=1):
    print(f"\n--- Chunk {i} ---")
    print(document)