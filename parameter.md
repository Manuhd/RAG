
# ✅ **1. BASIC RETRIEVER PARAMETERS**

These are the MOST commonly used.

---

## **1) `k` (Top-K)**

How many chunks to retrieve.

**Meaning:**
More chunks = more context (but slower).

**Syntax:**

```python
search_kwargs={"k": 5}
```

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)
```

---

## **2) `search_type`**

Which retrieval method to use.

**Values:**

* `"similarity"` (default)
* `"mmr"` (Maximal Marginal Relevance)
* `"similarity_score_threshold"`

**Example:**

```python
retriever = vectorstore.as_retriever(search_type="mmr")
```

---

# ✅ **2. ADVANCED RETRIEVER PARAMETERS**

These help you fine-tune retrieval quality.

---

## **3) `score_threshold`**

Only return chunks above a certain similarity score.

**Syntax:**

```python
search_kwargs={"score_threshold": 0.3}
```

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3}
)
```

---

## **4) `filter` (Metadata Filter)**

Retrieve chunks only from specific categories/languages.

**Syntax:**

```python
search_kwargs={"filter": {"category": "loan"}}
```

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"filter": {"department": "banking"}}
)
```

---

## **5) `lambda_mult` (For MMR)**

Controls diversity of chunks (0 → diverse, 1 → similar).

**Syntax:**

```python
search_kwargs={"lambda_mult": 0.5}
```

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "lambda_mult": 0.5}
)
```

---

## **6) `fetch_k`**

How many candidates to fetch *before* MMR selects final top-k.

Useful when using `"mmr"`.

**Syntax:**

```python
search_kwargs={"fetch_k": 20, "k": 5}
```

---

## **7) `maximal_marginal_relevance` (Older version)**

Boolean for enabling MMR manually.

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 5,
        "maximal_marginal_relevance": True
    }
)
```

---

## **8) `embedding` (Custom Embedding Model)**

If you want a specific embedder.

**Example:**

```python
retriever = vectorstore.as_retriever(
    embeddings=my_embedding_model
)
```

---

## **9) `include_metadata`**

Whether to return metadata with chunks.

**Example:**

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"include_metadata": True}
)
```

---

# ⭐ **FULL RETRIEVER PARAMETER SYNTAX (All-in-One)**

```
retriever = vectorstore.as_retriever(
    search_type="similarity" | "mmr" | "similarity_score_threshold",
    search_kwargs={
        "k": int,
        "fetch_k": int,
        "lambda_mult": float,
        "score_threshold": float,
        "filter": dict,
        "maximal_marginal_relevance": bool,
        "include_metadata": bool
    }
)
```

---


---

# ✅ **Example 1: Basic Similarity Search**

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)
```

---

# ✅ **Example 2: MMR Retrieval (Diverse Results)**

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 25,
        "lambda_mult": 0.5
    }
)
```

---

# ✅ **Example 3: Score Threshold Retrieval**

```python
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "score_threshold": 0.35,
        "k": 5
    }
)
```

---

# ✅ **Example 4: Metadata Filtering**

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 5,
        "filter": {"category": "loan-policy"}
    }
)
```

---

# ✨ **Example 5: Combine Everything**

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 7,
        "fetch_k": 30,
        "lambda_mult": 0.4,
        "filter": {"language": "en"},
        "include_metadata": True
    }
)
```

---

# ⭐ Final Summary — List of ALL Retriever Parameters

| Parameter                      | Meaning                                 |
| ------------------------------ | --------------------------------------- |
| **k**                          | Number of chunks retrieved              |
| **fetch_k**                    | Total candidates before final selection |
| **search_type**                | similarity / mmr / threshold            |
| **score_threshold**            | Minimum similarity                      |
| **filter**                     | Metadata filters                        |
| **lambda_mult**                | Diversity control for MMR               |
| **maximal_marginal_relevance** | Older MMR toggle                        |
| **include_metadata**           | Include metadata in results             |
| **embedding**                  | Custom embedder                         |

---


