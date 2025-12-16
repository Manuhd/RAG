## 🔷 What is FAISS?

**FAISS (Facebook AI Similarity Search)** is a **high-performance vector similarity search library** developed by Meta.

It is used to:

* Store vector embeddings
* Perform fast similarity search (nearest neighbor search)
* Power retrieval systems like **RAG**

📌 FAISS is **not a database** — it is an **indexing/search engine**.

---

## 🔷 Why FAISS is Used

Traditional databases struggle with:

* High-dimensional vectors (e.g., 768 dims)
* Cosine / L2 similarity at scale

FAISS is optimized for:

* Millions / billions of vectors
* Low-latency search
* CPU & GPU acceleration

---

## 🔷 Where FAISS Fits in RAG

```
Documents → Embeddings → FAISS Index → Retriever → LLM
```

FAISS replaces:
❌ SQL LIKE
❌ Full-table scans

---

## 🔷 FAISS Index Types (Most Important Part)

FAISS provides **multiple index types**, each optimized for different scales.

---

### 1️⃣ **Flat Index (Exact Search)**

```python
faiss.IndexFlatL2(dim)
```

🔹 How it works:

* Compares query against **all vectors**
* No approximation

🔹 Pros:

* 100% accurate
* Simple
* No training

🔹 Cons:

* Slow at scale

🔹 Best for:

* Small datasets (< 1k vectors)

---

### 2️⃣ **IVF (Inverted File Index)**

```python
faiss.IndexIVFFlat(quantizer, dim, nlist)
```

🔹 How it works:

* Clusters vectors
* Searches only relevant clusters

🔹 Key parameters:

* `nlist` → number of clusters
* `nprobe` → clusters searched at query time

🔹 Pros:

* Much faster than Flat
* Scales well

🔹 Cons:

* Approximate search
* Needs training

🔹 Best for:

* Medium–large datasets (10k+)

---

### 3️⃣ **HNSW (Graph-Based Index)**

```python
faiss.IndexHNSWFlat(dim, M)
```

🔹 How it works:

* Builds a graph of vectors
* Navigates graph during search

🔹 Key parameters:

* `M` → graph connections
* `efSearch` → accuracy vs speed

🔹 Pros:

* Very fast
* High recall

🔹 Cons:

* Higher memory usage

🔹 Best for:

* Low-latency production systems

---

### 4️⃣ **PQ (Product Quantization)**

```python
faiss.IndexPQ(dim, m, bits)
```

🔹 How it works:

* Compresses vectors into smaller representations

🔹 Pros:

* Huge memory savings

🔹 Cons:

* Lossy compression
* Lower accuracy

🔹 Best for:

* Massive datasets (1M+ vectors)

---

### 5️⃣ **IVF + PQ (Hybrid Index)**

```python
faiss.IndexIVFPQ(quantizer, dim, nlist, m, bits)
```

🔹 Combines:

* IVF clustering
* PQ compression

🔹 Best for:

* Billion-scale search
* Memory-constrained systems

---

## 🔷 Choosing the Right Index

| Data Size | Recommended Index |
| --------- | ----------------- |
| < 1k      | Flat              |
| 10k       | IVF               |
| 100k      | HNSW              |
| 1M+       | IVF + PQ          |

---

## 🔷 FAISS vs Vector Databases

| Feature     | FAISS         | Vector DB   |
| ----------- | ------------- | ----------- |
| Index types | Yes           | Abstracted  |
| Persistence | Manual        | Automatic   |
| CRUD        | No            | Yes         |
| Scale       | Library-level | Infra-level |

---

## 🎯  Summary

> **“FAISS is a vector similarity search library offering multiple index types such as Flat, IVF, HNSW, and PQ, allowing developers to trade accuracy, speed, and memory depending on scale.”**

---

## 🔑 Final Takeaway

* FAISS = **search engine**
* Index type choice = **performance strategy**
* Flat → IVF → HNSW → PQ as scale grows
* You must **write code** to use FAISS effectively

