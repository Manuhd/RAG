# ✅ **What is Metadata in RAG?**

**Metadata** = Extra information stored **along with each chunk** in your vector database.

Embeddings = numerical representation
Metadata = labels, tags, IDs, titles, filenames etc.

Metadata helps the retriever to **filter**, **rank**, and **search** better.

---

# 🎯 Why Metadata is Important in RAG?

Because:

✔ It **improves retrieval accuracy**
✔ It allows **filtering** (example: only retrieve documents from “banking” category)
✔ It enables **safety** (don’t retrieve old/outdated docs)
✔ It improves **context** for LLM during answer generation

---

# 📌 Example of metadata stored in Vector DB

Let’s say you upload a PDF called:
**"Bank Loan Policy 2024.pdf"**

Chunks will be stored like:

### **Chunk 1**

```
id: "chunk_1"
text: "Loan eligibility requires the customer to submit KYC documents..."
metadata: {
    "filename": "Bank Loan Policy 2024",
    "page": 2,
    "section": "Eligibility",
    "date": "2024-01-10",
}
```

### **Chunk 2**

```
id: "chunk_2"
text: "Interest rate varies from 8% to 9% based on credit score..."
metadata: {
    "filename": "Bank Loan Policy 2024",
    "page": 3,
    "section": "Interest Rate",
    "date": "2024-01-10",
}
```

👉 Embeddings store the **vectors**
👉 Metadata stores **labels** that describe the chunk

---

# 🧠 What Metadata is Typically Stored?

(Interview-Important)

### **1. Document-level metadata**

* filename
* URL
* document_id
* author
* created date
* updated date

### **2. Chunk-level metadata**

* page number
* paragraph
* section heading
* tags
* category

### **3. System metadata**

* embedding model
* chunk ID
* chunk size

---

# 🧪 Example query with metadata filter

**User asks:**
“Give me only 2024 loan policies.”

Your retriever can do:

```
results = collection.query(
    query_embeddings=[user_emb],
    n_results=5,
    where={"date": "2024-01-10"}
)
```

Translated:
**Retrieve only chunks where metadata.date is 2024-01-10.**

---

# 📚 Why Metadata Helps a Real Project?

### **Scenario: Banking Chatbot (your BFSI project example)**

User asks:

> “What is the latest interest rate?”

If metadata stores "year":

* 2022 doc → should not be retrieved
* 2024 doc → must be retrieved

Metadata-like:

```
"version": "2024",
"dept": "Retail Banking",
"classification": "public"
```

You can enforce filter:

```
where={"version": "2024"}
```

This gives **accurate & safe** RAG.

---

# 🔥 Metadata Example Code (Python + Chroma)

```python
collection.add(
    ids=[f"chunk_{i}"],
    documents=[chunk],
    embeddings=[embedding],
    metadatas=[{
        "filename": file_name,
        "page": page_number,
        "section": section_name,
        "category": "banking",
        "version": "2024"
    }]
)
```

---

# 🎨 Easy way to remember

**Chunk** = Text
**Embedding** = Vector
**Metadata** = Extra details that help retrieval

Simple formula:

👉 RAG = Embeddings + Metadata + Filtering

---

# 📝 Summary

**“Metadata in RAG is the extra information saved with each chunk (like filename, page number, section, date, topic). It helps in filtering documents, improving retrieval accuracy, and ensuring the LLM uses the latest and relevant information.”**

---


# ✅ **How Data Is Actually Stored in a Vector DB (Chroma / Pinecone / FAISS)**

**Chunk text is NOT stored in vector format.
Only the embeddings are vectors.
The chunk text is stored as NORMAL TEXT in the DB.**

So inside the vector DB:

### ✔ Embedding → vector format

Example:

```
[0.06, 0.08, 0.9, ...]
```

### ✔ Chunk Text → raw text (string)

Example:

```
"Loan interest rate starts from 8% for salaried individuals..."
```

### ✔ Metadata → JSON

Example:

```
{ "page": 3, "filename": "loan_policy.pdf" }
```

---

# 🔍 **How Data Is Actually Stored in a Vector DB (Chroma / Pinecone / FAISS)**

A typical row looks like:

```
{
  id: "chunk_20",
  embedding: [0.06, 0.08, 0.9, ...],  <-- VECTOR
  document: "Customers must submit KYC before approval",  <-- TEXT
  metadata: {
      page: 3,
      filename: "loan_policy.pdf",
      section: "KYC Rules"
  }
}
```

So the DB has 3 parts:

| Stored item           | Format       | Purpose               |
| --------------------- | ------------ | --------------------- |
| embedding             | vector array | for similarity search |
| document (chunk text) | plain text   | for LLM context       |
| metadata              | JSON/dict    | for filtering         |

---

# 🧠 **Why chunk text is NOT stored as vector?**

Because:

1. **Vectors are only used for similarity search.**
2. **LLM needs real text**, not numbers.
3. After matching, the top-k chunks are returned as **original text**, not vectors.

Example:

User asks:

> “What is the interest rate?”

RAG returns:

```
"Interest rate ranges from 8% to 9%..."
```

This is the **original chunk text**, NOT the embedding vector.

---

# 🔥 EASY WAY TO REMEMBER

### **Embedding = numbers (for searching)**

### **Chunk text = words (for answering)**

### **Metadata = labels (for filtering)**

---

# 🎯 **Summary**

> “In a vector DB, only the embeddings are vectors.
> The chunk text is stored as normal text so the LLM can read it during answer generation.
> Metadata is also stored as JSON to filter and refine retrieval.”

---

# ✅ **When Is Metadata Created in RAG?**

### ✔ Metadata is created at the **chunking stage**

When you split the PDF into chunks, you also create metadata for each chunk:

* filename
* page number
* section heading
* chunk_id
* tags / labels
* created date
* document type
* category

This metadata is **attached to each chunk** **before** storing into the vector database.

---

# 📦 **Flow: Chunking + Metadata Creation**

### Step 1: Read PDF

### Step 2: Extract text per page

### Step 3: Chunk the text

### Step 4: **Generate metadata for each chunk**

### Step 5: Send (chunk + metadata) to embedding model

### Step 6: Store in vector DB

---

# 🧠 Example: Metadata created during chunking

Suppose you split a 50-page PDF into 200 chunks.

For chunk #37, you generate:

```
{
  "chunk_id": "loan_doc_37",
  "filename": "Bank Loan Policy 2024.pdf",
  "page": 12,
  "section": "Interest Rate",
  "category": "banking",
  "year": "2024"
}
```

This is metadata created **during chunking**.

Then you embed it and store:

```
collection.add(
    ids=["loan_doc_37"],
    documents=["Interest rate ranges from 8% to 9%..."],
    embeddings=[embedding],
    metadatas=[{
      "filename": "Bank Loan Policy 2024.pdf",
      "page": 12,
      "section": "Interest Rate",
      "category": "banking",
      "year": "2024"
    }]
)
```

---

# 🎯 **Why metadata is created during chunking?**

Because:

### ✔ 1. Chunk needs identity

Each chunk must have an ID (chunk_1, chunk_2...)

### ✔ 2. We want to filter by page/section later

For example:

```
where={"year": "2024"}
```

### ✔ 3. We want traceability

If LLM gives wrong answer, we can check which chunk caused it.

### ✔ 4. Helps re-ranking

Metadata helps choose more relevant chunks.

---

# 🔥 YOUR UNDERSTANDING IS CORRECT

> **Chunking produces text chunks + metadata.
> Embeddings convert text to vectors.
> Vector DB stores: vector + text + metadata.**

---


# ✅ **During retrieval, only the embeddings are used for similarity search.**

But…

👉 **After retrieval**, the vector DB returns:

* the chunk text
* the metadata
* the similarity score
  (back to the LLM)

So **retrieval = embedding matching**,
**but response = original chunk text**.

Let’s break it down.

---

# 🔍 **Retrieval Process Step-by-Step**

## **Step 1 — User query embedding (vector)**

```
[0.11, 0.02, 0.90]
```

## **Step 2 — Compare with stored embeddings**

Vector DB does:

✔ cosine similarity
✔ dot product
✔ L2 distance
(according to index type)

Only **vectors** are compared.

### So YES → during matching, ONLY EMBEDDINGS are used.

---

# 🎯 **Step 3 — After matching, vector DB returns:**

### For top-k chunks, DB returns:

```
{
  "id": "chunk_37",
  "document": "Interest rate ranges from 8% to 9%...",
  "metadata": { "page": 12, "year": 2024 },
  "embedding": [0.06, 0.08, 0.9],
  "score": 0.84
}
```

So final result includes:

| Item           | Purpose                            |
| -------------- | ---------------------------------- |
| **chunk text** | used by LLM to answer              |
| **metadata**   | for filtering / reranking          |
| **embedding**  | used only during similarity search |
| **score**      | similarity ranking                 |

---

# 🧠 **Short Explanation (Best for Interview)**

### ✔ Retrieval uses only embeddings (vectors) to find similar chunks.

### ✔ But the output of retrieval includes text + metadata + score.

---

# 🎨 Easy Diagram for You

**Query → Embedding → Compare vectors → Get top-k**
**→ Return text + metadata → LLM → Final answer**

---

# ⭐ Summary

> “During retrieval, only embeddings are used for similarity matching.
> But after matching, the vector DB returns the actual chunk text and metadata so the LLM can generate the answer.”

---





