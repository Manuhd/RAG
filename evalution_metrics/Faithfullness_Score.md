

## **Faithfulness means the answer is trusted *only because it is supported by your data (context) for the given query*.**

✔️ **The LLM (or an evaluator LLM) gives this score**, not the user.

---

## Slight correction (important ⚠️)

❌ The **same LLM that generates the answer should NOT score itself**
✅ A **separate evaluator step (LLM-as-a-judge)** gives the faithfulness score

This avoids bias.

---

## How it works in a RAG system (step-by-step)

### 1️⃣ User asks a query

```
Query: What is the loan interest rate?
```

---

### 2️⃣ Retriever fetches context (your data)

```
Context:
"Loan interest rate is 8% for salaried employees."
```

---

### 3️⃣ Generator LLM produces answer

```
Answer:
"The loan interest rate is 8% and tenure is 20 years."
```

---

### 4️⃣ Evaluator LLM computes faithfulness ⭐

It does **NOT use its own knowledge**
It checks **answer vs context only**

* Extract claims from answer
* Verify each claim against context
* Compute score

$$
\text{Faithfulness} =
\frac{\text{Supported claims}}
{\text{Total claims}}
$$

Result:

```
Faithfulness = 0.5
```
Let’s calculate it **step by step**, very clearly 👍
This example is **perfect for understanding faithfulness**.

---

## Given

### **Context (your data)**

> “Loan interest rate is 8% for salaried employees.”

### **Answer**

> “The loan interest rate is 8% and tenure is 20 years.”

---

## Step 1️⃣ Break the answer into **claims**

A **claim = one factual statement**.

| Claim # | Claim text                   |
| ------- | ---------------------------- |
| 1       | Loan interest rate is **8%** |
| 2       | Loan tenure is **20 years**  |

➡️ **Total claims = 2**

---

## Step 2️⃣ Check each claim against the **context**

| Claim               | Present in context? | Supported? |
| ------------------- | ------------------- | ---------- |
| Interest rate is 8% | Yes                 | ✅          |
| Tenure is 20 years  | No                  | ❌          |

➡️ **Supported claims = 1**

---

## Step 3️⃣ Apply the faithfulness formula

$$
\text{Faithfulness} =
\frac{\text{Supported claims}}
{\text{Total claims}}
=====================

\frac{1}{2}
= 0.5
$$

---

## Final Result ✅

```
Faithfulness score = 0.5 (50%)
```

---

## Why this matters

* The model **partially used your data**
* It **added extra information** (tenure) not present in context
* That extra part is a **hallucination**

---

## Key interview one-liner ⭐

> “Faithfulness is calculated by decomposing the answer into atomic claims and checking how many of those claims are supported by the retrieved context.”

---

## Important note ⚠️

Even if **tenure = 20 years is true in real life**,
➡️ it is **not faithful**, because **your data did not say it**.

---

## Visual summary

```
Claims:       [8% interest] [20-year tenure]
Context has:  [8% interest]
Score:        1 / 2 = 0.5
```

---

If you want next, I can:

* Show **Python code** that does this automatically
* Show **RAGAS internals**
* Explain **edge cases** (implicit claims, paraphrases)

Just say 👍

---

## Who gives the faithfulness score?

| Component       | Role                    |
| --------------- | ----------------------- |
| Generator LLM   | Produces answer         |
| Evaluator LLM   | Scores faithfulness     |
| RAGAS / TruLens | Orchestrates evaluation |

✔️ The score is **automatic**

---

## Important distinction (interview favorite)

| Metric        | Meaning                        |
| ------------- | ------------------------------ |
| Faithfulness  | Answer is supported by context |
| Correctness   | Answer is factually correct    |
| Confidence    | How certain model sounds       |
| Hallucination | Unsupported claims             |

A response can be:

* **Correct but not faithful**
* **Faithful but incomplete**

---

## One-line ⭐

> “Faithfulness measures whether the LLM’s answer is grounded in the retrieved data for the query, and the score is computed automatically using an LLM-based evaluation step.”

---

## Production rule (best practice)

```text
If faithfulness < threshold → regenerate or block answer
```

Typical threshold:

* 0.8–0.9 for enterprise apps

---

## Final confirmation ✔️

- ✔️ Faithfulness = trust from **your data**
- ✔️ Score is given by **LLM-based evaluator**
- ✔️ Used mainly for **RAG / document QA**

---

