from document_loader import extract_text
from text_splitter import split_text

file_path = "documents/sample_travel_guide.pdf"

text = extract_text(file_path)

chunks = split_text(text)

print("TEXT SPLITTING SUCCESSFUL")
print("--------------------------")
print("Total characters:", len(text))
print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0])