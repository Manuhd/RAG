# Minimal RAG API (Single Library)

This is a **lightweight Retrieval-Augmented Generation (RAG) API** using only **scikit-learn**.  
It allows you to ask questions against a small knowledge base and returns the most relevant document.  

- **No PyTorch required**  
- **Fully offline**  
- **Single library** (`scikit-learn`)  

---

## Features

- Retrieve top matching documents based on TF-IDF similarity  
- Fast and lightweight  
- Expose a simple HTTP API using **FastAPI**  
- Configurable `top_k` results  

---

## Installation

1. **Clone the repository** or copy project files to a folder.

2. **Create a virtual environment** (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

## Install dependencies:

```
pip install fastapi uvicorn scikit-learn
```

### Project Structure
```
RAG/
│
├─ app.py          # FastAPI application
├─ README.md       # Project documentation
└─ .venv/          # Virtual environment
```
## Usage

Run the API
```
uvicorn app:app --reload
```

The API will run at http://127.0.0.1:8000

Interactive API docs: http://127.0.0.1:8000/docs

Send a POST request to /ask:
```
{
    "question": "What does RAG stand for?",
    "top_k": 1
}
```

Sample Response
```
{
    "answer": "RAG stands for Retrieval-Augmented Generation."
}
```

## How it Works

- Documents are vectorized using TF-IDF

- Queries are transformed into vectors

- Cosine similarity finds the closest matching document(s)

- Returns the top k results

## Notes

- You can modify docs in app.py to add your own knowledge base

- Fully offline; no API key or internet required

- Works on Windows, Mac, Linux

License

MIT License


--
