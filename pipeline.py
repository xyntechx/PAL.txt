from pydantic import BaseModel


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


def judge():
    # TODO: (?) provide original chapter as reference
    # TODO: evaluate on qualitative metrics (see slack)
    pass


if __name__ == "__main__":
    pass
