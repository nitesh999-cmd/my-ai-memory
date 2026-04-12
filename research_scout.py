import os
from anthropic import Anthropic
from datetime import datetime

# Setup
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MEMORY_FILE = "long-term-memory.md"

# The "Hunt" Instructions
prompt = "Search Reddit and Hacker News for new AI tools or updates. If found, list as: [DATE] | [URL] | [NOTE]. If nothing new, say 'No updates'."

# Ask Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=500,
    messages=[{"role": "user", "content": prompt}]
)

# Save the answer
with open(MEMORY_FILE, "a") as f:
    f.write(f"\n{response.content[0].text}\n")
