import re
from model import MODEL_NAME, client

def get_completion(prompt: str, system_prompt="", prefill=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt},
          {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text

# Prompt
PROMPT = "Who is the heaviest hippo of all time? Only answer if you know the answer with certainty."

# Print Claude's response
print(get_completion(PROMPT))