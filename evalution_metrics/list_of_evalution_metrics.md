

# 🔹 1. Classification Metrics (ML / DL)

Assume:

* **TP** = True Positive
* **FP** = False Positive
* **TN** = True Negative
* **FN** = False Negative

---

## ✅ Accuracy

**What:** Overall correctness

**Formula:**  

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

**Example:**
- TP = 40, TN = 50, FP = 5, FN = 5  
- Accuracy = (40 + 50) / 100 = **0.90**

---

## ✅ Precision

**What:** How many predicted positives are correct

**Formula**
$$
Precision = \frac{TP}{TP + FP}
$$

**Example**

* TP=40, FP=10
  $$
  Precision = \frac{40}{50} = 0.8
  $$

---

## ✅ Recall (Sensitivity)

**What:** How many actual positives were found

**Formula**
[
Recall = \frac{TP}{TP + FN}
]

**Example**

* TP=40, FN=20
  [
  Recall = \frac{40}{60} = 0.67
  ]

---

## ✅ F1 Score

**What:** Balance between Precision & Recall

**Formula**
[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
]

**Example**

* Precision=0.8, Recall=0.67
  [
  F1 = 0.73
  ]

---

## ✅ Specificity

**What:** How well negatives are identified

**Formula**
[
Specificity = \frac{TN}{TN + FP}
]

---

# 🔹 2. Ranking & Retrieval Metrics (Search / RAG)

---

## ✅ Precision@k

**What:** Relevant docs in top-k results

**Formula**
[
Precision@k = \frac{\text{Relevant docs in top k}}{k}
]

**Example**

* Top 5 results → 3 relevant
  [
  P@5 = \frac{3}{5} = 0.6
  ]

---

## ✅ Recall@k

**What:** How many relevant docs were retrieved

**Formula**
[
Recall@k = \frac{\text{Relevant docs in top k}}{\text{Total relevant docs}}
]

**Example**

* 10 relevant docs exist, retrieved 4
  [
  Recall@k = 0.4
  ]

---

## ✅ Mean Reciprocal Rank (MRR)

**What:** How early the first correct result appears

**Formula**
[
MRR = \frac{1}{N}\sum \frac{1}{rank_i}
]

**Example**

* First relevant result at rank 2
  [
  MRR = \frac{1}{2} = 0.5
  ]

---

## ✅ Hit Rate

**What:** Whether at least one relevant doc is retrieved

**Formula**
[
Hit =
\begin{cases}
1 & \text{if relevant doc exists} \
0 & \text{otherwise}
\end{cases}
]

---

## ✅ nDCG (Normalized Discounted Cumulative Gain)

**What:** Ranking quality with graded relevance

**Formula**
[
DCG = \sum \frac{rel_i}{\log_2(i+1)}
]

[
nDCG = \frac{DCG}{IDCG}
]

**Used when:** relevance is not binary (high/medium/low)

---

# 🔹 3. RAG & LLM Evaluation Metrics (Very Important)

---

## ✅ Context Precision

**What:** Retrieved context relevance

**Formula**
[
Context\ Precision = \frac{\text{Relevant retrieved chunks}}{\text{Retrieved chunks}}
]

---

## ✅ Context Recall

**What:** Coverage of required context

**Formula**
[
Context\ Recall = \frac{\text{Relevant retrieved chunks}}{\text{Total relevant chunks}}
]

---

## ✅ Faithfulness (Groundedness)

**What:** Answer is supported by context

**Formula**
[
Faithfulness = \frac{\text{Supported claims}}{\text{Total claims}}
]

**Example**

* 4 statements, 3 supported
  [
  Faithfulness = 0.75
  ]

---

## ✅ Answer Correctness

**What:** Matches ground truth

**Formula**
[
Correctness = \frac{\text{Correct answers}}{\text{Total answers}}
]

---

## ✅ Hallucination Rate

**What:** Unsupported content

**Formula**
[
Hallucination\ Rate = 1 - Faithfulness
]

**Example**

* Faithfulness = 0.8
  [
  Hallucination = 0.2 \ (20%)
  ]

---

## ✅ Confidence Score

**What:** Model’s certainty

**Example**

* Token probability or self-reported confidence
  [
  Confidence = 0.85
  ]

---

# 🔹 4. Text Generation Metrics (NLP)

---

## ✅ BLEU

**What:** N-gram overlap (translation)

**Formula**
[
BLEU = BP \times \exp\left(\sum w_n \log p_n\right)
]

---

## ✅ ROUGE

**What:** Recall-based overlap (summarization)

* ROUGE-1 (unigram)
* ROUGE-2 (bigram)
* ROUGE-L (longest sequence)

---

## ✅ METEOR

**What:** Semantic similarity (better than BLEU)

---

## ✅ Perplexity

**What:** Model uncertainty

**Formula**
[
Perplexity = e^{Loss}
]

**Lower = better**

---

# 🔹 5. System / Business Metrics

---

## ✅ Latency

[
Latency = Response\ Time
]

---

## ✅ Throughput

[
Throughput = \frac{Requests}{Second}
]

---

## ✅ Cost per Query

[
Cost = Tokens \times Price
]

---

# 🔹 6. One-Line Interview Summary (Very Useful)

> **Retrieval metrics** check *finding data*,
> **Generation metrics** check *answer quality*,
> **Faithfulness & hallucination** ensure *trust*,
> **Latency & cost** ensure *production readiness*.

---

If you want, I can next:

* ✅ Give **RAGAS metrics mapping**
* ✅ Provide **Python code to compute all metrics**
* ✅ Create a **1-page interview cheat sheet**

Just tell me 👍
