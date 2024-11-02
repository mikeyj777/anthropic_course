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

# First input variable - the user's question
QUESTION = "How long do I have to make an 83b election?"

# Second input variable - the tax code document that Claude will be using to answer the user's question
TAX_CODE = """
(a)General rule
If, in connection with the performance of services, property is transferred to any person other than the person for whom such services are performed, the excess of—
(1)the fair market value of such property (determined without regard to any restriction other than a restriction which by its terms will never lapse) at the first time the rights of the person having the beneficial interest in such property are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, over
(2)the amount (if any) paid for such property,
shall be included in the gross income of the person who performed such services in the first taxable year in which the rights of the person having the beneficial interest in such property are transferable or are not subject to a substantial risk of forfeiture, whichever is applicable. The preceding sentence shall not apply if such person sells or otherwise disposes of such property in an arm’s length transaction before his rights in such property become transferable or not subject to a substantial risk of forfeiture.
(b)Election to include in gross income in year of transfer
(1)In general
Any person who performs services in connection with which property is transferred to any person may elect to include in his gross income for the taxable year in which such property is transferred, the excess of—
(A)the fair market value of such property at the time of transfer (determined without regard to any restriction other than a restriction which by its terms will never lapse), over
(B)the amount (if any) paid for such property.
If such election is made, subsection (a) shall not apply with respect to the transfer of such property, and if such property is subsequently forfeited, no deduction shall be allowed in respect of such forfeiture.
(2)Election
An election under paragraph (1) with respect to any transfer of property shall be made in such manner as the Secretary prescribes and shall be made not later than 30 days after the date of such transfer. Such election may not be revoked except with the consent of the Secretary.

(c)Special rules
For purposes of this section—
(1)Substantial risk of forfeiture
The rights of a person in property are subject to a substantial risk of forfeiture if such person’s rights to full enjoyment of such property are conditioned upon the future performance of substantial services by any individual.

(2)Transferability of property
The rights of a person in property are transferable only if the rights in such property of any transferee are not subject to a substantial risk of forfeiture.

(3)Sales which may give rise to suit under section 16(b) of the Securities Exchange Act of 1934
So long as the sale of property at a profit could subject a person to suit under section 16(b) of the Securities Exchange Act of 1934, such person’s rights in such property are—
(A)subject to a substantial risk of forfeiture, and
(B)not transferable.
(4)For purposes of determining an individual’s basis in property transferred in connection with the performance of services, rules similar to the rules of section 72(w) shall apply.
(d)Certain restrictions which will never lapse
(1)Valuation
In the case of property subject to a restriction which by its terms will never lapse, and which allows the transferee to sell such property only at a price determined under a formula, the price so determined shall be deemed to be the fair market value of the property unless established to the contrary by the Secretary, and the burden of proof shall be on the Secretary with respect to such value.

(2)Cancellation
If, in the case of property subject to a restriction which by its terms will never lapse, the restriction is canceled, then, unless the taxpayer establishes—
(A)that such cancellation was not compensatory, and
(B)that the person, if any, who would be allowed a deduction if the cancellation were treated as compensatory, will treat the transaction as not compensatory, as evidenced in such manner as the Secretary shall prescribe by regulations,
the excess of the fair market value of the property (computed without regard to the restrictions) at the time of cancellation over the sum of—
(C)the fair market value of such property (computed by taking the restriction into account) immediately before the cancellation, and
(D)the amount, if any, paid for the cancellation,
shall be treated as compensation for the taxable year in which such cancellation occurs.
(e)Applicability of section
This section shall not apply to—
(1)a transaction to which section 421 applies,
(2)a transfer to or from a trust described in section 401(a) or a transfer under an annuity plan which meets the requirements of section 404(a)(2),
(3)the transfer of an option without a readily ascertainable fair market value,
(4)the transfer of property pursuant to the exercise of an option with a readily ascertainable fair market value at the date of grant, or
(5)group-term life insurance to which section 79 applies.
(f)Holding period
In determining the period for which the taxpayer has held property to which subsection (a) applies, there shall be included only the period beginning at the first time his rights in such property are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier.

(g)Certain exchanges
If property to which subsection (a) applies is exchanged for property subject to restrictions and conditions substantially similar to those to which the property given in such exchange was subject, and if section 354, 355, 356, or 1036 (or so much of section 1031 as relates to section 1036) applied to such exchange, or if such exchange was pursuant to the exercise of a conversion privilege—
(1)such exchange shall be disregarded for purposes of subsection (a), and
(2)the property received shall be treated as property to which subsection (a) applies.
(h)Deduction by employer
In the case of a transfer of property to which this section applies or a cancellation of a restriction described in subsection (d), there shall be allowed as a deduction under section 162, to the person for whom were performed the services in connection with which such property was transferred, an amount equal to the amount included under subsection (a), (b), or (d)(2) in the gross income of the person who performed such services. Such deduction shall be allowed for the taxable year of such person in which or with which ends the taxable year in which such amount is included in the gross income of the person who performed such services.

(i)Qualified equity grants
(1)In general
For purposes of this subtitle—
(A)Timing of inclusion
If qualified stock is transferred to a qualified employee who makes an election with respect to such stock under this subsection, subsection (a) shall be applied by including the amount determined under such subsection with respect to such stock in income of the employee in the taxable year determined under subparagraph (B) in lieu of the taxable year described in subsection (a).

(B)Taxable year determined
The taxable year determined under this subparagraph is the taxable year of the employee which includes the earliest of—
(i)the first date such qualified stock becomes transferable (including, solely for purposes of this clause, becoming transferable to the employer),
(ii)the date the employee first becomes an excluded employee,
(iii)the first date on which any stock of the corporation which issued the qualified stock becomes readily tradable on an established securities market (as determined by the Secretary, but not including any market unless such market is recognized as an established securities market by the Secretary for purposes of a provision of this title other than this subsection),
(iv)the date that is 5 years after the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, or
(v)the date on which the employee revokes (at such time and in such manner as the Secretary provides) the election under this subsection with respect to such stock.
(2)Qualified stock
(A)In general
For purposes of this subsection, the term “qualified stock” means, with respect to any qualified employee, any stock in a corporation which is the employer of such employee, if—
(i)such stock is received—
(I)in connection with the exercise of an option, or
(II)in settlement of a restricted stock unit, and
(ii)such option or restricted stock unit was granted by the corporation—
(I)in connection with the performance of services as an employee, and
(II)during a calendar year in which such corporation was an eligible corporation.
(B)Limitation
The term “qualified stock” shall not include any stock if the employee may sell such stock to, or otherwise receive cash in lieu of stock from, the corporation at the time that the rights of the employee in such stock first become transferable or not subject to a substantial risk of forfeiture.

(C)Eligible corporation
For purposes of subparagraph (A)(ii)(II)—
(i)In general
The term “eligible corporation” means, with respect to any calendar year, any corporation if—
(I)no stock of such corporation (or any predecessor of such corporation) is readily tradable on an established securities market (as determined under paragraph (1)(B)(iii)) during any preceding calendar year, and
(II)such corporation has a written plan under which, in such calendar year, not less than 80 percent of all employees who provide services to such corporation in the United States (or any possession of the United States) are granted stock options, or are granted restricted stock units, with the same rights and privileges to receive qualified stock.
(ii)Same rights and privileges
For purposes of clause (i)(II)—
(I)except as provided in subclauses (II) and (III), the determination of rights and privileges with respect to stock shall be made in a similar manner as under section 423(b)(5),
(II)employees shall not fail to be treated as having the same rights and privileges to receive qualified stock solely because the number of shares available to all employees is not equal in amount, so long as the number of shares available to each employee is more than a de minimis amount, and
(III)rights and privileges with respect to the exercise of an option shall not be treated as the same as rights and privileges with respect to the settlement of a restricted stock unit.
(iii)Employee
For purposes of clause (i)(II), the term “employee” shall not include any employee described in section 4980E(d)(4) or any excluded employee.

(iv)Special rule for calendar years before 2018
In the case of any calendar year beginning before January 1, 2018, clause (i)(II) shall be applied without regard to whether the rights and privileges with respect to the qualified stock are the same.

(3)Qualified employee; excluded employee
For purposes of this subsection—
(A)In general
The term “qualified employee” means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.
(B)Excluded employee
The term “excluded employee” means, with respect to any corporation, any individual—
(i)who is a 1-percent owner (within the meaning of section 416(i)(1)(B)(ii)) at any time during the calendar year or who was such a 1 percent owner at any time during the 10 preceding calendar years,
(ii)who is or has been at any prior time—
(I)the chief executive officer of such corporation or an individual acting in such a capacity, or
(II)the chief financial officer of such corporation or an individual acting in such a capacity,
(iii)who bears a relationship described in section 318(a)(1) to any individual described in subclause (I) or (II) of clause (ii), or
(iv)who is one of the 4 highest compensated officers of such corporation for the taxable year, or was one of the 4 highest compensated officers of such corporation for any of the 10 preceding taxable years, determined with respect to each such taxable year on the basis of the shareholder disclosure rules for compensation under the Securities Exchange Act of 1934 (as if such rules applied to such corporation).
(4)Election
(A)Time for making election
An election with respect to qualified stock shall be made under this subsection no later than 30 days after the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, and shall be made in a manner similar to the manner in which an election is made under subsection (b).

(B)Limitations
No election may be made under this section with respect to any qualified stock if—
(i)the qualified employee has made an election under subsection (b) with respect to such qualified stock,
(ii)any stock of the corporation which issued the qualified stock is readily tradable on an established securities market (as determined under paragraph (1)(B)(iii)) at any time before the election is made, or
(iii)such corporation purchased any of its outstanding stock in the calendar year preceding the calendar year which includes the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, unless—
(I)not less than 25 percent of the total dollar amount of the stock so purchased is deferral stock, and
(II)the determination of which individuals from whom deferral stock is purchased is made on a reasonable basis.
(C)Definitions and special rules related to limitation on stock redemptions
(i)Deferral stock
For purposes of this paragraph, the term “deferral stock” means stock with respect to which an election is in effect under this subsection.

(ii)Deferral stock with respect to any individual not taken into account if individual holds deferral stock with longer deferral period
Stock purchased by a corporation from any individual shall not be treated as deferral stock for purposes of subparagraph (B)(iii) if such individual (immediately after such purchase) holds any deferral stock with respect to which an election has been in effect under this subsection for a longer period than the election with respect to the stock so purchased.

(iii)Purchase of all outstanding deferral stock
The requirements of subclauses (I) and (II) of subparagraph (B)(iii) shall be treated as met if the stock so purchased includes all of the corporation’s outstanding deferral stock.

(iv)Reporting
Any corporation which has outstanding deferral stock as of the beginning of any calendar year and which purchases any of its outstanding stock during such calendar year shall include on its return of tax for the taxable year in which, or with which, such calendar year ends the total dollar amount of its outstanding stock so purchased during such calendar year and such other information as the Secretary requires for purposes of administering this paragraph.

(5)Controlled groups
For purposes of this subsection, all persons treated as a single employer under section 414(b) shall be treated as 1 corporation.

(6)Notice requirement
Any corporation which transfers qualified stock to a qualified employee shall, at the time that (or a reasonable period before) an amount attributable to such stock would (but for this subsection) first be includible in the gross income of such employee—
(A)certify to such employee that such stock is qualified stock, and
(B)notify such employee—
(i)that the employee may be eligible to elect to defer income on such stock under this subsection, and
(ii)that, if the employee makes such an election—
(I)the amount of income recognized at the end of the deferral period will be based on the value of the stock at the time at which the rights of the employee in such stock first become transferable or not subject to substantial risk of forfeiture, notwithstanding whether the value of the stock has declined during the deferral period,
(II)the amount of such income recognized at the end of the deferral period will be subject to withholding under section 3401(i) at the rate determined under section 3402(t), and
(III)the responsibilities of the employee (as determined by the Secretary under paragraph (3)(A)(ii)) with respect to such withholding.
(7)Restricted stock units
This section (other than this subsection), including any election under subsection (b), shall not apply to restricted stock units.
"""



######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = """You are a senior legal counsel.  your expertise and quality of response are the most valued at your firm.  
it is your job to meticulously read the provided legal resources.   
You are very well versed in tax law.  you are sought after for your ability to provide advice in clear terms, regardless of the complexity

"""

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = """give legal advice, but provide it an accessible tone.  

Accessible here means for example, the use of plain language explanations followed by technical details,
and that complex terms should be defined when used. you should be maintaining confidence in the advice while being approachable.

"""

##### Prompt element 4: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = f"""Here is some research that's been compiled. Use it to answer a legal question from the user.

<tax_code>{TAX_CODE}</tax_code>


"""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in  XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = """Here are examples of how to structure your complete response:

<example1>
<quotes>
"The rights of a person in property are subject to a substantial risk of forfeiture if such person's rights to full enjoyment of such property are conditioned upon the future performance of substantial services by any individual." [1]

"An election under paragraph (1) with respect to any transfer of property shall be made not later than 30 days after the date of such transfer." [2]
</quotes>

<analysis>
When you receive equity as part of your compensation, you typically need to work at the company for a period of time before you fully own these shares - this is called "vesting". However, the IRS gives you an important choice through something called an 83(b) election. This election lets you pay taxes on the shares up front, even before they vest.

From a technical standpoint, Section 83(b) of the Internal Revenue Code allows you to elect to be taxed on the fair market value of restricted stock at the time of grant, rather than waiting until the restrictions lapse. This can have significant tax advantages, particularly if you expect the stock value to increase substantially. [1]
</analysis>

<example_conclusion>
You must file an 83(b) election within 30 days of receiving your equity grant - this deadline is strict and cannot be extended. [2]
</example_conclusion>
</example1>

<example2>
<quotes>
"For purposes of this section, rules similar to the rules of section 72(w) shall apply." [4]
</quotes>

<analysis>
The provided tax code references rules in section 72(w) which are not included in our research materials. Without access to these referenced rules, I cannot provide a complete analysis of how they would impact this situation.

The technical details of how these rules would apply could significantly affect the proper interpretation of this section. [4]
</analysis>

<example_conclusion>
Sorry, I do not have sufficient information at hand to answer this question.
</example_conclusion>
</example2>

When citing the legal research in your answer, use brackets containing the section reference followed by a period at the end of the sentence doing the citing, as shown in the examples above.

"""

##### Prompt element 6: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = f""" Write a clear, concise answer to this question:

{QUESTION}

Your response should:
- Be no more than a couple of paragraphs
- Begin with a plain language explanation followed by any necessary technical details
- Define any complex terms as they are introduced
- Address practical considerations or common pitfalls if relevant
- Conclude with a single, direct sentence answering the user's question

If there is not sufficient information in the compiled research to produce a complete and accurate answer, 
respond with "Sorry, I do not have sufficient information at hand to answer this question."

Base your answer solely on the provided research materials, not on general knowledge of tax law.
"""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = ""

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = """Before providing your answer, please:
1. Extract relevant quotes from the research and place them in <quote> tags
2. Identify the key timing requirements and conditions
3. Note any relevant exceptions or special cases
4. Organize these elements from most to least important for answering the specific question
Only then proceed with your response."""

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = """Format your response as follows:
<quotes>
  Your extracted relevant quotes here
</quotes>

<analysis>
  Your two-paragraph response here, with plain language followed by technical details
</analysis>

<conclusion>
  Your single-sentence direct answer here
</conclusion>
"""

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
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
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))