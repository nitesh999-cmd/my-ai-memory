import os
import sys
from anthropic import Anthropic  # ✅ Fixed: Added Anthropic here

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ API Key missing")
    sys.exit(1)

client = Anthropic(api_key=api_key)

# 1. Read the raw research notes
try:
    with open("long-term-memory.md", "r") as f:
        raw_notes = f.read()
except FileNotFoundError:
    raw_notes = "No notes found yet."

# 2. Ask Claude 4.6 to summarize
prompt = f"Review these research notes and create a high-level summary of the top 3 most important updates. Notes:\n{raw_notes}"

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{"role": "user", "content": prompt}]
)

# 3. Save summary and clear staging area
with open("project_updates.md", "a") as f:
    # ✅ Fixed: Added [0] to match the 2026 library version
    f.write(f"\n## Weekly Summary ({os.popen('date +%Y-%m-%d').read().strip()})\n{response.content[0].text}\n")

# Clear the old notes so next week starts fresh
with open("long-term-memory.md", "w") as f:
    f.write("# Long Term Memory\n")

print("✅ Weekly review complete. Summary saved to project_updates.md")
