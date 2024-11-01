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
# PROMPT = "Name a famous movie starring an actor who was born in the year 1956. First brainstorm about some actors and their birth years in  tags, then give your answer."

# # Print Claude's response
# print(get_completion(PROMPT))

# Exercise 6.1 - Classifying Emails
# In this exercise, we'll be instructing Claude to sort emails into the following categories:

# (A) Pre-sale question
# (B) Broken or defective item
# (C) Billing question
# (D) Other (please explain)
# For the first part of the exercise, change the PROMPT to make Claude output the correct classification and ONLY the classification. Your answer needs to include the letter (A - D) of the correct choice, with the parentheses, as well as the name of the category.

# Refer to the comments beside each email in the EMAILS list to know which category that email should be classified under.

categories = [
  "(A) Pre-sale question",
  "(B) Broken or defective item",
  "(C) Billing question",
  "(D) Other (please explain)"
]

category_str = '|'.join(categories)

# Prompt template with a placeholder for the variable content
PROMPT = """Please classify this email {email} into the following categories {category_str}.  categories are delimited by pipes with their letter in parentheses.  output the correct classification and ONLY the classification. Your answer needs to only be the letter (A - D) of the correct choice, not the description"""

# Prefill for Claude's response, if any
PREFILL = "<answer>"

# Variable content stored as a list
EMAILS = [
    "Hi -- My Mixmaster4000 is producing a strange noise when I operate it. It also smells a bit smoky and plasticky, like burning electronics.  I need a replacement.", # (B) Broken or defective item
    "Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?", # (A) Pre-sale question OR (D) Other (please explain)
    "I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???", # (C) Billing question
    "How did I get here I am not good with computer.  Halp." # (D) Other (please explain)
]

# Correct categorizations stored as a list of lists to accommodate the possibility of multiple correct categorizations per email
ANSWERS = [
    ["B"],
    ["A","D"],
    ["C"],
    ["D"]
]

# Dictionary of string values for each category to be used for regex grading
REGEX_CATEGORIES = {
    "A": "A\) P",
    "B": "B\) B",
    "C": "C\) B",
    "D": "D\) O"
}

# Iterate through list of emails
for i,email in enumerate(EMAILS):
    
    # Substitute the email text into the email placeholder variable
    formatted_prompt = PROMPT.format(email=email, category_str=category_str)
   
    # Get Claude's response
    response = get_completion(formatted_prompt, prefill=PREFILL)

    # Grade Claude's response
    grade = any([bool(re.search(REGEX_CATEGORIES[ans], response)) for ans in ANSWERS[i]])
    
    # Print Claude's response
    print("--------------------------- Full prompt with variable substutions ---------------------------")
    print("USER TURN")
    print(formatted_prompt)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print("\n------------------------------------- Claude's response -------------------------------------")
    print(response)
    print("\n------------------------------------------ GRADING ------------------------------------------")
    print("This exercise has been correctly solved:", grade, "\n\n\n\n\n\n")