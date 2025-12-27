# Dot Product works

Dot Product formula:

$$
Q \cdot D = \sum Q_i \times D_i
$$

### Document Embeddings stored in Vector DB
```

A = [0.06, 0.08, 0.90]
B = [0.10, 0.80, 0.90]
C = [0.03, 0.04, 0.50]
```
### Query Embedding
```
Q = [0.11, 0.02, 0.90]
```
---

## **1️⃣ Dot Product: Q · A**

$$
(0.11 \times 0.06) + (0.02 \times 0.08) + (0.90 \times 0.90)
$$

$$
= 0.0066 + 0.0016 + 0.81
$$

$$
= **0.8182**
$$

✔ **Q–A dot similarity = 0.8182**

---

## **2️⃣ Dot Product: Q · B**

$$
(0.11 \times 0.10) + (0.02 \times 0.80) + (0.90 \times 0.90)
$$

$$
= 0.011 + 0.016 + 0.81
$$

$$
= **0.837**
$$

✔ **Q–B dot similarity = 0.837**

---

## **3️⃣ Dot Product: Q · C**

$$
(0.11 \times 0.03) + (0.02 \times 0.04) + (0.90 \times 0.50)
$$

$$
= 0.0033 + 0.0008 + 0.45
$$

$$
= **0.4541**
$$

✔ **Q–C dot similarity = 0.4541**

---

## ⭐ **Dot Product Ranking**

| Pair    | Dot Product | Meaning               |
| ------- | ----------- | --------------------- |
| **Q–B** | **0.837**   | 🥇 Highest similarity |
| **Q–A** | **0.8182**  | 🥈 Very similar       |
| **Q–C** | **0.4541**  | 🥉 Least similar      |

---

> Dot Product measures how much two vectors “point in the same direction.”
> Higher value = more similar.
> Dot Product considers **magnitude**, unlike cosine.

---

## 🚀 Summary Across All 3 Metrics

| Metric                 | Best Match | Notes                             |
| ---------------------- | ---------- | --------------------------------- |
| **Cosine Similarity**  | C, A       | Measures angle (semantic meaning) |
| **Euclidean Distance** | A, C       | Measures closeness (distance)     |
| **Dot Product**        | B, A       | Measures magnitude × direction    |

