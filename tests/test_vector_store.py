from document_loader import extract_text
from text_splitter import split_text
from embeddings import generate_embeddings
from vector_store import add_documents, collection


file_path = "documents/sample_travel_guide.pdf"

# 1. Extract text
text = extract_text(file_path)

# 2. Split text
chunks = split_text(text)

# 3. Generate embeddings
embeddings = generate_embeddings(chunks)

# 4. Store in ChromaDB
add_documents(
    chunks,
    embeddings,
    "sample_travel_guide.pdf"
)

print("DOCUMENTS STORED SUCCESSFULLY")
print("--------------------------------")
print("Number of chunks:", len(chunks))

# Check how many documents are in ChromaDB
print("Documents in database:", collection.count())