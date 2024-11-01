# Import python's built-in regular expression library
import re
import anthropic

# Retrieve the API_KEY & MODEL_NAME variables from the IPython store
from data.data import API_KEY

MODEL_NAME = "claude-3-haiku-20240307"

client = anthropic.Anthropic(api_key=API_KEY)

# New argument added for prefill text, with a default value of an empty string
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

# Variable content
# ANIMAL = "Cat"

# # Prompt template with a placeholder for the variable content
# PROMPT = f"Please write a haiku about {ANIMAL}. Put it in  tags."

# # Prefill for Claude's response
# PREFILL = "<haiku>"

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN:")
# print(PROMPT)
# print("\nASSISTANT TURN:")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(get_completion(PROMPT, prefill=PREFILL))
     

# Variable content
# ANIMAL = "Cat"

# # Prompt template with a placeholder for the variable content
# PROMPT = f"Please write a haiku about {ANIMAL}. Use JSON format with the keys as \"first_line\", \"second_line\", and \"third_line\"."

# # Prefill for Claude's response
# PREFILL = "{"

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN")
# print(PROMPT)
# print("\nASSISTANT TURN")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(get_completion(PROMPT, prefill=PREFILL))

# # First input variable
# EMAIL = "Hi Zack, just pinging you for a quick update on that prompt you were supposed to write."

# # Second input variable
# ADJECTIVE = "tripping-over-shoes-tied-together"

# # Prompt template with a placeholder for the variable content
# PROMPT = f"Hey Claude. Here is an email: <email>{EMAIL}</email>. Make this email more {ADJECTIVE}. Write the new version in <{ADJECTIVE}_email> XML tags."

# # Prefill for Claude's response (now as an f-string with a variable)
# PREFILL = f"<{ADJECTIVE}_email>"

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN")
# print(PROMPT)
# print("\nASSISTANT TURN")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(get_completion(PROMPT, prefill=PREFILL))

# Prompt template with a placeholder for the variable content
# PROMPT = f"Who is the best basketball player of all time? Please choose one specific player."

# # Prefill for Claude's response
# PREFILL = "Steph Curry is the GOAT.  are you nuts?  he plays for the"

# # Get Claude's response
# response = get_completion(PROMPT, prefill=PREFILL)

# # Function to grade exercise correctness
# def grade_exercise(text):
#     return bool(re.search("warrior", text))

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN")
# print(PROMPT)
# print("\nASSISTANT TURN")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(response)
# print("\n------------------------------------------ GRADING ------------------------------------------")
# print("This exercise has been correctly solved:", grade_exercise(response))


# Exercise 5.2 - Two Haikus
# Modify the PROMPT below using XML tags so that Claude writes two haikus about the animal instead of just one. It should be clear where one poem ends and the other begins.


# Variable content
# ANIMAL = "cats"

# # Prompt template with a placeholder for the variable content
# PROMPT = f"Please write a haiku about {ANIMAL}. Put it in  tags."

# # Prefill for Claude's response
# PREFILL = "I'll provide not just one haiku, but two.  and nothing else.  here are your poems, bruh:"

# # Get Claude's response
# response = get_completion(PROMPT, prefill=PREFILL)

# # Function to grade exercise correctness
# def grade_exercise(text):
#     return bool(
#         (re.search("cat", text.lower()) and re.search("", text))
#         and (text.count("\n") + 1) > 5
#     )

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN")
# print(PROMPT)
# print("\nASSISTANT TURN")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(response)
# print("\n------------------------------------------ GRADING ------------------------------------------")
# print("This exercise has been correctly solved:", grade_exercise(response))

# First input variable
ANIMAL1 = "Cat"

# Second input variable
ANIMAL2 = "Dog"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write two haikus.  The first should be about {ANIMAL1}. Put it in tags.  The second should be about {ANIMAL2}.  Put it in tags."

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("tail", text.lower()) and re.search("cat", text.lower()) and re.search("", text))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))