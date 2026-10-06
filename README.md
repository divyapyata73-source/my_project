# 🌍 Travel Guide RAG

An AI-powered **Travel Guide Chatbot** built using **Python, Streamlit, RAG (Retrieval-Augmented Generation), Sentence Transformers, and a Vector Database**.

The application allows users to upload their own travel guides in **PDF, TXT, or DOCX** format and ask questions about the uploaded content. The system retrieves the most relevant information from the document and generates an answer using an AI model.

---

## ✨ Features

- 📄 Upload travel guides in **PDF, TXT, or DOCX** format
- 🔍 Extract text from uploaded documents
- ✂️ Split large documents into smaller chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗄️ Store document embeddings in a vector database
- 🔎 Retrieve the most relevant document chunks for a question
- 🤖 Generate AI-based answers using the RAG pipeline
- 💬 Interactive chat interface using Streamlit
- 🌍 Designed specifically for travel-related information
- 🖼️ Custom travel background and user-friendly interface

---

## 🏗️ How the RAG System Works

The application follows the Retrieval-Augmented Generation pipeline:

```text
Upload Travel Guide
        ↓
Extract Text
        ↓
Split Text into Chunks
        ↓
Generate Embeddings
        ↓
Store in Vector Database
        ↓
User Asks Question
        ↓
Convert Question into Embedding
        ↓
Retrieve Relevant Chunks
        ↓
Generate AI Answer
        ↓
Display Answer
```

The system uses the uploaded travel guide as the knowledge source instead of relying only on general AI knowledge.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11.9 | Programming language |
| Streamlit | Web application interface |
| Sentence Transformers | Text embeddings |
| Vector Database | Store and retrieve embeddings |
| PyPDF | PDF text extraction |
| python-docx | DOCX text extraction |
| Python | Text processing and RAG pipeline |
| Ollama / LLM | AI answer generation |
| HTML/CSS | User interface customization |

---

## 📂 Project Structure

```text
travel_rag/
│
├── app.py
│
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── rag_pipeline.py
│
├── tests/
│   ├── test_loader.py
│   └── test_generator.py
│
├── documents/
│   └── uploaded travel documents
│
├── assets/
│   └── travel_background.png
│
├── rag_database/
│   └── vector database files
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Project Workflow

### 1. Upload Document

The user uploads a travel guide through the Streamlit interface.

Supported formats:

- PDF
- TXT
- DOCX

### 2. Extract Text

The uploaded document is processed using the document loader.

```python
text = extract_text(file_path)
```

### 3. Split Text

The extracted text is divided into smaller chunks.

```python
chunks = split_text(text)
```

Chunking makes it easier to search for relevant information.

### 4. Generate Embeddings

Each chunk is converted into a numerical vector using an embedding model.

```python
embeddings = generate_embeddings(chunks)
```

These embeddings represent the semantic meaning of the text.

### 5. Store in Vector Database

The chunks and their embeddings are stored in the vector database.

```python
added = add_documents(
    chunks,
    embeddings,
    uploaded_file.name
)
```

### 6. Ask Questions

The user can ask questions through the chat interface.

Example:

```text
What are the best places to visit in Switzerland?
```

### 7. Retrieve Relevant Information

The RAG pipeline searches the vector database and retrieves the most relevant chunks.

```python
answer, documents = rag_pipeline(
    question,
    top_k=3
)
```

### 8. Generate Answer

The retrieved information is passed to the AI model to generate a relevant answer.

---

## 💻 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/travel-guide-rag.git
```

Move into the project directory:

```bash
cd travel-guide-rag
```

---

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📄 Using the Application

### Step 1

Upload your travel guide.

### Step 2

Click:

```text
Process Document
```

### Step 3

Wait for the document to be processed.

The application will:

```text
Extract → Chunk → Embed → Store
```

### Step 4

Ask a question in the chat box.

For example:

```text
What places should I visit in Switzerland?
```

or:

```text
What transportation options are mentioned in the guide?
```

or:

```text
Which food is recommended in this destination?
```

The AI assistant will retrieve relevant information from the uploaded travel guide and generate an answer.

---

## 🌍 Example Travel Guide

The application can be used with travel information such as:

```text
Switzerland Travel Guide

Zurich
↓
Lucerne
↓
Interlaken
↓
Montreux
↓
Zermatt
```

The document can contain information about:

- Tourist attractions
- Transportation
- Hotels
- Restaurants
- Local food
- Travel routes
- Activities
- Suggested itineraries
- Travel tips

---

## 🧠 RAG Architecture

```text
                ┌─────────────────────┐
                │   Travel Document   │
                │   PDF / TXT / DOCX  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Text Extraction  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Text Chunking   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Embeddings       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Vector Database   │
                └──────────┬──────────┘
                           │
                           │
User Question ─────────────┤
                           ▼
                ┌─────────────────────┐
                │  Similarity Search  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Relevant Chunks   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      AI / LLM       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Final Answer     │
                └─────────────────────┘
```

---

## 🧪 Testing

The project contains tests for important components.

Run the tests using:

```bash
pytest
```

Example components tested include:

- Document extraction
- RAG generation
- Document processing

---

## 🔐 Important Notes

Do not upload sensitive information such as:

- API keys
- Passwords
- Personal documents
- `.env` files containing secrets

Make sure sensitive files are included in `.gitignore`.

Example:

```text
.env
venv/
__pycache__/
*.pyc
rag_database/
```

---

## 🚀 Future Enhancements

Possible future improvements include:

- 🗺️ Interactive maps for travel destinations
- 📍 Location-based recommendations
- 🏨 Hotel recommendations
- 🍴 Restaurant recommendations
- ✈️ Flight information
- 🌦️ Weather information
- 🧳 Personalized travel itineraries
- 🌐 Multi-language support
- 📱 Mobile-friendly interface
- 🖼️ Destination images
- 🎙️ Voice-based travel assistant
- 💾 Chat history
- 👤 User authentication

---

## 🎯 Project Objective

The main objective of this project is to build an intelligent travel assistant that can understand information from user-provided travel documents and provide useful answers using **Retrieval-Augmented Generation (RAG)**.

Instead of manually searching through large travel guides, users can simply upload their document and ask questions in natural language.

---

## 👩‍💻 Author

**Divya**

B.Tech Student

---

## ⭐ Acknowledgement

This project was developed as an educational project to explore:

- Artificial Intelligence
- Retrieval-Augmented Generation
- Natural Language Processing
- Vector Databases
- Semantic Search
- Streamlit
- Large Language Models

---

## 📌 Project Status

🚧 **Currently under development**

