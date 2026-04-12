import os
from chromadb import PersistentClient
import google.generativeai as genai

# 1. Setup
CHROMA_CLIENT = PersistentClient(path="./chroma_db")
collection = CHROMA_CLIENT.get_or_create_collection(name="media_vault")
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def ingest_media(file_path, file_type):
    # 2. Describe & Embed using Gemini 2
    # This turns an image/video into a "mathematical description"
    description = f"Media file: {file_path} of type {file_type}"
    embedding = genai.embed_content(model="models/embedding-001", content=description)
    
    # 3. Store in Vector DB
    collection.add(
        ids=[file_path],
        embeddings=[embedding['embedding']],
        metadatas=[{"type": file_type, "source": "github-upload"}]
    )
    print(f"✅ {file_path} stored in semantic memory.")
