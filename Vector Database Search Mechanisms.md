
# Vector Database Search Mechanisms and Indexing Techniques

## 1️⃣ **HNSW (Hierarchical Navigable Small World)**

**What it is:**
A **fast ANN (Approximate Nearest Neighbor)** search algorithm used by vector DBs to find similar embeddings quickly.

Used by:
✔ ChromaDB
✔ Pinecone
✔ FAISS
✔ Weaviate

### 🧠 **Why use HNSW?**

Because vector comparisons (cosine similarity) become slow with thousands/millions of vectors.

HNSW makes search:

* **Super fast** (logarithmic time)
* **High accuracy**
* **Low memory cost**

### 🔥 Hint:

> “HNSW is the indexing algorithm that speeds up vector similarity search. Instead of checking all vectors, it navigates multiple graph layers to quickly find nearest neighbors.”

---

## 2️⃣ **Filtering (Metadata filtering)**

Filtering = selecting chunks based on **metadata**, not embeddings.

For example:

```
where = {
   "year": "2024",
   "category": "banking",
   "page": {"$gte": 10}
}
```

### ❤️ Why filtering is important?

Because sometimes you only want chunks:

* From a specific **document**
* From a specific **category**
* From a specific **year/version**
* With a specific **tag**

### 🔥 Hint:

> “Filtering restricts retrieval to only those embeddings whose metadata matches certain conditions. It ensures accuracy and prevents irrelevant chunks.”

---

# 3️⃣ **Hybrid Search**

Hybrid Search =
**Vector search + Keyword/Text search combined.**

Used when:

* Some queries need *semantic* meaning
* Some queries need *exact keywords*

### Example:

User types:
“policy number 2024-A”

Vector search → finds “loan policy documents”
Keyword search → finds the exact “2024-A” string

Final result = combined scores.

### Types of hybrid:

* **Vector + BM25**
* **Embedding similarity + keyword frequency**
* **Weighted combination**

### 🔥 Hint:

> “Hybrid search combines semantic embedding search and keyword search. It ensures high recall for both meaning-based queries and exact term searches.”

---

## 4️⃣ **Persistence Directory**

A **folder on disk** where the vector DB stores:

* embeddings
* metadata
* documents
* index files (HNSW graph)

Usually used in **Chroma** and **FAISS**.

Example in Python:

```python
client = chromadb.PersistentClient(path="./chroma_db")
```

This creates folders like:

```
/chroma_db/
    collections/
    indexes/
    metadata/
```

### Why needed?

✔ Vector DB survives restart
✔ You don’t need to re-embed every time
✔ Useful for local storage and offline RAG

### 🔥 Hint:

> “Persistence directory is where the vector DB stores embeddings and indexes permanently so that the database survives restarts.”

---

# 🎁 **One-Liner Summary (Very Clear)**

| Term                      | Meaning                                        |
| ------------------------- | ---------------------------------------------- |
| **HNSW**                  | Indexing algorithm for fast ANN vector search  |
| **Filtering**             | Restricts chunks using metadata                |
| **Hybrid Search**         | Vector search + keyword search combined        |
| **Persistence Directory** | Folder where vector DB stores embeddings/index |

---
**WHEN** each thing happens in the RAG pipeline — HNSW, filtering, hybrid search, persistence directory.
This will make everything crystal clear.

---

## **1️⃣ HNSW — When does it happen?**

### ✔ Happens during **searching**

HNSW is used when the vector DB is trying to find the **nearest embeddings**.

### ✔ Also happens during **index building**

When you insert embeddings, the vector DB updates the HNSW graph.

### **So HNSW happens in 2 moments:**

1. **Indexing time** (when you store embeddings)
2. **Query time** (when vector DB finds similar vectors)

---

## **2️⃣ Filtering — When does it happen?**

### ✔ Happens during **retrieval query**

Not during embedding, not during chunking.

Filtering is applied **after user query embedding** but **before similarity search**.

Example:

```
where = {
  "year": "2024",
  "category": "loan"
}
```

Vector DB will:

1. Find all embeddings with metadata year=2024
2. Search only inside those

---

## **3️⃣ Hybrid Search — When does it happen?**

### ✔ During **retrieval time**, when the user asks a question.

Hybrid search = vector search + keyword search.

Steps:

1. User query → converted to embedding
2. Vector DB runs **semantic search**
3. Vector DB runs **keyword/BM25 search**
4. Combines the scores
5. Returns best chunks

👉 Happens **only at retrieval time**, not during chunking or embedding.

---

## **4️⃣ Persistence Directory — When does it happen?**

### ✔ During **database initialization**

When you create a persistent DB:

```python
client = chromadb.PersistentClient(path="./chroma_db")
```

### ✔ During **insertion**

Data is saved to disk instead of memory.

### ✔ During **restart**

Vector DB loads embeddings + metadata + HNSW index from the persistence directory.

👉 It happens **continuously**, whenever the DB is used.

---

# ⭐ **Overall Timeline **

### **1. Chunking Stage**

⛔ HNSW — No
⛔ Filtering — No
⛔ Hybrid search — No
⛔ Persistence — No

### **2. Embedding Stage**

⛔ HNSW — Index updates happen
⛔ Filtering — No
⛔ Hybrid — No
✔ Persistence — Saves embeddings to disk

### **3. Insert into Vector DB**

✔ HNSW index updated
✔ Persistence directory stores vectors

### **4. Retrieval (User asks question)**

🔥 NOW EVERYTHING HAPPENS HERE:

✔ User embedding created
✔ Filtering applied
✔ HNSW used to find nearest vectors
✔ Hybrid search executed (if enabled)
✔ Persistence directory loads DB

---

# 🎯 Final Ultra-Clear Summary

| Feature                   | When does it happen?                                 |
| ------------------------- | ---------------------------------------------------- |
| **HNSW**                  | Index creation + During retrieval search             |
| **Filtering**             | During retrieval (before similarity search)          |
| **Hybrid Search**         | During retrieval (combining vector + keyword search) |
| **Persistence Directory** | Always active (during save/load of vector DB)        |

---


