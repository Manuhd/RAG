

## 🔹 L2 Distance (Euclidean Distance) — Formula

For two vectors

$$
\mathbf{x} = (x_1, x_2, \dots, x_n), \quad
\mathbf{y} = (y_1, y_2, \dots, y_n)
$$

### **L2 distance formula**

$$
\boxed{
d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
}
$$

This measures the **straight-line distance** between two points in n-dimensional space.

---

## 🔹 Simple 2D Example (step by step)

Let:

$$
\mathbf{x} = (1, 2), \quad \mathbf{y} = (4, 6)
$$

### Step 1: Subtract components

$$
(1 - 4) = -3,\quad (2 - 6) = -4
$$

### Step 2: Square them

$$
(-3)^2 = 9,\quad (-4)^2 = 16
$$

### Step 3: Sum

$$
9 + 16 = 25
$$

### Step 4: Square root

$$
\sqrt{25} = \boxed{5}
$$

✅ **L2 distance = 5**

---

## 🔹 3D Example (more realistic for embeddings)

Let:

$$
\mathbf{x} = (0.2, 0.4, 0.6), \quad
\mathbf{y} = (0.1, 0.3, 0.9)
$$

### Calculation

$$
\begin{aligned}
d &= \sqrt{(0.2-0.1)^2 + (0.4-0.3)^2 + (0.6-0.9)^2} \
&= \sqrt{(0.1)^2 + (0.1)^2 + (-0.3)^2} \
&= \sqrt{0.01 + 0.01 + 0.09} \
&= \sqrt{0.11} \
&\approx \boxed{0.332}
\end{aligned}
$$

---

## 🔹 Geometric intuition (very important)

![Image](https://upload.wikimedia.org/wikipedia/commons/5/55/Euclidean_distance_2d.svg?utm_source=chatgpt.com)


![Image](https://cdn1.byjus.com/wp-content/uploads/2021/12/euclidean-distance-formula-derivation.png?utm_source=chatgpt.com)

* L2 = **straight-line distance**
* Smaller distance → vectors are **more similar**
* Larger distance → vectors are **less similar**

---

## 🔹 How FAISS uses L2

* FAISS finds vectors with **minimum L2 distance**
* IVF uses L2:

  * During **clustering**
  * During **search inside clusters**

---

> “L2 distance measures the straight-line distance between two vectors. In FAISS, smaller L2 distance means higher similarity.”

---

## 🔹 Quick comparison (to remember)

| Metric   | Meaning      |
| -------- | ------------ |
| L2 ↓     | More similar |
| Cosine ↑ | More similar |

---
