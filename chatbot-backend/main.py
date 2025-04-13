from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from llm_router import get_llm
from retriever import get_vectorstore
from langchain.schema import Document
import uvicorn
import os

app = FastAPI()

# Allow frontend access via CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://localhost:3000"] for local dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional: log every request for debugging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"➡️ {request.method} {request.url}")
    return await call_next(request)

# Request model
class ChatTurn(BaseModel):
    role: str
    content: str

class ChatHistory(BaseModel):
    history: List[ChatTurn]

@app.post("/chat")
def chat(chat: ChatHistory):
    try:
        llm = get_llm()
        retriever = get_vectorstore().as_retriever(search_kwargs={"k": 5})

        # Get latest user message
        user_message = [m for m in chat.history if m.role == "user"][-1].content
        docs = retriever.get_relevant_documents(user_message)

        print("🔎 Qdrant Results:")
        for doc in docs:
            print("-", doc.page_content[:200])

        if not docs:
            docs = [Document(page_content="""
LifeSynergy offers small-group Magic Mushroom Retreats in Playa del Carmen, Mexico.
Upcoming retreat dates include:
- April 29 – May 3
- June 3 – 7
- July 1 – 5
- Nov 25 – 29, 2025.
Each retreat includes yoga, integration support, and 1-on-1 guidance.
""")]

        context = "\n".join([doc.page_content for doc in docs])
        system_message = {
            "role": "system",
            "content": f"You are the LifeSynergy Retreats assistant. Use only this context to answer questions:\n\n{context}"
        }

        full_history = [system_message] + [
            {"role": m.role, "content": m.content} for m in chat.history
        ]

        result = llm.invoke(full_history)
        return {"response": result.content}

    except Exception as e:
        print(f"❌ Error in /chat: {e}")
        raise HTTPException(status_code=500, detail="Sorry, something went wrong.")

# Only reload in local dev
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=os.getenv("ENV") == "dev")
