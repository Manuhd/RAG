import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
from embeddings import get_embedding

client = chromadb.PersistentClient(path="vectorstore")
collection = client.get_or_create_collection("docs")

# -------------------------
# 1. Extract text from PDF
# -------------------------
def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# -------------------------
# 2. Chunk text
# -------------------------
def chunk_text(text, chunk_size=500):
    chunks = []
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# -------------------------
# 3. Save to Chroma DB
# -------------------------
def store_document(chunks):
    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk)
        collection.add(
            ids=[f"chunk_{i}"],
            documents=[chunk],
            embeddings=[emb]
        )

# -------------------------
# 4. Retrieve relevant chunks
# -------------------------
def retrieve(query):
    q_emb = get_embedding(query)
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=3
    )
    return results["documents"][0]
