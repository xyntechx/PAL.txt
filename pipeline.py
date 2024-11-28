from pydantic import BaseModel


################################
# Personalization LLM -- Start #
################################


def extract_concepts(client, content:str):
    class Info(BaseModel):
        language: str
        concepts: list[str]

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful computer science professor. Extract the main technical concepts taught in the following computer science textbook chapter written in markdown format. The main technical concepts are likely in the headers. If the chapter uses a specific programming language, include that in the 'language' field; otherwise, leave the 'language' field blank.",
            },
            {
                "role": "user",
                "content": f"{content}",
            },
        ],
        response_format=Info,
    )

    res = completion.choices[0].message.parsed
    return res.language, res.concepts


def create_overview(client, concepts:list[str]):
    class Overview(BaseModel):
        text: str

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful computer science (CS) professor. Given the set of CS concepts, write a brief overview for a CS textbook chapter that covers these concepts. Include an h1 title for the chapter and at most 2 paragraphs of overview. Your output should be in markdown format.",
            },
            {
                "role": "user",
                "content": f"CS concepts: {concepts}",
            },
        ],
        response_format=Overview,
    )

    res = completion.choices[0].message.parsed
    return res.text


def personalize(client, language:str, concept:str, interest:str):
    class Content(BaseModel):
        text: str

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"You are an expert in computer science (CS) and {interest}. Explain the provided CS concept in terms of {interest} concepts. Your explanation will be just one subsection of a CS textbook chapter. Headers should be h2, and subheaders should be h3. Avoid numbering the headers and subheaders.{f' Feel free to include code snippets in {language} to illustrate your explanations.' if language else ''}",
            },
            {
                "role": "user",
                "content": f"CS concept to teach: {concept}",
            },
        ],
        response_format=Content,
    )

    res = completion.choices[0].message.parsed
    return res.text


def personalize_refine(client, interest:str, subsection:str, feedback:str):
    class Content(BaseModel):
        text: str

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"You are an expert in computer science (CS) and {interest} who is open to feedback. You have previously crafted the provided CS textbook chapter subsection for a friend who is interested in {interest}. Address the provided feedback to improve the CS textbook chapter subsection. The improved subsection should be similar in structure to the old subsection; your improvements does not need to drastically change the old subsection.",
            },
            {
                "role": "user",
                "content": f"[The Start of Old Subsection]\n{subsection}\n[The End of Old Subsection]\n\n[The Start of Feedback]\n{feedback}\n[The End of Feedback]",
            },
        ],
        response_format=Content,
    )

    res = completion.choices[0].message.parsed
    return res.text


##############################
# Personalization LLM -- End #
##############################


######################
# Judge LLM -- Start #
######################


def give_feedback(client, interest:str, reference:str, modified:str):
    class Eval(BaseModel):
        category: str
        score: int
        explanation: str
    
    class Evals(BaseModel):
        evals: list[Eval]

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"You are an expert in {interest} and computer science. Please act as an objective judge and evaluate the quality of a modified computer science (CS) textbook chapter outputted by an AI assistant, which explains CS concepts using {interest} concepts. You will be given a reference textbook chapter that explains CS concepts without modifications. Your task is to score the modified textbook on three categories on a scale of 1 to 3, where 1 is unsatisfactory, 2 is semi-satisfactory, and 3 is satisfactory. In your output, include the category, the score, and your explanation for why you gave that score. The categories are:\n\n- All CS concepts from the reference chapter have been adequately covered\n- All CS concepts from the reference chapter have been accurately explained\n- The {interest} concepts are sufficiently used\n- The {interest} concepts are accurately used\n- The {interest} concepts do not overshadow the CS concepts (the main subject to be taught is CS)\n\nDo not allow the length of the responses to influence your evaluation. Be as objective as possible.",
            },
            {
                "role": "user",
                "content": f"[The Start of Reference Chapter]\n{reference}\n[The End of Reference Chapter]\n\n[The Start of Modified Chapter]\n{modified}\n[The End of Modified Chapter]",
            },
        ],
        response_format=Evals,
    )

    res = completion.choices[0].message.parsed
    return res.evals


def compare(client, interest:str, draft_a:str, draft_b:str):
    class Verdict(BaseModel):
        choice: str
        explanation: str

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"Please act as an impartial judge and evaluate the quality of the modified computer science (CS) textbook chapters outputted by two AI assistants. The chapters explain CS concepts using {interest} concepts. Your evaluation is from the perspective of someone who is interested in {interest} but is new to the CS concepts. Your job is to evaluate which assistant's chapter is more effective for you to learn CS.\n\nAvoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict in the 'choice' field by strictly following this format: 'A' if assistant A is better, 'B' if assistant B is better, and 'C' for a tie. Include a brief explanation of your choice in the output.",
            },
            {
                "role": "user",
                "content": f"[The Start of Assistant A's Chapter]\n{draft_a}\n[The End of Assistant A's Chapter]\n\n[The Start of Assistant B's Chapter]\n{draft_b}\n[The End of Assistant B's Chapter]",
            },
        ],
        response_format=Verdict,
    )

    res = completion.choices[0].message.parsed
    return res.choice, res.explanation


####################
# Judge LLM -- End #
####################


if __name__ == "__main__":
    pass
