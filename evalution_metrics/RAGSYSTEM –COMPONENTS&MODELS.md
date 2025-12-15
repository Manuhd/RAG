
# 🧠 RAG SYSTEM – COMPONENTS & MODELS

## 1️⃣ Embedding Model (Indexing & Retrieval)

👉 Converts text → vectors

### Models

* **Sentence-BERT (SBERT)**
* **all-MiniLM-L6-v2**
* **E5** (e5-small / base / large)
* **BGE Embeddings** (bge-small / base / large)
* **Instructor-XL / Instructor-Base**
* **OpenAI text-embedding-3-small / large**
* **Cohere Embed**
* **Jina Embeddings**

📌 Used in: FAISS, Pinecone, Weaviate, Chroma

---

## 2️⃣ Retriever Model

👉 Finds top-K relevant documents

### Dense Retrievers

* **DPR (Dense Passage Retriever)**
* **SBERT Retriever**
* **BGE Retriever**
* **E5 Retriever**

### Sparse Retrievers

* **BM25**
* **TF-IDF**
* **ElasticSearch (Lucene)**

### Hybrid Retrievers

* **BM25 + Embeddings**
* **Weaviate Hybrid**
* **Pinecone Hybrid**

---

## 3️⃣ Reranker Model

👉 Re-scores retrieved documents (query + doc together)

### Cross-Encoder Rerankers

* **cross-encoder/ms-marco-MiniLM-L-6-v2**
* **cross-encoder/ms-marco-MiniLM-L-12-v2**
* **BAAI/bge-reranker-base**
* **BAAI/bge-reranker-large**
* **Cohere Rerank API**
* **OpenAI Rerank API**

### Late Interaction Rerankers

* **ColBERT**
* **ColBERTv2**

### LLM-based Reranking

* **GPT-4 / GPT-4o**
* **Gemini Pro**
* **Claude**

---

## 4️⃣ Generator Model (LLM)

👉 Generates final answer

### Models

* **GPT-4 / GPT-4o**
* **Gemini Pro**
* **Claude**
* **LLaMA 2 / 3**
* **Mistral**
* **Phi**
* **Falcon**

---

## 5️⃣ Prompt / Guardrail Layer

👉 Controls hallucinations & format

### Techniques (not models)

* System Prompt
* Context-only answering
* Refusal rules
* Answer-with-citations
* JSON schema output

---

## 6️⃣ Evaluation Models / Metrics

👉 Measures quality

### Metric Frameworks

* **RAGAS**
* **TruLens**
* **DeepEval**
* **LangSmith**

### Metrics

* Faithfulness
* Context Recall
* Context Precision
* Answer Relevancy
* Hallucination Risk
* Confidence Score

---

## 7️⃣ Optional Agent / Orchestration Models

👉 Multi-step reasoning

* **LangChain Agents**
* **LlamaIndex Agents**
* **Auto-GPT**
* **CrewAI**

---

# 🔗 Complete RAG Flow (All Components)

```
User Query
 ↓
Embedding Model
 ↓
Retriever (Dense / Sparse / Hybrid)
 ↓
Reranker
 ↓
Prompt + Context
 ↓
LLM (Generator)
 ↓
Evaluation (RAGAS)
```

---

## 🎯Short

> **A production RAG system uses separate models for embeddings, retrieval, reranking, generation, and evaluation—each optimized for its own task.**

---
