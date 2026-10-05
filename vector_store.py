import chromadb


# ============================================================
# CHROMA DATABASE SETTINGS
# ============================================================

DB_PATH = "./rag_database"

COLLECTION_NAME = "travel_documents"


# ============================================================
# CREATE CHROMA CLIENT
# ============================================================

client = chromadb.PersistentClient(
    path=DB_PATH
)


# ============================================================
# CREATE / GET COLLECTION
# ============================================================

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


# ============================================================
# ADD DOCUMENTS
# ============================================================

def add_documents(
    chunks,
    embeddings,
    source
):

    ids = []

    metadatas = []

    for i in range(len(chunks)):

        chunk_id = f"{source}_{i}"

        ids.append(chunk_id)

        metadatas.append(
            {
                "source": source,
                "chunk": i
            }
        )


    # --------------------------------------------------------
    # CHECK EXISTING IDS
    # --------------------------------------------------------

    existing = collection.get(
        ids=ids
    )

    existing_ids = set(
        existing.get("ids", [])
    )


    # --------------------------------------------------------
    # FIND ONLY NEW CHUNKS
    # --------------------------------------------------------

    new_chunks = []

    new_embeddings = []

    new_ids = []

    new_metadatas = []


    for i in range(len(chunks)):

        chunk_id = f"{source}_{i}"

        if chunk_id not in existing_ids:

            new_chunks.append(
                chunks[i]
            )

            new_embeddings.append(
                embeddings[i]
            )

            new_ids.append(
                chunk_id
            )

            new_metadatas.append(
                metadatas[i]
            )


    # --------------------------------------------------------
    # DOCUMENT ALREADY EXISTS
    # --------------------------------------------------------

    if len(new_chunks) == 0:

        return 0


    # --------------------------------------------------------
    # ADD NEW DOCUMENTS
    # --------------------------------------------------------

    collection.add(
        ids=new_ids,

        documents=new_chunks,

        embeddings=new_embeddings,

        metadatas=new_metadatas
    )


    return len(new_chunks)


# ============================================================
# SEARCH
# ============================================================

def search(
    query_embedding,
    top_k=3
):

    # Make sure top_k is always a valid integer
    if top_k is None:
        top_k = 3

    top_k = int(top_k)

    # Don't request more documents than exist
    total_documents = collection.count()

    if total_documents == 0:
        return {
            "documents": [[]],
            "metadatas": [[]],
            "ids": [[]]
        }

    top_k = min(
        top_k,
        total_documents
    )


    results = collection.query(
        query_embeddings=[query_embedding],

        n_results=top_k
    )


    return results