import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from openai import OpenAI
import uuid
from langchain.text_splitter import RecursiveCharacterTextSplitter



# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333"),
    api_key=os.getenv("QDRANT_API_KEY")  # Only needed for Qdrant Cloud
)

COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "lifesynergy-knowledge")

def chunk_documents(documents: List[str], chunk_size: int = 800, chunk_overlap: int = 100) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []
    for doc in documents:
        split = splitter.split_text(doc)
        chunks.extend(split)
    return chunks

def embed_documents(chunks: List[str]) -> List[List[float]]:
    embeddings = []
    for chunk in chunks:
        response = openai_client.embeddings.create(
            input=chunk,
            model="text-embedding-3-small"
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

def store_embeddings(embeddings: List[List[float]], chunks: List[str]):
    # Ensure collection exists
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )

    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"page_content": text, "source": "lifesynergy"}
        )
        for vector, text in zip(embeddings, chunks)
    ]

    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

if __name__ == "__main__":
    print("📄 Loading documents...")
    files = [f"docs/{f}" for f in os.listdir("docs") if f.endswith(".txt")]
    documents = []
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            documents.append(f.read())


    print("🔪 Chunking documents...")
    chunks = chunk_documents(documents)

    print("🧠 Embedding chunks...")
    embeddings = embed_documents(chunks)

    print("📦 Storing in Qdrant...")
    store_embeddings(embeddings, chunks)

    print(f"✅ Done! Embedded {len(chunks)} chunks into Qdrant collection '{COLLECTION_NAME}'.")
