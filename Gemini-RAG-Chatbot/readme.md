# 📘 PROJECT: Gemini RAG Chatbot (FastAPI + Chroma + ChatGPT-Style UI)

This project is a full RAG (Retrieval-Augmented Generation) system using:

- ✅ Python (FastAPI backend)
- ✅ Gemini LLM (Google Generative AI)
- ✅ Chroma Vector Database
- ✅ PDF Upload & Embeddings
- ✅ ChatGPT-style UI (HTML + JS)
- ✅ Voice Input + File Upload


## 🎯 What This Project Does

This AI chatbot can:

✅ Read and process PDF resumes, policies, manuals, documents

✅ Store and retrieve embeddings using Chroma DB

✅ Answer questions based on the uploaded PDF (RAG)

✅ Support voice input (speech-to-text)




### Demo
![alt text](https://github.com/Manuhd/RAG/blob/main/Gemini-RAG-Chatbot/RAG-project/RAG.PNG)

## 📁 FILE STRUCTURE

```
rag-gemini/
│── main.py                  # FastAPI backend (API routes)
│── rag.py                   # PDF extract, chunking, retrieval logic
│── embeddings.py            # Gemini embedding model
│── requirements.txt         # Python dependencies
│── .env                     # GEMINI_API_KEY
│── data/                    # Uploaded PDF storage
│── vectorstore/             # Chroma vector DB storage
│── static/
│     └── index.html         # ChatGPT-style UI (frontend)
```
## 📌 REQUIREMENTS
✅ Software

Python 3.9+

pip

FastAPI

Uvicorn (server)

ChromaDB

Google Generative AI Python SDK

✅ Python Libraries (requirements.txt)
```
fastapi
uvicorn
chromadb
PyPDF2
google-generativeai
python-dotenv
```
## 🔧 INSTALLATION & SETUP
### 1️⃣ Clone the Project
```
git clone https://github.com/your-username/rag-gemini.git
cd rag-gemini
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Add Gemini API Key

Create .env
```
GEMINI_API_KEY=your_google_api_key
```
### 4️⃣ Create Necessary Folders
```
mkdir data
mkdir vectorstore
mkdir static
```

Place the index.html UI file inside /static.

## 🧠 BACKEND COMPONENTS
1. embeddings.py

Handles Gemini embeddings.
```
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding(text: str):
    model = "models/text-embedding-004"
    result = genai.embed_content(model=model, content=text)
    return result['embedding']
```
✅ 2. rag.py

Handles PDF processing, chunking, and Chroma DB retrieval.

✅ Extract PDF
✅ Chunk text
✅ Store embeddings
✅ Retrieve relevant chunks

✅ 3. main.py

FastAPI server with:

✅ /upload_pdf → Upload + Process PDF
✅ /ask → Ask questions with RAG
✅ Serves frontend /static/index.html

## 🌐 RUNNING THE PROJECT

Start FastAPI:
```
uvicorn main:app --reload
```

Open your browser:
```
http://127.0.0.1:8000/static/index.html
```
## 📌 API ROUTES
### 1. Upload PDF
```
POST /upload_pdf
```
Body: multipart/form-data

Key	Value
file	PDF file

Response:
```
{
  "message": "PDF uploaded and processed."
}
```

2. Ask Question

GET /ask?q=Your question

Returns:

{
  "answer": "AI response based on the PDF context"
}

### 💡 FEATURES INCLUDED

✅ ChatGPT-style UI
✅ Dark mode
✅ Left sidebar chat history
✅ Right-aligned user messages
✅ Left-aligned bot messages
✅ Animated typing dots
✅ Live voice recording animation
✅ Upload PDFs / Images / Docs
✅ Extract PDF + Chunking + Embeddings
✅ Chroma Vector DB storage
✅ Gemini LLM answer generation
✅ Kannada & English support
✅ User-friendly interactions
