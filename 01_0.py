from data.data import API_KEY

MODEL_NAME = "claude-3-haiku-20240307"

# Import python's built-in regular expression library
import re
import anthropic

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


# System prompt
SYSTEM_PROMPT = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."

# Prompt
PROMPT = "Why is the sky blue?"

# # Print Claude's response
# ans = get_completion(PROMPT, SYSTEM_PROMPT)

# print(ans)

# Prompt - this is the only field you should change
PROMPT = "display the integers from 1 to 3 inclusive.  provide no other data but the numbers"

# Get Claude's response
# response = get_completion(PROMPT)

# # Function to grade exercise correctness
# def grade_exercise(text):
#     pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
#     return bool(pattern.match(text))

# # Print Claude's response and the corresponding grade
# print(response)
# print("\n--------------------------- GRADING ---------------------------")
# print("This exercise has been correctly solved:", grade_exercise(response))

SYSTEM_PROMPT = 'Your answers should emulate those of a 3 year old child'

# Prompt
PROMPT = "How big is the sky?"

# Get Claude's response
response = get_completion(PROMPT, SYSTEM_PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search(r"giggles", text) or re.search(r"soo", text))

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))

