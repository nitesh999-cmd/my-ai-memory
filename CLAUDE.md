# 🤖 Media Memory Protocol
You are equipped with a `/skills/media-memory` skill.

### 📥 Ingestion
Whenever the user uploads media (images, video, audio) to the `/media-memory` folder, you must:
1. Extract text/transcripts.
2. Generate a natural language description.
3. Call `media_memory.py` to embed and store it.

### 🔍 Retrieval
When a user asks about a past asset, query the ChromaDB instance.
*   Filter by: `type`, `date`, or `tags`.
*   Search by: Semantic similarity (e.g., "Find the image of the cat from last week").
