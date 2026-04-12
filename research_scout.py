import os
import sys
from anthropic import Anthropic

# 1. Check if the key is actually there
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ ERROR: API Key is missing! Check your GitHub Secrets.")
    sys.exit(1)

try:
    client = Anthropic(api_key=api_key)
    
    # 2. Simple test call
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=100,
        messages=[{"role": "user", "content": "Search Reddit for one new AI tool today."}]
    )
    
    # 3. Save it
    with open("long-term-memory.md", "a") as f:
        f.write(f"\n- {response.content[0].text}\n")
    print("✅ Success! Findings saved.")

except Exception as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
