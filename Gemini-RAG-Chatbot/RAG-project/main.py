from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import shutil
import google.generativeai as genai
from rag import extract_pdf_text, chunk_text, store_document, retrieve
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Serve static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# -------------------------
# Upload PDF & store in DB
# -------------------------
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile):
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_pdf_text(path)
    chunks = chunk_text(text)
    store_document(chunks)

    return {"message": "PDF uploaded and processed."}

# -------------------------
# Ask question (RAG)
# -------------------------
@app.get("/ask")
async def ask_question(q: str):
    context_chunks = retrieve(q)
    context = "\n".join(context_chunks)

    prompt = f"""
    You are a helpful assistant. Use the given context to answer the question.
    If the user asks in Kannada, reply in Kannada.
    If the user asks for translation, explain or translate using the same context.
    Never create new facts outside the provided context.

    Context:
    {context}

    Question:
    {q}

    Answer:
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return {"answer": response.text}
