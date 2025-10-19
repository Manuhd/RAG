from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Sample documents / knowledge
# ----------------------------
docs = [
    "LangChain is a framework for building applications with LLMs.",
    "RAG stands for Retrieval-Augmented Generation.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors."
]

# Vectorize documents
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(docs)

# ----------------------------
# Helper function
# ----------------------------
def retrieve(query, top_k=1):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    return [docs[i] for i in top_indices]

# ----------------------------
# FastAPI setup
# ----------------------------
app = FastAPI(title="Minimal RAG API")

class QueryRequest(BaseModel):
    question: str
    top_k: int = 1

@app.post("/ask")
def ask_question(request: QueryRequest):
    results = retrieve(request.question, top_k=request.top_k)
    return {"answer": " ".join(results)}
