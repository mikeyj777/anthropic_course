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
# PROMPT = "Will Santa bring me presents on Christmas?"

# # Print Claude's response
# print(get_completion(PROMPT))  
# 
# Prompt
# PROMPT = """Please complete the conversation by writing the next line, speaking as "A".
# Q: Is the tooth fairy real?
# A: Of course, sweetie. Wrap up your tooth and put it under your pillow tonight. There might be something waiting for you in the morning.
# Q: Will Santa bring me presents on Christmas?"""

# Print Claude's response
# print(get_completion(PROMPT)) 

# Prompt template with a placeholder for the variable content
# PROMPT = """Silvermist Hollow, a charming village, was home to an extraordinary group of individuals.
# Among them was Dr. Liam Patel, a neurosurgeon who revolutionized surgical techniques at the regional medical center.
# Olivia Chen was an innovative architect who transformed the village's landscape with her sustainable and breathtaking designs.
# The local theater was graced by the enchanting symphonies of Ethan Kovacs, a professionally-trained musician and composer.
# Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers.
# These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow.

# 1. Dr. Liam Patel [NEUROSURGEON]
# 2. Olivia Chen [ARCHITECT]
# 3. Ethan Kovacs [MISICIAN AND COMPOSER]
# 4. Isabella Torres [CHEF]


# At the heart of the town, Chef Oliver Hamilton has transformed the culinary scene with his farm-to-table restaurant, Green Plate. Oliver's dedication to sourcing local, organic ingredients has earned the establishment rave reviews from food critics and locals alike.
# Just down the street, you'll find the Riverside Grove Library, where head librarian Elizabeth Chen has worked diligently to create a welcoming and inclusive space for all. Her efforts to expand the library's offerings and establish reading programs for children have had a significant impact on the town's literacy rates.
# As you stroll through the charming town square, you'll be captivated by the beautiful murals adorning the walls. These masterpieces are the work of renowned artist, Isabella Torres, whose talent for capturing the essence of Riverside Grove has brought the town to life.
# Riverside Grove's athletic achievements are also worth noting, thanks to former Olympic swimmer-turned-coach, Marcus Jenkins. Marcus has used his experience and passion to train the town's youth, leading the Riverside Grove Swim Team to several regional championships.

# 1. Oliver Hamilton [CHEF]
# 2. Elizabeth Chen [LIBRARIAN]
# 3. Isabella Torres [ARTIST]
# 4. Marcus Jenkins [COACH]


# Oak Valley, a charming small town, is home to a remarkable trio of individuals whose skills and dedication have left a lasting impact on the community.
# At the town's bustling farmer's market, you'll find Laura Simmons, a passionate organic farmer known for her delicious and sustainably grown produce. Her dedication to promoting healthy eating has inspired the town to embrace a more eco-conscious lifestyle.
# In Oak Valley's community center, Kevin Alvarez, a skilled dance instructor, has brought the joy of movement to people of all ages. His inclusive dance classes have fostered a sense of unity and self-expression among residents, enriching the local arts scene.
# Lastly, Rachel O'Connor, a tireless volunteer, dedicates her time to various charitable initiatives. Her commitment to improving the lives of others has been instrumental in creating a strong sense of community within Oak Valley.
# Through their unique talents and unwavering dedication, Laura, Kevin, and Rachel have woven themselves into the fabric of Oak Valley, helping to create a vibrant and thriving small town."""

# # Prefill for Claude's response
# PREFILL = ""

# # Print Claude's response
# print("--------------------------- Full prompt with variable substutions ---------------------------")
# print("USER TURN:")
# print(PROMPT)
# print("\nASSISTANT TURN:")
# print(PREFILL)
# print("\n------------------------------------- Claude's response -------------------------------------")
# print(get_completion(PROMPT, prefill=PREFILL))


# Exercise 7.1 - Email Formatting via Examples
# We're going to redo Exercise 6.2, but this time, we're going to edit the PROMPT to use "few-shot" examples of emails + proper classification (and formatting) to get Claude to output the correct answer. We want the last letter of Claude's output to be the letter of the category.

# Refer to the comments beside each email in the EMAILS list if you forget which letter category is correct for each email.

# Remember that these are the categories for the emails:

# (A) Pre-sale question
# (B) Broken or defective item
# (C) Billing question
# (D) Other (please explain)

categories = [
  "(A) Pre-sale question",
  "(B) Broken or defective item",
  "(C) Billing question",
  "(D) Other (please explain)"
]

category_str = '|'.join(categories)

# Prompt template with a placeholder for the variable content
PROMPT = """Please classify this email {email} into the following categories {category_str}.  Here's some examples:  

<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}"""

# Prefill for Claude's response
PREFILL = ""

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

# Iterate through list of emails
for i,email in enumerate(EMAILS):
    
    # Substitute the email text into the email placeholder variable
    formatted_prompt = PROMPT.format(email=email, category_str=category_str)
   
    # Get Claude's response
    response = get_completion(formatted_prompt, prefill=PREFILL)

    # Grade Claude's response
    grade = any([bool(re.search(ans, response[-1])) for ans in ANSWERS[i]])
    
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