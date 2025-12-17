### First You need to understand below topic before real real example.
- Euclidian Distance [Link](https://github.com/Manuhd/RAG/blob/main/evalution_metrics/Vector-search-system/Euclidean_Distance.md)
- FAISS [Link](https://github.com/Manuhd/RAG/blob/main/evalution_metrics/Vector-search-system/FAISS.md)
- IVF [Link](https://github.com/Manuhd/RAG/blob/main/evalution_metrics/Vector-search-system/With_IVF.md)


# How L2 Distance Works Inside IVF (with “What is EMI?” example)


## 1️⃣ Convert text to vectors (embeddings)

All text is first converted into **numerical vectors**.

### Query

**“What is EMI?”**

Embedding (example):

$$
Q = (0.20,\ 0.40,\ 0.60)
$$

### Documents stored in vector DB

| Doc | Text                                  | Vector             |
| --- | ------------------------------------- | ------------------ |
| D1  | EMI means Equated Monthly Installment | (0.18, 0.39, 0.61) |
| D2  | Interest rate calculation for loans   | (0.70, 0.10, 0.20) |
| D3  | How credit cards work                 | (0.90, 0.80, 0.10) |
| D4  | Loan repayment schedule               | (0.21, 0.42, 0.58) |

---

## 2️⃣ IVF training (one-time process)

### Step 1: Create clusters using K-means (L2 distance)

Assume IVF creates **2 clusters** (`nlist = 2`).

**Centroids learned:**

* **C1 (Loan / EMI related)**

 $$
  (0.20,\ 0.40,\ 0.60)
$$

* **C2 (Other finance topics)**

 $$
  (0.85,\ 0.75,\ 0.15)
 $$

---

### Step 2: Assign documents to nearest centroid (using L2)

Each document is assigned to the centroid with **minimum L2 distance**.

Result:

```
C1 → [D1, D4]
C2 → [D2, D3]
```

This mapping of **centroid → document list** is the **Inverted File**.

---

## 3️⃣ Query time with IVF + L2

### Step 3.1: Query vs centroids (L2 distance)

Compute L2 distance between query **Q** and each centroid.

#### Q → C1

$$
\sqrt{(0.20-0.20)^2 + (0.40-0.40)^2 + (0.60-0.60)^2} = 0
$$

#### Q → C2

$$
\sqrt{(0.20-0.85)^2 + (0.40-0.75)^2 + (0.60-0.15)^2} \approx 0.87
$$

Nearest centroid = **C1**

---

### Step 3.2: Probe selected clusters

Assume:

* `nprobe = 1`

Only **cluster C1** is searched.

---

### Step 3.3: Query vs documents inside C1 (L2 again)

#### Q → D1

$$
\sqrt{(0.20-0.18)^2 + (0.40-0.39)^2 + (0.60-0.61)^2}
\approx 0.024
$$

#### Q → D4

$$
\sqrt{(0.20-0.21)^2 + (0.40-0.42)^2 + (0.60-0.58)^2}
\approx 0.03
$$

---

## 4️⃣ Ranking result

Documents are ranked by **smallest L2 distance**:

| Doc | L2 Distance |
| --- | ----------- |
| D1  | **0.024**   |
| D4  | 0.030       |

D1 is the most relevant result.

---

## 5️⃣ What actually happened (combined view)

* **L2 distance** is used everywhere to measure similarity
* **IVF** reduces work by:

  * Searching centroids first
  * Searching only selected clusters
* Final similarity is still based on **L2 distance**

So IVF does **not replace similarity** — it **optimizes how similarity search is done**.

---

## 6️⃣ Final flow summary

```
Text → Embedding
     → L2 distance to centroids (IVF)
     → Select nearest clusters
     → L2 distance to vectors inside clusters
     → Return closest documents
```

---


## Let’s continue **the same single topic (L2 + IVF)** and change **only one thing**:

> **Assume `nprobe = 2`**

Everything else stays the same.

---

## IVF + L2 when `nprobe = 2` (with “What is EMI?”)

---

## 1️⃣ Clusters already created (from training)

We already have **2 clusters** (`nlist = 2`):

* **C1 (Loan / EMI related)**

  ```
  C1 → [D1, D4]
  ```
* **C2 (Other finance topics)**

  ```
  C2 → [D2, D3]
  ```

Centroids:

* C1 = (0.20, 0.40, 0.60)
* C2 = (0.85, 0.75, 0.15)

Query embedding:

$$
Q = (0.20,\ 0.40,\ 0.60)
$$

---

## 2️⃣ Query vs centroids (L2 distance)

| Centroid | L2 distance |
| -------- | ----------- |
| C1       | **0.00**    |
| C2       | **0.87**    |

Sorted by distance:

1. C1
2. C2

---

## 3️⃣ What `nprobe = 2` means

* FAISS will search the **top 2 nearest clusters**
* Here, that means:

  ```
  Search C1 AND C2
  ```

So **no cluster is skipped**.

---

## 4️⃣ Search inside both clusters (L2 distance again)

### Distances to all documents

#### C1 documents

* Q → D1 ≈ **0.024**
* Q → D4 ≈ **0.030**

#### C2 documents

* Q → D2 ≈ **0.707**
* Q → D3 ≈ **0.949**

---

## 5️⃣ Final ranking result

| Doc | L2 Distance |
| --- | ----------- |
| D1  | **0.024**   |
| D4  | 0.030       |
| D2  | 0.707       |
| D3  | 0.949       |

---

## 6️⃣ What changed compared to `nprobe = 1`

| Aspect            | nprobe = 1  | nprobe = 2          |
| ----------------- | ----------- | ------------------- |
| Clusters searched | Only C1     | C1 + C2             |
| Docs compared     | 2           | 4                   |
| Speed             | Faster      | Slightly slower     |
| Accuracy          | Approximate | Same as flat search |

With `nprobe = nlist`, IVF behaves like **full search**.

---

## 7️⃣ Key understanding

* `nprobe` controls **how many clusters are searched**
* Higher `nprobe`:

  * More comparisons
  * Better recall
* Lower `nprobe`:

  * Faster
  * Possible misses

---

## 8️⃣ Final mental model

```
nlist = total clusters
nprobe = clusters actually searched
```

* `nprobe = 1` → very fast, approximate
* `nprobe = nlist` → slow, exact-like

---


