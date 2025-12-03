### **Sample vector calculations based on the exact values in diagram**.


### **Document Embeddings stored in Vector DB**

```
A = [0.06, 0.08, 0.9]
B = [0.10, 0.8, 0.9]
C = [0.03, 0.04, 0.5]
```

### **Query Embedding**

```
Q = [0.11, 0.02, 0.90]
```

Now let’s calculate cosine similarity between Q and each document vector.

Formula:

$$
\text{similarity}(Q,D) = \frac{Q \cdot D}{\|Q\|\|D\|}
$$


---

# ✅ **1️⃣ Similarity(Q, A)**

### Step 1: Dot product

$$
Q \cdot A = (0.11×0.06) + (0.02×0.08) + (0.90×0.9)
$$

=
0.0066 + 0.0016 + 0.81
= **0.8182**

### Step 2: Norms

$$
\|Q\| = \sqrt{0.11^2 + 0.02^2 + 0.9^2}
$$

= √(0.0121 + 0.0004 + 0.81)  
= √0.8225  
= **0.907**

$$
\|A\| = \sqrt{0.06^2 + 0.08^2 + 0.9^2}
$$

= √(0.0036 + 0.0064 + 0.81)  
= √0.82  
= **0.905**

### Step 3: Cosine similarity

$$
\frac{0.8182}{0.907 × 0.905}
$$

= 0.8182 / 0.821
= **0.997**

✔ **Q–A similarity = 0.997**

---

# ✅ **2️⃣ Similarity(Q, B)**

### Similarity(Q, B)

**Dot product**

Q ⋅ B = (0.11 × 0.10) + (0.02 × 0.8) + (0.90 × 0.9)  
= 0.011 + 0.016 + 0.81  
= **0.837**

**Norm of B**

$$
\|B\| = \sqrt{0.10^2 + 0.8^2 + 0.9^2}
$$

= √(0.01 + 0.64 + 0.81)  
= √1.46  
= **1.208**

**Cosine similarity**

$$
\text{similarity}(Q,B)=\frac{0.837}{0.907 \times 1.208}
$$

= 0.837 / 1.095  
= **0.764**

✔ Q–B similarity = **0.764**


---

### ✅ 3️⃣ Similarity(Q, C)

**Dot product**

Q ⋅ C = (0.11 × 0.03) + (0.02 × 0.04) + (0.90 × 0.5)  
= 0.0033 + 0.0008 + 0.45  
= **0.4541**

**Norm of C**

$$
\|C\| = \sqrt{0.03^2 + 0.04^2 + 0.5^2}
$$

= √(0.0009 + 0.0016 + 0.25)  
= √0.2525  
= **0.502**

**Cosine similarity**

$$
\text{similarity}(Q,C)=\frac{0.4541}{0.907 \times 0.502}
$$

= 0.4541 / 0.455  
= **0.998**

✔ Q–C similarity = **0.998**

---

# ⭐ FINAL RESULT (Ranking)

| Document | Similarity | Rank |
| -------- | ---------- | ---- |
| **C**    | **0.998**  | 🥇 1 |
| **A**    | **0.997**  | 🥈 2 |
| **B**    | **0.764**  | 🥉 3 |

---

# 🎯 **Top-K Retrieved Docs (K = 2)**

1️⃣ C
2️⃣ A

These two chunks are sent to the LLM.

---

