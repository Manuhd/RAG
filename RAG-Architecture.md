

# ✅ **RAG Architecture**
![alt-text](https://github.com/Manuhd/RAG/blob/main/RAG%20ARCHITECTURE.drawio.png)
```
                ┌────────────────┐
                │ Knowledge Base │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │  Data Chunks   │   ← Chunk PDFs / Docs / Website
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Embedding      │
                │    Model       │   ← Converts text → vectors
                └───────┬────────┘
        ┌───────────────┼──────────────────┐
        │               │                  │
        ▼               ▼                  ▼
User Query → Embedding(Query)       Document Embeddings
                         │
                         ▼
                ┌────────────────┐
                │   Vector DB    │   ← Stores embeddings
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │ Retrieved Docs │   ← Top-k most similar chunks
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │      LLM       │   ← GPT / Gemini / Llama
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    Response    │
                └────────────────┘
```

---

**RAG (Retrieval-Augmented Generation)** =
LLM + search from your private database → more accurate answers.

### Steps:

1. **Knowledge base** (PDFs, Docs, HTML, DB data)
2. **Chunking** → break into small pieces
3. **Embedding model** → convert each chunk into vectors
4. **Vector DB** → store embeddings for fast search
5. **User Query** → convert query to vector
6. **Retriever** → find top-k similar chunks using cosine similarity
7. **LLM** → uses retrieved chunks as context
8. **Final Response** → grounded in your data, not hallucinated

---
