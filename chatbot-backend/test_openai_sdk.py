import os
from openai import OpenAI
from dotenv import load_dotenv
from openai.types.chat import ChatCompletion
from llm_router import get_llm

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key or api_key.startswith("sk-..."):
    raise ValueError("Please set your OPENAI_API_KEY environment variable or update the fallback key.")

# Create OpenAI client
client = OpenAI(api_key=api_key)

def test_basic_chat():
    """Test a basic chat completion."""
    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the retreat capital of the world?"}
        ]
    )
    print("Basic Chat Test Response:", response.choices[0].message.content)

def test_invalid_model():
    """Test with an invalid model to ensure error handling."""
    try:
        client.chat.completions.create(
            model="invalid-model",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "This should fail."}
            ]
        )
    except Exception as e:
        print("Invalid Model Test Passed:", str(e))

def test_long_prompt():
    """Test with a long user prompt."""
    long_prompt = "Tell me about retreats. " * 100
    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": long_prompt}
        ]
    )
    print("Long Prompt Test Response:", response.choices[0].message.content[:200], "...")

def test_missing_api_key():
    """Test behavior when API key is missing."""
    try:
        broken_client = OpenAI(api_key=None)
        broken_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "This should fail due to missing API key."}
            ]
        )
    except Exception as e:
        print("Missing API Key Test Passed:", str(e))

def test_openai():
    """Test OpenAI integration via llm_router."""
    llm = get_llm()
    response = llm.invoke("What is the retreat capital of the world?")
    print("OpenAI Test Response:", response)

def test_openai_via_llm_router():
    """Test OpenAI via LangChain get_llm router."""
    llm = get_llm()
    response = llm.invoke("What is the retreat capital of the world?")
    print("LLM Router Response:", response)


if __name__ == "__main__":
    print("Running OpenAI API Tests...")
    test_basic_chat()
    test_invalid_model()
    test_long_prompt()
    test_missing_api_key()
    test_openai()
    test_openai_via_llm_router()
