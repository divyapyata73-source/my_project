import ollama

MODEL_NAME = "phi3:latest"


def generate_answer(question, context):

    prompt = f"""
You are a helpful international travel guide assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:

"I don't know based on the provided documents."

Do not invent or add information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]