from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text(file_path):

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    # PDF
    if extension == ".pdf":

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    # TXT
    elif extension == ".txt":

        return file_path.read_text(
            encoding="utf-8"
        )

    # DOCX
    elif extension == ".docx":

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text

    else:

        raise ValueError(
            "Unsupported file type"
        )