import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

try:
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )

    # Try listing collections as a health check
    collections = client.get_collections()
    print(f"✅ Connected to Qdrant at {QDRANT_URL}")
    print("📦 Existing collections:", collections.collections)

except Exception as e:
    print(f"❌ Failed to connect to Qdrant at {QDRANT_URL}")
    print("Error:", e)
