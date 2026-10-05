import streamlit as st
from pathlib import Path
import base64

from document_loader import extract_text
from text_splitter import split_text
from embeddings import generate_embeddings
from vector_store import add_documents
from rag_pipeline import rag_pipeline


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Travel Guide RAG",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Background Image
# -----------------------------

background_path = Path("assets/travel_background.png")

if background_path.exists():

    with open(background_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        /* Remove the gap at the top */
        .stAppViewContainer .main .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 2rem !important;
        }}

        .stMainBlockContainer {{
            padding-top: 0rem !important;
        }}

        [data-testid="stMainBlockContainer"] {{
            padding-top: 0rem !important;
        }}

        /* Make Streamlit header transparent */
        header[data-testid="stHeader"] {{
            background: transparent !important;
        }}

        /* Full-page background */
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(255,255,255,0.12),
                    rgba(255,255,255,0.12)
                ),
                url("data:image/png;base64,{encoded_image}");

            background-size: cover;
            background-position: center top;
            background-attachment: fixed;
            min-height: 100vh;
        }}

        /* Main title - Navy Blue */
        .main-title {{
            font-size: 42px;
            font-weight: 900;
            color: #000080;
            text-align: center;
            margin-top: 0px !important;
            margin-bottom: 5px;
        }}

        /* Subtitle - Dark Green */
        .main-subtitle {{
            font-size: 23px;
            font-weight: 900;
            color: #064E3B;
            text-align: center;
            margin-top: 0px !important;
            margin-bottom: 18px;
        }}

        /* Upload heading - Brown */
        .section-title {{
            font-size: 25px;
            font-weight: 900;
            color: #6B3E26;
            margin-top: 0px !important;
            margin-bottom: 6px;
        }}

        /* AI heading - Black */
        .ai-title {{
            font-size: 28px;
            font-weight: 900;
            color: #000000;
            margin-top: 15px;
            margin-bottom: 5px;
        }}

        /* Description - Navy Blue */
        .description {{
            font-size: 18px;
            font-weight: 800;
            color: #000080;
            margin-bottom: 10px;
        }}

        /* Upload box */
        .upload-box {{
            background: rgba(255, 255, 255, 0.88);
            padding: 10px 16px;
            border-radius: 16px;
            border: 2px solid rgba(6, 78, 59, 0.35);
            box-shadow: 0px 5px 18px rgba(0,0,0,0.12);
            margin-bottom: 10px;
        }}

        /* File uploader text - Dark Green */
        [data-testid="stFileUploader"] {{
            font-weight: 800;
            color: #064E3B;
        }}

        /* File uploader label */
        [data-testid="stFileUploader"] label {{
            color: #064E3B !important;
            font-weight: 800 !important;
            font-size: 16px !important;
        }}

        /* Button */
        .stButton > button {{
            background-color: #064E3B;
            color: white;
            font-weight: 800;
            border-radius: 10px;
            border: none;
            padding: 8px 20px;
        }}

        .stButton > button:hover {{
            background-color: #000080;
            color: white;
        }}

        /* AI Answer - White and Thick */
        [data-testid="stChatMessage"] .stMarkdown {{
            color: white !important;
            font-weight: 800 !important;
        }}

        [data-testid="stChatMessage"] .stMarkdown p {{
            color: white !important;
            font-weight: 800 !important;
        }}

        /* Chat input */
        .stChatInput textarea {{
            min-height: 45px !important;
            height: 45px !important;
            max-height: 45px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

else:

    st.error(
        "Background image not found. "
        "Please place travel_background.png inside the assets folder."
    )


# -----------------------------
# Title
# -----------------------------

st.markdown(
    '<div class="main-title">🌍 Travel Guide RAG</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">Your AI Travel Companion ✈️</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Upload Travel Document
# -----------------------------

st.markdown(
    '<div class="section-title">📄 Upload Your Travel Guide</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="upload-box">',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload a PDF, TXT, or DOCX file",
    type=["pdf", "txt", "docx"]
)

if uploaded_file is not None:

    file_path = Path("documents") / uploaded_file.name

    file_path.parent.mkdir(exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully! ✅")

    if st.button("Process Document"):

        with st.spinner("Processing your travel guide..."):

            # Extract text
            text = extract_text(file_path)

            # Split text
            chunks = split_text(text)

            # Generate embeddings
            embeddings = generate_embeddings(chunks)

            # Store in vector database
            added = add_documents(
                chunks,
                embeddings,
                uploaded_file.name
            )

        st.success(
            f"Document processed successfully! "
            f"Added {added} new chunks."
        )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# -----------------------------
# Chat Section
# -----------------------------

st.markdown(
    '<div class="ai-title">🤖 AI Travel Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">'
    'Ask me anything about your uploaded travel guide 🌍'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# User Question
# -----------------------------

question = st.chat_input(
    "Ask a question about your travel guide..."
)


# -----------------------------
# Generate Answer
# -----------------------------

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, documents = rag_pipeline(
                question,
                top_k=3
            )

        st.write(answer)