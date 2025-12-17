# How Evaluation Metrics Are Calculated in This Project with Real Data Examples.

## 1️⃣ Sample Loan CSV (your knowledge base)

**loan_faq.csv**

| id | question                        | answer                                      |
| -- | ------------------------------- | ------------------------------------------- |
| 1  | What is the loan interest rate? | The loan interest rate is 8% per annum.     |
| 2  | What is the loan tenure?        | The loan tenure is 20 years.                |
| 3  | Is prepayment allowed?          | Yes, prepayment is allowed without penalty. |

This CSV is embedded and stored in a vector DB.

---

## 2️⃣ User Query

> **User:** *“What is the loan interest rate and tenure?”*

---

## 3️⃣ Retrieval Step (Vector Search)

### Retrieved documents (Top-2)

* Doc 1 → Interest rate (ID 1)
* Doc 2 → Tenure (ID 2)

Assume:

* Total relevant docs = 2
* Retrieved relevant docs = 2

### 🔹 Recall@2

$$
\text{Recall@2} = \frac{2}{2} = 1.0
$$

### 🔹 Precision@2

$$
\text{Precision@2} = \frac{2}{2} = 1.0
$$

---

## 4️⃣ LLM Generated Answer

> **Answer:**
> *“The loan interest rate is 8% and the tenure is 20 years.”*

---

## 5️⃣ Faithfulness Calculation (Important 🔥)

### Step 1: Break answer into claims

| Claim               | Supported by CSV? |
| ------------------- | ----------------- |
| Interest rate is 8% | ✅ Yes (Row 1)     |
| Tenure is 20 years  | ✅ Yes (Row 2)     |

### Step 2: Apply formula

$$
\text{Faithfulness} = \frac{\text{Supported Claims}}{\text{Total Claims}}
$$

$$
\text{Faithfulness} = \frac{2}{2} = 1.0
$$

---

## 6️⃣ Hallucination Metrics

### Hallucination Rate

$$
\text{Hallucination Rate} = 1 - 1.0 = 0
$$

### Hallucination Risk (%)

$$
\text{Hallucination Risk} = (1 - 1.0) \times 100 = 0%
$$

✅ **Perfect grounded answer**

---

## 7️⃣ Now a BAD Example (Very Important)

### LLM Answer:

> *“The loan interest rate is 8%, tenure is 20 years, and processing fee is 2%.”*

### Claims table

| Claim             | Supported?     |
| ----------------- | -------------- |
| Interest rate 8%  | ✅              |
| Tenure 20 years   | ✅              |
| Processing fee 2% | ❌ (Not in CSV) |

### Faithfulness

$$
\text{Faithfulness} = \frac{2}{3} = 0.67
$$

### Hallucination Risk

$$
(1 - 0.67) \times 100 = 33%
$$

🚨 **This is hallucination**

---

## 8️⃣ Token Cost Example (Per Query)

Assume:

* Prompt tokens = 120
* Context tokens = 180
* Output tokens = 40

### Total Tokens

$$
120 + 180 + 40 = 340
$$

### Cost (Gemini example: $0.001 / 1K tokens)

$$
\frac{340}{1000} \times 0.001 = $0.00034
$$

---

## 9️⃣  One-Line Explanation

> “I split the LLM answer into factual claims, verify each claim against retrieved CSV context, compute faithfulness as supported claims over total claims, and derive hallucination risk from that.”


---



---
