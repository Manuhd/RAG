# Euclidean Distance works


Formula:

$$
d(Q,D)=\sqrt{\sum (Q_i - D_i)^2}
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
We will calculate:

* **Distance(Q, A)**
* **Distance(Q, B)**
* **Distance(Q, C)**

## **1️⃣ Euclidean Distance: Q ↔ A**

$$
d(Q,A)=\sqrt{(0.11-0.06)^2 + (0.02-0.08)^2 + (0.90-0.90)^2}
$$

$$
= \sqrt{(0.05² + (-0.06)² + 0²)}
$$

$$
= \sqrt{(0.0025 + 0.0036)}
$$

$$
= \sqrt{0.0061}
$$

$$
= **0.0781**
$$

👉 **0.0781** - **Very close** (high similarity)

---

## **2️⃣ Euclidean Distance: Q ↔ B**

$$
d(Q,B)=\sqrt{(0.11-0.10)^2 + (0.02-0.8)^2 + (0.90-0.90)^2}
$$

$$
= \sqrt{(0.01² + (-0.78)² + 0²)}
$$

$$
= \sqrt{(0.0001 + 0.6084)}
$$

$$
= \sqrt{0.6085}
$$

$$
**0.7799**
$$

👉 **0.7799** - **Far** (low similarity)

---

## **3️⃣ Euclidean Distance: Q ↔ C**

$$
d(Q,C)=\sqrt{(0.11-0.03)^2 + (0.02-0.04)^2 + (0.90-0.50)^2}
$$

$$
= \sqrt{(0.08² + (-0.02)² + 0.40²)}
$$

$$
= \sqrt{(0.0064 + 0.0004 + 0.16)}
$$

$$
= \sqrt{0.1668}
$$

$$
**0.408**
$$

👉 **0.408** - Somewhat far (medium similarity)

---

## ⭐ **Final Euclidean Ranking**

| Pair    | Distance  | Similarity Meaning        |
| ------- | --------- | ------------------------- |
| **Q–A** | **0.078** | 🥇 Closest → MOST similar |
| **Q–C** | **0.408** | 🥈 Medium similarity      |
| **Q–B** | **0.780** | 🥉 Least similar          |

---

### 🎯 **Which chunk would retriever pick using Euclidean Distance?**

If **K = 2**, retriever returns:

- 1️⃣ **A** (closest)
- 2️⃣ **C**
---


##  Convert **distance → similarity** 

### formula:

$$
\text{similarity} = \frac{1}{1 + \text{distance}}
$$

### How each was calculated

* **Q–A**
  
$$
  \frac{1} {(1 + 0.078)} \approx 0.928
$$

* **Q–C**

$$
  \frac{1} {(1 + 0.408)} \approx 0.710
$$

* **Q–B**

$$
  \frac{1} {(1 + 0.780)} \approx 0.562
$$

---

### Converted values

| Pair    |  Distance | Similarity | Meaning                   |
| ------- | --------: | ---------: | ------------------------- |
| **Q–A** | **0.078** |  **0.928** | 🥇 Closest → MOST similar |
| **Q–C** | **0.408** |  **0.710** | 🥈 Medium similarity      |
| **Q–B** | **0.780** |  **0.562** | 🥉 Least similar          |

---

## Key takeaway

> “By converting distance to similarity using `1 / (1 + distance)`, we normalize scores to a 0–1 range where higher values mean more similar.”


## Python code

```
import math

labels = ["A", "B", "C"]
db = [
    [0.06, 0.08, 0.9],   # A
    [0.10, 0.8, 0.9],    # B
    [0.03, 0.04, 0.5]    # C
]

q = [0.11, 0.02, 0.90]

def euclidean_distance(vec1, vec2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))

for label, vec in zip(labels, db):
    dist = euclidean_distance(q, vec)
    print(f"Distance between (Q, {label}) = {dist}")

```
## Distance + similarity
```
import math

labels = ["A", "B", "C"]
db = [
    [0.06, 0.08, 0.9],   # A
    [0.10, 0.8, 0.9],    # B
    [0.03, 0.04, 0.5]    # C
]

q = [0.11, 0.02, 0.90]

def euclidean_distance(vec1, vec2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))

for label, vec in zip(labels, db):
    dist = euclidean_distance(q, vec)
    similarity = 1 / (1 + dist)
    print(
        f"Distance between (Q, {label}) = {dist:.3f}, "
        f"Similarity = {similarity:.3f}"
    )

```
