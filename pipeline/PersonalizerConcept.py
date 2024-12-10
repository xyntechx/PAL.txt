from openai import OpenAI
from pydantic import BaseModel

from loguru import logger
from pathlib import Path
from tqdm import tqdm


class PersonalizerConcept():
    def __init__(self, name:str, user_interest:str, reference_text:str, save_dir:str):
        self.client = OpenAI()
        self.name = name
        self.user_interest = user_interest
        self.reference_text = reference_text
        self.save_dir = save_dir

        self.text_lang = ""
        self.concepts = []

        self.outline = []

        self.draft_chunks = []
        self.draft = ""
        self.judge_feedback = ""
        self.judge_summ_opp = ""

        self.final_chunks = []
        self.final_draft = ""

        self.judge_score = ""


    def extract_concepts(self) -> None:
        logger.info(f"{self.name} extracting concepts...")

        class Info(BaseModel):
            language: str
            concepts: list[str]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful computer science professor. Extract the main technical concepts taught in the following computer science textbook chapter written in markdown format. The main technical concepts are likely in the headers. If the chapter uses a specific programming language, include that in the 'language' field; otherwise, leave the 'language' field blank.",
                },
                {
                    "role": "user",
                    "content": f"{self.reference_text}",
                },
            ],
            response_format=Info,
        )

        res = completion.choices[0].message.parsed

        self.text_lang = res.language
        self.concepts = res.concepts
        self._save_specs()


    def write_outline(self) -> None:
        logger.info(f"{self.name} writing outline...")

        class ConceptOutline(BaseModel):
            concept: str
            layout: list[str]

        class Outline(BaseModel):
            outline: list[ConceptOutline]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful and thoughtful computer science (CS) textbook author. Your task is to outline the layout of text blocks that the reference chapter used to explain each concept in the concept list, where a text block is a paragraph, code block, etc. One concept should have one outline. Merge similar concepts together. If you are having trouble finding the layout for a particular concept, then it is likely that the concept is actually not in the chapter, and you must exclude that concept from your output.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Reference Chapter]\n{self.reference_text}\n[The End of Reference Chapter]\n\n[The Start of Concept List]\n{', '.join(self.concepts)}\n[The End of Concept List]",
                },
            ],
            response_format=Outline,
        )

        res = completion.choices[0].message.parsed

        # Updating concepts
        self.concepts = [item.concept for item in res.outline]

        self.outline = res.outline
        self._save_outline()


    def create_overview(self) -> None:
        logger.info(f"{self.name} creating overview...")

        class Overview(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful computer science (CS) professor. Given the set of CS concepts, write a brief overview for a CS textbook chapter that covers these concepts. Include an h1 title for the chapter and at most 2 paragraphs of overview. Your output should be in markdown format. Refrain from generating irrelevant details such as the chapter number.",
                },
                {
                    "role": "user",
                    "content": f"CS concepts: {', '.join(self.concepts)}",
                },
            ],
            response_format=Overview,
        )

        res = completion.choices[0].message.parsed

        self.draft_chunks.insert(0, res.text)


    def personalize(self, with_outline:bool=False) -> None:
        logger.info(f"{self.name} personalizing chapter concept-by-concept...")

        if with_outline:
            for item in tqdm(self.outline):
                self.draft_chunks.append(
                    self._personalize_concept(
                        item.concept,
                        layout=self._formatted_layout(item.layout)
                    )
                )
        else:
            for concept in tqdm(self.concepts):
                self.draft_chunks.append(self._personalize_concept(concept))

        self.draft = "\n\n".join(self.draft_chunks)
        self._save_draft()


    def _personalize_concept(self, concept:str, layout:str=None) -> str:
        layout_instructions = f"\n\nFollow the following layout in your output:\n{layout}" if layout else ""
        code_instructions = f" Include code snippets in {self.text_lang} to illustrate your explanations, where relevant." if self.text_lang else ""

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest}. Explain the provided CS concept in terms of {self.user_interest} concepts. Your explanation will be just one subsection of a CS textbook chapter. Include the concept as an h2 header, and subparts as one h3 header each (rephrase each subpart so that it is presentable to a student). Avoid numbering the headers and subheaders. Replace specific examples with examples related to {self.user_interest}.{code_instructions}{layout_instructions}",
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


    def _formatted_layout(self, layout:list[str]) -> str:
        return "\n".join([f"{i+1}. {x}" for i, x in enumerate(layout)])


    def refine(self) -> None:
        logger.info(f"{self.name} refining draft based on feedback...")
        self.final_chunks.append(self.draft_chunks[0]) # include overview
        for chunk in tqdm(self.draft_chunks[1:]): # exclude overview from refinement
            self.final_chunks.append(self._refine_subsection(chunk))
        self.final_draft = "\n\n".join(self.final_chunks)
        self._save_final()


    def _refine_subsection(self, subsection:str) -> str:
        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest} who is open to feedback. You have previously crafted the provided CS textbook chapter subsection for a friend who is interested in {self.user_interest}. Address the provided feedback to improve the CS textbook chapter subsection. The improved subsection should be similar in structure to the old subsection; your improvements does not need to drastically change the old subsection.{' You are also given an evaluation summary of a CS textbook chapter modified by another AI assistant; you may learn from that summary to improve your own chapter. Do not output any comments about the summary or your improvements, and output the chapter directly.' if self.judge_summ_opp else ''}",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Old Subsection]\n{subsection}\n[The End of Old Subsection]\n\n[The Start of Feedback for Your Work]\n{self.judge_feedback}\n[The End of Feedback for Your Work]\n\n[The Start of Evaluation Summary for Another Assistant's Work]\n{self.judge_summ_opp}\n[The End of Evaluation Summary for Another Assistant's Work]",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        return res.text


    def _save_specs(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/specs.txt", "w", encoding="utf-8") as file:
            file.write(f"Language: {self.text_lang}\n\nConcepts: {self.concepts}")
            logger.info(f"Specs (language and concepts) saved in {self.save_dir}/{self.name}/specs.txt")


    def _save_outline(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/outline.md", "w", encoding="utf-8") as file:
            text = []
            for item in self.outline:
                text.append(f"# {item.concept}\n{self._formatted_layout(item.layout)}")
            file.write("\n\n".join(text))
            logger.info(f"Outline saved in {self.save_dir}/{self.name}/outline.md")


    def _save_draft(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/draft.md", "w", encoding="utf-8") as file:
            file.write(self.draft)
            logger.info(f"Draft personalized chapter saved in {self.save_dir}/{self.name}/draft.md")


    def _save_final(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/final_draft.md", "w", encoding="utf-8") as file:
            file.write(self.final_draft)
            logger.info(f"Final personalized chapter saved in {self.save_dir}/{self.name}/final_draft.md")


if __name__ == "__main__":
    pass
