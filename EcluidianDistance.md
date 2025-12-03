# Euclidean Distance works

We will calculate:

* **Distance(Q, A)**
* **Distance(Q, B)**
* **Distance(Q, C)**

Using:

$$
d(Q,D)=\sqrt{\sum (Q_i - D_i)^2}
$$

Your vectors:

```
Q = [0.11, 0.02, 0.90]
A = [0.06, 0.08, 0.90]
B = [0.10, 0.80, 0.90]
C = [0.03, 0.04, 0.50]
```

---

# ✅ **1️⃣ Euclidean Distance: Q ↔ A**

$$
d(Q,A)=\sqrt{(0.11-0.06)^2 + (0.02-0.08)^2 + (0.90-0.90)^2}
$$

= √(0.05² + (-0.06)² + 0²)
= √(0.0025 + 0.0036)
= √0.0061
= **0.0781**

👉 **Very close** (high similarity)

---

# ✅ **2️⃣ Euclidean Distance: Q ↔ B**

$$
d(Q,B)=\sqrt{(0.11-0.10)^2 + (0.02-0.8)^2 + (0.90-0.90)^2}
$$

= √(0.01² + (-0.78)² + 0²)
= √(0.0001 + 0.6084)
= √0.6085
= **0.7799**

👉 **Far** (low similarity)

---

# ✅ **3️⃣ Euclidean Distance: Q ↔ C**

$$
d(Q,C)=\sqrt{(0.11-0.03)^2 + (0.02-0.04)^2 + (0.90-0.50)^2}
$$

= √(0.08² + (-0.02)² + 0.40²)
= √(0.0064 + 0.0004 + 0.16)
= √0.1668
= **0.408**

👉 Somewhat far (medium similarity)

---

# ⭐ **Final Euclidean Ranking**

| Pair    | Distance  | Similarity Meaning        |
| ------- | --------- | ------------------------- |
| **Q–A** | **0.078** | 🥇 Closest → MOST similar |
| **Q–C** | **0.408** | 🥈 Medium similarity      |
| **Q–B** | **0.780** | 🥉 Least similar          |

---

# 🎯 **Which chunk would retriever pick using Euclidean Distance?**

If **K = 2**, retriever returns:

1️⃣ **A** (closest)
2️⃣ **C**

