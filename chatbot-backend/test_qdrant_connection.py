import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not QDRANT_API_KEY:
    print("❌ QDRANT_API_KEY is missing!")
else:
    print(f"✅ QDRANT_API_KEY is loaded (length: {len(QDRANT_API_KEY)})")


try:
    print("🌐 Using QDRANT_URL:", QDRANT_URL)
    print("🌐 Using API KEY:", QDRANT_API_KEY)
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        port=80,
        prefer_grpc=False  # force REST mode
    )

    # Try listing collections as a health check
    collections = client.get_collections()
    print(f"✅ Connected to Qdrant at {QDRANT_URL}")
    print("📦 Existing collections:", collections.collections)

except Exception as e:
    import traceback
    print(f"❌ Failed to connect to Qdrant at {QDRANT_URL}")
    print("Error:", e)
    traceback.print_exc()

