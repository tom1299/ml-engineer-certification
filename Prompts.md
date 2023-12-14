> Put instructions at the beginning of the prompt and use ### or """ to separate the instruction and context

```text
Summarize the text below as a bullet point list of the most important points.

Text: """
{text input here}
"""
```

> Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc 

```text
Create a condensed abstract of the transcript of an online course below using at least 20 bullet points no longer than 2 to 3 sentences. Highlight the key aspects in bold. Exclude any text regarding the course. Add a heading to the text that summarizes the content of the text.

Desired format:
Heading:
Bullet points

Text: """
{text input here}
"""
```

> Tactic: Ask the model to adopt a persona The system message can be used to specify the persona used by the model in its replies.

```text
SYSTEM: You are an excellent technical writer eager to help people learn the concepts of data processing and machine learning with google cloud.
USER: Create a condensed abstract of the transcript of an online course below using at least 20 bullet points no longer than 2 to 3 sentences. Highlight the key aspects in bold. Exclude any text regarding the course. Add a heading to the text that summarizes the content of the text.

Desired format:
Heading:
Bullet points

Text: """
{text input here}
"""
```

```text
SYSTEM: You are a senior writer of online tests and want to do your best to train a trainee on passing an exam on google cloud and machine learning.
USER: Create 10 multiple choice questions all with multiple select options for the content of the following text. Half of the questions should have more than one right answers. 1 questions should not have any right answers. Wide the scope of the questions a little bit by assuming general knowledge of google cloud concepts, machine and data analysis. Do not mention the text explicitly but rather pose general questions.
Solutions to the questions should be put at the end of the output separated from the questions by 10 blank lines. Content should be written in markdown.

Desired format:
Heading:
Questions
---
Answers

Examples:
```markdown
### Questions on topic <Add topic here>

1. What are challenges faced when aiming to get messages reliably into a data warehouse from Pub/Sub? (Select all that apply)
    - A Data encryption
    - B. Scalability
    - C. Data transformation
    - D. Data visualization
    - E. Matching Pub/Sub scale and elasticity

<Add additional questions here>
---
#### Answers

1. B, C, E
<Add subsequent answers here>
```
Text: """
{text input here}
"""
```