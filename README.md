# RAG
RAG stands for Retrieval-Augmented Generation — it’s an AI architecture that combines information retrieval (fetching facts from external data sources) with text generation (using a large language model like GPT).

## 1. Retrieve

When you ask a question, the system searches a database, documents, or vector store (like Pinecone, FAISS, or Chroma) to find the most relevant pieces of text — often called context or knowledge snippets.

## 2. Augment

The retrieved data is added to your prompt, so the LLM sees this extra context before answering.

Example prompt to the model:
```
Context:
- Green tea contains antioxidants that help reduce inflammation.
- It may aid fat oxidation and improve metabolism.

Question:
What are the benefits of green tea?
```

## 3. Generate

The LLM (like GPT-5) then uses that retrieved context to generate a more accurate, factual, and grounded response.

## Common Use Cases

- Chatbots that answer from your company’s knowledge base

- Document Q&A (PDFs, WordPress posts, or research papers)

- Customer support assistants trained on internal manuals

- E-commerce assistants that answer using your product data

## Tech Stack Example

- A typical RAG pipeline might include:

- Embeddings model: text-embedding-3-small or sentence-transformers

- Vector store: Pinecone, FAISS, or Chroma

- Retriever: Searches by similarity

- LLM: GPT-5, Claude, or Gemini to generate the final answer


