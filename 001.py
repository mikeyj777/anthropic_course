from data import API_KEY

MODEL_NAME = "claude-3-haiku-20240307"

import anthropic

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
