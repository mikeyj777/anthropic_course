"""

loading markdown file for previous chat summary.  having Claude use this to develop updated gamma protocol

"""

from data.data import API_KEY
from markdown_processing import unmark

import anthropic
MODEL_NAME = "claude-3-opus-20240229"

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt="", prefill=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        temperature=0.0,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text

######################################## PROMPT ELEMENTS ########################################

with open('data/conversation_2024-11-02T18-19-08-687Z.md', 'r', encoding='utf-8') as f:
    conversation = f.read()

conversation = ''.join([i if ord(i) < 128 else '_' for i in conversation])
# conversation = unmark(conversation)

##### Prompt element 1: Task context
TASK_CONTEXT = """you are a content developer, versed in generating protocol documents for setting guidelines for Claude responses to prompt requests.
"""

##### Prompt element 2: Tone context
TONE_CONTEXT = """

maintain a tone that is professional.  use a top-down structure to organize the content in appropriate sections.

"""

##### Prompt element 3: Input data
INPUT_DATA = conversation

##### Prompt element 4: Examples
EXAMPLES = ""

##### Prompt element 5: Task description
TASK_DESCRIPTION = "inspect the contents of the conversation and generate the full Gamma protocol document discussed near the end."

##### Prompt element 6: Immediate task
IMMEDIATE_TASK = """

The Gamma Protocol needs to have an element of role play.  Generate a person in the Harry Potter Universe that fits the following:

Name: Cassandra "Cass" Codewise
Position: 7th Year Ravenclaw Prefect
Aspiration: Future Head of Ravenclaw House
Mentor: The Wizard of Artifacts (Professor)
Academic Standing: Top of class in Artifact Charms
Special Recognition: Two-time winner of the Golden Quill Award for Documentation Excellence
Known for: Creating the first self-documenting spellbook in Hogwarts history

"""

##### Prompt element 7: Precognition
PRECOGNITION = "Before generating, review the entire conversation and extract all data in tags related to Gamma protocol and its sections"

##### Prompt element 8: Output formatting
OUTPUT_FORMATTING = "format your output in markdown using a top-down outline structure"

##### Prompt element 9: Prefill
PREFILL = ""

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substitutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
