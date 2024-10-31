import re
import anthropic


from data.data import API_KEY

MODEL_NAME = "claude-3-haiku-20240307"

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

# # Prompt
# PROMPT = "In one sentence, what do you think about skateboarding?"

# # Print Claude's response
# print(f'not a cat: {get_completion(PROMPT)}')


# # System prompt
# SYSTEM_PROMPT = "You are a cat."

# # Prompt
# PROMPT = "In one sentence, what do you think about skateboarding?"

# # Print Claude's response
# print(f'Is a cat:  {get_completion(PROMPT, SYSTEM_PROMPT)}')

# System prompt - if you don't want to use a system prompt, you can leave this variable set to an empty string
SYSTEM_PROMPT = "you are a math professor, methodically grading papers.  go through each step and confirm that the answer is correct."

# Prompt
PROMPT = """Is this equation solved correctly below?

2x - 3 = 9
2x = 6
x = 3"""

# Get Claude's response
response = get_completion(PROMPT, SYSTEM_PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    if "incorrect" in text or "not correct" in text.lower():
        return True
    else:
        return False

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
