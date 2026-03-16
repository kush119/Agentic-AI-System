import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from mcp/.env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)


def get_llm_client():
    """
    Returns a configured Azure OpenAI client.
    """
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
    )


# ✅ MUST be a string, not a function
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")