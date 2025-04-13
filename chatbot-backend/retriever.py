import os
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from langchain_qdrant import Qdrant
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings

from llm_router import get_llm

# Optional import (only if needed)
from langchain_openai import OpenAIEmbeddings
# Future: from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "lifesynergy-knowledge")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")


# Step 1: Load vectorstore
def get_vectorstore():
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    if LLM_PROVIDER == "openai":
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        return Qdrant(client=client, collection_name=QDRANT_COLLECTION, embeddings=embeddings)

    elif LLM_PROVIDER == "ollama":
        OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=OLLAMA_BASE_URL)
        return Qdrant(
            client=client,
            collection_name=QDRANT_COLLECTION,
            embeddings=embeddings,
        )

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")

# Step 2: System prompt
system_message = """
You are the retreat assistant for LifeSynergy Retreats — a sacred, supportive space for inner healing through magic mushroom retreats, yoga, and integration in Playa del Carmen, Mexico.

Speak with calm, care, and clarity. Always be concise and centered — like someone who listens deeply and speaks simply.

Your purpose is to:
1. Answer questions clearly using only the provided context.
2. Invite people to book a discovery call when they’re ready.
3. Gently ask for name, email, and anything they'd like to share (intentions, medication, mental health history, ideal dates).
4. Reassure them their information is safe and confidential.
5. Never make up info — use only the context provided.

Always respond as a grounded, kind retreat guide. Never say “I’m just an AI” or talk about being a chatbot.

If lead details are shared, respond normally but include:
---
lead:
  name: ...
  email: ...
  phone: ...
  retreat_interest: ...
  notes: ...
---
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("user", "Context:\n{context}\n\nQuestion:\n{question}")
])


# Step 3: Setup chain
def get_qa_chain():
    retriever = get_vectorstore().as_retriever(
        search_kwargs={"k": 5, "score_threshold": 0.3}
    )
    llm = get_llm()

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )


# Step 4: Query
def query_retreat_agent(question: str):
    qa = get_qa_chain()
    result = qa.invoke({"query": question})

    print("🔎 Retrieved context:")
    for doc in result["source_documents"]:
        print("-", doc.page_content[:250].replace("\n", " "), "...\n")

    return result["result"]
