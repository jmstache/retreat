from llm_router import get_llm

def test_llm_router():
    """Test the LLM router for both OpenAI and Ollama."""
    llm = get_llm()
    response = llm.predict("What is the retreat capital of the world?")
    print("LLM Response:", response)

if __name__ == "__main__":
    test_llm_router()
