import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

load_dotenv()

def get_llm():
    """Return the appropriate LLM client based on the LLM_PROVIDER env var."""
    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Missing OPENAI_API_KEY in .env")
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, api_key=api_key)
    
    elif provider == "ollama":
        model_name = os.getenv("OLLAMA_MODEL", "mistral")
        return ChatOllama(model=model_name)
    
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")
