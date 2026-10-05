from document_loader import extract_text
from text_splitter import split_text
from embeddings import generate_embeddings


file_path = "documents/sample_travel_guide.pdf"

text = extract_text(file_path)

chunks = split_text(text)

embeddings = generate_embeddings(chunks)


print("EMBEDDINGS GENERATED SUCCESSFULLY")
print("---------------------------------")
print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))
print("First 5 values:", embeddings[0][:5])