# RAG

## What is RAG (Retrieval-Augmented Generation)?

RAG (Retrieval-Augmented Generation) is a technique where an LLM answers questions using your own data, not only its internal knowledge.

RAG = Search + AI

- ✅ First retrieves relevant documents
- ✅ Then generates an answer using those documents

This avoids hallucinations and makes answers accurate.

![alt-text](https://github.com/Manuhd/RAG/blob/main/rag%20diagram.png)
### Why RAG is used?

Because LLMs:
- ❌ Don’t know your private data
- ❌ Forget updated information
- ❌ Can hallucinate

RAG solves these by connecting LLMs to:
- ✅ PDFs
- ✅ Databases
- ✅ Websites
- ✅ Internal documents
- ✅ Company knowledge bases

###  RAG Architecture (Simple)
  ```  
                 ┌──────────────────────────────────┐
                 │            USER QUERY            │
                 │                                  │
                 └──────────────────────────────────┘
                                 │
                                 ▼
                     (1) EMBED THE QUERY
                                 │
                                 ▼
         ┌───────────────────────────────────────────────┐
         │               VECTOR DATABASE                 │
         │   (Stores embeddings of all documents/chunks) │
         └───────────────────────────────────────────────┘
                                 ▲
                                 │
                     (2) EMBEDDINGS STORED HERE
                                 │
                                 ▼
    ┌──────────────────────────────────────────────────────────┐
    │                    RETRIEVAL PROCESS                     │
    │  - Query embedding compared with stored vectors using    │
    │    cosine similarity / dot product / Euclidean           │
    │  - Find Top-K most relevant chunks                       │
    └──────────────────────────────────────────────────────────┘
                                 │
                                 ▼
          ┌─────────────────────────────────────────────────┐
          │             TOP-K RELEVANT CHUNKS               │
          │   (Policies, FAQs, loan rules, documents…)      │
          └─────────────────────────────────────────────────┘
                                 │
                     (3) PASS CONTEXT TO LLM
                                 │
                                 ▼
        ┌────────────────────────────────────────────────────────┐
        │                 LLM (GPT/Gemini/Claude)                │
        │  - Reads user query + retrieved chunks                 │
        │  - Generates grounded, accurate answer                 │
        └────────────────────────────────────────────────────────┘
                                 │
                                 ▼
              ┌────────────────────────────────────┐
              │            FINAL ANSWER            │
              │   “Your loan eligibility depends…” │
              └────────────────────────────────────┘
```
## Core Components of RAG
#### 1️⃣ Document Loader

Load PDFs, text, websites, DB data.

#### 2️⃣ Text Splitter

Split into embeddings-friendly chunks.

#### 3️⃣ Embeddings

Convert text → vectors.

#### 4️⃣ Vector Store

FAISS, Pinecone, Chroma, Weaviate.

#### 5️⃣ Retriever

Find top-k similar documents.

#### 6️⃣ LLM

Generate answer using retrieved context.

## Small RAG Example (Very Easy Python Code)

### ✅ Step 1: Load documents
```
from langchain_community.document_loaders import TextLoader

loader = TextLoader("company_policy.txt")
docs = loader.load()
```
### ✅ Step 2: Split text
```
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)
```
### ✅ Step 3: Create embeddings + vector store
```
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)
```
### ✅ Step 4: Build retriever
```
retriever = vectorstore.as_retriever()
```
### ✅ Step 5: LLM + Retrieval Chain
```
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4o-mini")

rag = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

print(rag.invoke("What is our leave policy?"))
```

- ✅ This is a fully working RAG system
- ✅ Loads your documents → embeds → retrieves → answers

## One-line 

“RAG retrieves relevant documents from a knowledge base and then uses an LLM to generate accurate, factual answers based on that retrieved context.”

RAG (Retrieval-Augmented Generation) combines information retrieval with LLM generation. It first searches for relevant documents (retrieval) and then uses an LLM to produce an answer based on those documents. This improves accuracy, reduces hallucinations, and allows AI to use your private or enterprise data.
