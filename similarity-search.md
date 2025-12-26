#  What Are Similarity Metrics?

**Similarity metrics** are mathematical functions that measure how alike two items are — such as text, images, embeddings, or other data. They’re fundamental in generative AI for tasks like:

* finding the *most relevant documents* based on a query,
* clustering similar data,
* detecting duplicates,
* semantic search,
* recommendation systems.

In generative AI, especially with embeddings, similarity metrics quantify how close two vectors are in a high-dimensional space.

---

## 🔑 Common Similarity Metrics

### **1. Cosine Similarity**

* **Definition:** Measures the cosine of the angle between two vectors.
* **Range:** –1 (opposite) to +1 (identical).
* **Good for:** Semantic similarity of text embeddings.
* **Scale-agnostic:** Only orientation matters, not length.
* **Formula:**
  
$$
  \text{cos}(A,B)=\frac{A \cdot B}{||A||,||B||}
$$

**Use case:** Compare sentence or document embeddings to find semantically similar texts.

---

### **2. Euclidean Distance**

* **Definition:** Straight-line (L2) distance between two points.
* **Range:** 0 to ∞ (0 means identical).
* **Good for:** Spatial similarity where actual distance matters.
* **Formula:**
  
$$
  ||A - B||_2 = \sqrt{\sum_i(A_i-B_i)^2}
$$

**Use case:** Clustering embeddings using algorithms like k-means or t-SNE.

---

### **3. Manhattan (L1) Distance**

* **Definition:** Sum of absolute differences across dimensions.
* **Formula:**
  
$$
  ||A - B||_1 = \sum_i |A_i - B_i|
$$

**Use case:** Situations where differences in individual dimensions are additive.

---

### **4. Dot Product**

* **Definition:** Measures vector correlation by raw multiplication.
* **Range:** Negative to positive values.
* **Note:** Closely related to cosine similarity if vectors are normalized.
* **Dot Product formula:**

$$
Q \cdot D = \sum Q_i \times D_i
$$

**Use case:** Simple and fast similarity scoring for embeddings.

---

### **5. Jaccard Similarity**

* **Definition:** Ratio of intersection over union between sets.
* **Range:** 0 to 1.
* **Formula:**
  
$$
  \text{Jaccard}(A,B)=\frac{|A\cap B|}{|A\cup B|}
$$

**Use case:** Compare sets of tokens/keywords — e.g., bag-of-words.

---

### **6. Soft-Cosine**

* **Definition:** Variation of cosine that accounts for similarity between features.
* **When useful:** When features (e.g., words) have known similarities.

**Use case:** Compare text where synonyms shouldn’t be treated as totally distinct.

---

### **7. Pearson Correlation**

* **Definition:** Measures linear correlation between vectors.
* **Range:** –1 to +1.

**Use case:** Time-series similarity, feature correlation analysis.

---

## 🧩 Choosing the Right Metric

| Task                                    | Metric                    |
| --------------------------------------- | ------------------------- |
| Semantic text similarity                | **Cosine similarity**     |
| Clustering vectors                      | **Euclidean / Manhattan** |
| Keyword set overlap                     | **Jaccard similarity**    |
| High-dimensional directional similarity | **Cosine or dot product** |
| Embeddings with normalization concern   | **Cosine**                |

---

## Why These Metrics Matter in GenAI

Generative models (like GPT, BERT, CLIP) output **embeddings** — compact vector representations of text or images. Similarity metrics quantify how “close” two embeddings are:

* **Semantic search:** Find documents most similar to a query.
* **Retrieval-augmented generation:** Score relevant data chunks.
* **Clustering & classification:** Group similar concepts.
* **Relevance ranking:** Rank generated responses/documents.

---

##  Practical Notes

### 🟢 Normalization

Some metrics (like cosine) assume vectors are normalized. If you’re using non-normalized vectors:

* Euclidean distances may be affected by magnitude.
* Normalizing to unit length often improves cosine accuracy.

### 🧩 Embedding Libraries

Most tools handle metric choices internally:

* **FAISS, Annoy, HNSWlib** (efficient vector search)
* **Sentence Transformers** (semantic text embeddings)
* **OpenAI embeddings** (Cosine & dot easily computed)

---

## Quick Summary

| Metric            | Orientation | Magnitude | Best For                  |
| ----------------- | ----------- | --------- | ------------------------- |
| Cosine similarity | ✔           | ✖         | Semantic similarity       |
| Euclidean         | ✖           | ✔         | Distance-based clustering |
| Manhattan         | ✖           | ✔         | Sparse differences        |
| Jaccard           | Set based   | N/A       | Token overlap             |

---
