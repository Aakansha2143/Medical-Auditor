# debug_db.py
import os
from langchain_community.vectorstores import Chroma

print(" Step 1: Checking API Key...")
# Look for key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        import tomllib # Python 3.11+
        with open(".streamlit/secrets.toml", "rb") as f:
            secrets = tomllib.load(f)
            api_key = secrets.get("GROQ_API_KEY")
    except Exception:
        pass

if not api_key:
    print(" ERROR: GROQ_API_KEY is missing from environment and secrets.toml!")
    exit()
print(" API Key found.")

print("\n Step 2: Testing Embeddings Class...")
try:
    # Let's see if the import or initialization is what's freezing
    from langchain_groq import ChatGroq
    print("langchain_groq tools imported successfully.")
except Exception as e:
    print(f" ERROR importing models: {e}")
    exit()

print("\n🔄 Step 3: Checking if Chroma initialized or hung...")
try:
    # Let's test a simple, fast fallback embedding to see if Chroma works locally
    from langchain_community.embeddings import MockEmbeddings
    embeddings = MockEmbeddings(size=384)
    
    db = Chroma(
        collection_name="test_store",
        embedding_function=embeddings,
        persist_directory="test_chroma_db"
    )
    print("Chroma initialized instantly with mock embeddings.")
except Exception as e:
    print(f" ERROR initializing Chroma: {e}")