from document_loader import extract_text


file_path = "documents/sample_travel_guide.pdf"

text = extract_text(file_path)

print("TEXT EXTRACTED SUCCESSFULLY")
print("----------------------------")
print(text[:2000])