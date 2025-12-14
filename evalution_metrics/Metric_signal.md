## 🔹 1. Retrieval Strategy (Very Important)

Even with good data, **bad retrieval = bad answers**.

**Improve**

* Embedding model quality
* Chunk size & overlap
* Metadata filtering (date, category, source)
* Hybrid search (vector + keyword)

**Metric signal**

* Low Recall@k
* Low MRR

---

## 🔹 2. Reranking (High Impact, Low Cost)

A reranker ensures **best chunks reach the LLM**.

**Improve**

* Cross-encoder reranker
* Limit context to top-N high-quality chunks

**Metric signal**

* Precision@k improves
* Faithfulness improves

---

## 🔹 3. Chunking & Document Structure

Poor chunking hides answers.

**Improve**

* Semantic chunking
* Table-aware chunking
* Preserve headings & hierarchy

**Metric signal**

* Context recall improves

---

## 🔹 4. Query Understanding & Rewriting

Users don’t ask perfect questions.

**Improve**

* Query normalization
* Query expansion
* Rewrite vague questions

**Metric signal**

* Retrieval metrics improve for ambiguous queries

---

## 🔹 5. Guardrails & Answer Control

Prevent confident wrong answers.

**Improve**

* “Not found” fallback
* Minimum faithfulness threshold
* Answer refusal when context is weak

**Metric signal**

* Hallucination rate drops

---

## 🔹 6. Evaluation & Feedback Loop (Ongoing)

Evaluation is **not one-time**.

**Improve**

* Continuous metric tracking
* Real user feedback
* Error categorization

**Metric signal**

* Gradual score improvement over time

---

## 🔹 7. Model Choice & Routing

Not every query needs the same model.

**Improve**

* Route simple queries to cheap models
* Complex queries to stronger models

**Metric signal**

* Cost drops without accuracy loss

---

## 🔹 8. Latency & Cost Optimization

Accuracy alone is not enough in production.

**Improve**

* Caching frequent queries
* Token limits
* Streaming responses

**Metric signal**

* Lower latency & cost per query

---

## 🔹 9. Security & Data Safety

Critical for enterprise systems.

**Improve**

* PII masking
* Access control
* Source attribution

---

## 🎯 Summary

> **“Beyond data, prompt, and model parameters, we must also improve retrieval quality, reranking, chunking, query understanding, guardrails, continuous evaluation, model routing, and cost-latency optimization to build a reliable LLM system.”**

---

## 🔑 Ultimate Takeaway

> **LLM accuracy is a system problem, not a model problem.**

---


