
# GenAI RAG Chatbot with Evaluation Metrics & Dashboard

This project demonstrates a **Retrieval-Augmented Generation (RAG)** chatbot built using **Python and Gemini LLM**, along with a **complete evaluation framework** to measure response quality, hallucination risk, and system reliability.

The system is designed to reflect **real-world enterprise GenAI practices**, especially for **banking / regulated domains**.



##  Features

- Retrieval-Augmented Question Answering (RAG)
- Grounded answer generation using Gemini LLM
- Automatic intent handling for ambiguous questions
- Strict hallucination control
- Per-response and system-level evaluation metrics
- Metrics logging to CSV
- Manager-friendly Streamlit dashboard



##  Architecture Overview

```

User Question
↓
Retriever (Top-k from CSV using embeddings)
↓
Context Construction
↓
Gemini LLM (Grounded Prompt)
↓
Answer
↓
Evaluation Metrics
↓
Metrics Logging (CSV)
↓
Dashboard (Streamlit)

```

##  Project Structure


```
GEN AI Projects/
│
├── data/
│   └── loan_faq.csv
│
├── ingest.py                 # CSV ingestion & embedding creation
├── retrieve.py               # Top-k retrieval logic
├── ask_gemini.py             # Grounded answer generation
├── evaluate.py               # Metrics calculation
├── ground_truth.py           # true_id mapping from CSV
├── metrics_logger.py         # Logs metrics to CSV
├── plot_metrics.py           # Optional metric visualization
├── main.py                   # Run chatbot + evaluation
├── dashboard.py              # Streamlit dashboard
├── metrics_log.csv           # Logged evaluation data
└── README.md

```

---

## 📊 Evaluation Metrics

The system evaluates each response using the following metrics:

### 🔹 Retrieval Metric
- **Recall@k** – Checks whether the correct answer (`true_id`) appears in the top-k retrieved results.

### 🔹 Answer Quality Metrics
- **Accuracy** – Whether the generated answer matches the expected meaning.
- **Correctness** – Direct comparison with ground-truth answer.
- **Faithfulness** – Degree to which the answer is grounded in retrieved context (0–1).

### 🔹 Hallucination Metrics
- **Hallucination (Binary)** – Whether the answer contains unsupported information.
- **Hallucination Risk (%)** – Calculated as:

```

Hallucination Risk = (1 - Faithfulness) × 100

```

### 🔹 Confidence Score
- Combined score derived from correctness, faithfulness, hallucination, and recall.

---

## 📈 Metrics Interpretation (Enterprise Standard)

| Metric | Target |
|------|-------|
| Faithfulness | ≥ 90% |
| Hallucination Risk | ≤ 5% |
| Hallucination Rate | ≤ 3–5% |
| Confidence Score | ≥ 85% |

---

##  Example Output

```

Enter your question: What documents are required for loan?

--- Per Question ---
Answer: ID proof, address proof, income proof.
Recall@3: 100%
Accuracy: 100%
Correctness: 100%
Faithfulness: 95%
Hallucination Risk: 5%
Confidence Score: 92%

````

---

##  Streamlit Dashboard

Run the dashboard using:

```bash
streamlit run dashboard.py
````

Dashboard displays:

* Average Confidence
* Faithfulness %
* Hallucination Rate %
* Hallucination Risk Distribution
* Logged Q&A history

---

##  Key Design Decisions

* **Extractive / Grounded Prompting** to prevent hallucinations
* **Strict refusal handling** for out-of-domain queries
* **Faithfulness-driven hallucination detection**
* **CSV-based logging** for auditability
* **Percentage-based metrics** for stakeholder readability

---

##  Real-World Relevance

This project mirrors how **enterprise GenAI systems** are built and evaluated in:

* Banking
* Finance
* Healthcare
* Regulated AI environments

It demonstrates **production thinking**, not just model usage.

---


## 🛠️ Tech Stack

* Python
* Gemini LLM (Google Generative AI)
* Pandas, NumPy
* Streamlit
* CSV-based evaluation logging

---

## 📌 Future Enhancements

* Batch evaluation on test sets
* Threshold-based auto-refusal
* Schema versioning for logs
* Alerting on hallucination spikes
* Confidence-based retry logic

---

## 👨‍💻 Author

Built as a **hands-on GenAI engineering project** focused on **real-world applicability and safety**.

---

