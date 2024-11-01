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
# PROMPT = """Is this movie review sentiment positive or negative?

# This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since the year 1900."""

# # Print Claude's response
# print(get_completion(PROMPT))

# System prompt
# SYSTEM_PROMPT = "You are a savvy reader of movie reviews."

# # Prompt
# PROMPT = """Is this review sentiment positive or negative? First, write the best arguments for each side in  and  XML tags, then answer.

# This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since 1900."""

# # Print Claude's response
# print(get_completion(PROMPT, SYSTEM_PROMPT))

# Prompt
PROMPT = "Name a famous movie starring an actor who was born in the year 1956. First brainstorm about some actors and their birth years in  tags, then give your answer."

# Print Claude's response
print(get_completion(PROMPT))