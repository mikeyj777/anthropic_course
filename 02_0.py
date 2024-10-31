import re
import anthropic

from data.data import API_KEY

MODEL_NAME = "claude-3-haiku-20240307"

# Retrieve the API_KEY & MODEL_NAME variables from the IPython store

client = anthropic.Anthropic(api_key=API_KEY)

# Note that we changed max_tokens to 4K just for this lesson to allow for longer completions in the exercises
def get_completion(prompt: str, system_prompt=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

# Exercise 2.1 - Spanish
# Modify the SYSTEM_PROMPT to make Claude output its answer in Spanish.


# System prompt - this is the only field you should change
SYSTEM_PROMPT = "Your responses should be in proper Spanish.  The kind they speak on Univision that no one understand because Spanish is so differentiated."

# Prompt
# PROMPT = "Hello Claude, how are you?"

# # Get Claude's response
# response = get_completion(PROMPT, SYSTEM_PROMPT)

# # Function to grade exercise correctness
# def grade_exercise(text):
#     return "hola" in text.lower()

# # Print Claude's response and the corresponding grade
# print(response)
# print("\n--------------------------- GRADING ---------------------------")
# print("This exercise has been correctly solved:", grade_exercise(response))



# Exercise 2.2 - One Player Only
# Modify the PROMPT so that Claude doesn't equivocate at all and responds with ONLY the name of one specific player, with no other words or punctuation.


# Prompt - this is the only field you should change
PROMPT = "Skip the preamble.  Only return the name.  No punctuation. While there are multiple contenders for the top, list the most likely best basketball player ever."

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return text == "Michael Jordan"

# Print Claude's response and the corresponding grade
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))