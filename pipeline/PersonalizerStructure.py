from openai import OpenAI
from pydantic import BaseModel

from loguru import logger
from pathlib import Path
from tqdm import tqdm


class PersonalizerStructure():
    def __init__(self, name:str, user_interest:str, reference_text:str, save_dir:str):
        self.client = OpenAI()
        self.name = name
        self.user_interest = user_interest
        self.reference_text = reference_text
        self.save_dir = save_dir

        self.sections = []
        self.draft_chunks = []
        self.draft = ""
        self.feedback_student = ""
        self.feedback_expert = ""
        self.final_draft = ""


    def extract_sections(self) -> None:
        logger.info(f"{self.name} extracting sections...")

        class Sections(BaseModel):
            sections: list[str]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a thoughtful computer science (CS) textbook author. Your task is to separate the sections within the provided CS textbook chapter that is written in Markdown. Each section is mutually exclusive to one another; one unique text block (e.g. header, paragraph, code block, etc.) must belong to one and only one section. Each section must contain two or more text blocks. Your output must contain all text blocks found in the chapter.",
                },
                {
                    "role": "user",
                    "content": f"{self.draft}",
                },
            ],
            temperature=0,
            response_format=Sections,
        )

        res = completion.choices[0].message.parsed
        self.sections = res.sections


    def personalize(self) -> None:
        logger.info(f"{self.name} personalizing chapter with one-to-one mapping...")

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest}. Your task is to modify the explanations and examples in the provided CS textbook chapter (written in Markdown) using {self.user_interest} concepts. Ensure the layout of your personalized chapter exactly follows the layout of the original section. Do not leave out any paragraph, code block, etc.",
                },
                {
                    "role": "user",
                    "content": f"{self.reference_text}",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        self.draft = res.text
        self._save_draft()


    def insert_analogies(self, other):
        text = ""

        for concept in tqdm(other.draft_dict):
            section = list(filter(lambda x: concept in x, self.sections))

            if len(section) == 0:
                continue

            section = section[0]
            analogy = other.draft_dict[concept]
            text += f"{section}\n\n{analogy}\n\n"

        self.draft_analogy = text
        self.draft = text
        self._save_draft_analogy()


    def refine_student(self):
        self.draft = ""
        for section in tqdm(self.sections):
            self.draft += f"{self._refine_student(section)}\n\n"


    def _refine_student(self, section) -> str:
        logger.info(f"{self.name} refining draft based on feedback...")

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest} who is receptive to feedback. A student gave you feedback to improve the old CS textbook section. Output the improved old section based on the feedback and only the feedback. Only make minor edits.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Old Section]\n{section}\n[The End of Old Section]\n\n[The Start of Student Feedback]\n{self.feedback_student}\n[The End of Student Feedback]",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        return res.text


    def refine_expert(self):
        self.draft = ""
        for section in tqdm(self.sections):
            self.draft += f"{self._refine_expert(section)}\n\n"


    def _refine_expert(self, section) -> str:
        logger.info(f"{self.name} refining draft based on feedback...")

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest} who is receptive to feedback. Another expert gave you feedback to improve the old CS textbook chapter. Output the improved old section based on the feedback and only the feedback. Only make minor edits.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Old Section]\n{section}\n[The End of Old Section]\n\n[The Start of Expert Feedback]\n{self.feedback_expert}\n[The End of Expert Feedback]",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        return res.text


    def finalize(self):
        self.final_draft = self.draft
        self._save_final()


    def _save_draft(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/draft.md", "w", encoding="utf-8") as file:
            file.write(self.draft)
            logger.info(f"Draft personalized chapter saved in {self.save_dir}/{self.name}/draft.md")

    def _save_draft_analogy(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/draft_analogy.md", "w", encoding="utf-8") as file:
            file.write(self.draft_analogy)
            logger.info(f"Draft personalized chapter saved in {self.save_dir}/{self.name}/draft_analogy.md")


    def _save_final(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/final_draft.md", "w", encoding="utf-8") as file:
            file.write(self.final_draft)
            logger.info(f"Final personalized chapter saved in {self.save_dir}/{self.name}/final_draft.md")


if __name__ == "__main__":
    pass
