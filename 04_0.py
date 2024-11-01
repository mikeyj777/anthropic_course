# Import python's built-in regular expression library
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

# using XML tags

# Exercise 4.1 - Haiku Topic
# Modify the PROMPT so that it's a template that will take in a variable called TOPIC and output a haiku about the topic. This exercise is just meant to test your understanding of the variable templating structure with f-strings.


# Variable content
# TOPIC = "Pigs"

# # Prompt template with a placeholder for the variable content
# PROMPT = f"consider what a Haiku is.  once you have the idea, start to develop a haiku based on the topic <topic>{TOPIC}<\topic>.  when complete review the entire haiku to confirm adequate structure.  repeat as needed."

# # Get Claude's response
# response = get_completion(PROMPT)

# # Function to grade exercise correctness
# def grade_exercise(text):
#     return bool(re.search("pigs", text.lower()) and re.search("haiku", text.lower()))

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print(PROMPT)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(response)
# print("\n------------------------------------------ GRADING ------------------------------------------")
# print("This exercise has been correctly solved:", grade_exercise(response))
     
# Exercise 4.2 - Dog Question with Typos
# Fix the PROMPT by adding XML tags so that Claude produces the right answer.

# Try not to change anything else about the prompt. The messy and mistake-ridden writing is intentional, so you can see how Claude reacts to such mistakes.


# Variable content
QUESTION = "ar cn brown?"

# Prompt template with a placeholder for the variable content
PROMPT = f"Hia its me i have a q about dogs jkaerjv <question>{QUESTION}</question> jklmvca tx it help me muhch much atx fst fst answer short short tx"

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("brown", text.lower()))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))