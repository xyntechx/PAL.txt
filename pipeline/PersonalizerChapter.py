from openai import OpenAI
from pydantic import BaseModel

from loguru import logger
from pathlib import Path
from tqdm import tqdm


class PersonalizerChapter():
    def __init__(self, name:str, user_interest:str, reference_text:str, save_dir:str):
        self.client = OpenAI()
        self.name = name
        self.user_interest = user_interest
        self.reference_text = reference_text
        self.save_dir = save_dir

        self.sections = []

        self.draft_chunks = []
        self.draft = ""
        self.judge_feedback = ""
        self.judge_summ_opp = ""

        self.final_chunks = []
        self.final_draft = ""

        self.judge_score = ""


    def extract_sections(self) -> None:
        logger.info(f"{self.name} extracting sections...")

        class Section(BaseModel):
            section: str

        class Sections(BaseModel):
            sections: list[Section]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a thoughtful computer science (CS) textbook author. Your task is to separate the sections within the provided CS textbook chapter that is written in Markdown. Each section is mutually exclusive to one another; one unique text block (e.g. header, paragraph, code block, etc.) must belong to one and only one section. Each section must contain two or more text blocks. Your output must contain all text blocks found in the chapter.",
                },
                {
                    "role": "user",
                    "content": f"{self.reference_text}",
                },
            ],
            temperature=0,
            response_format=Sections,
        )

        res = completion.choices[0].message.parsed
        self.sections = res.sections


    def personalize(self) -> None:
        logger.info(f"{self.name} personalizing chapter section-by-section...")

        for section in tqdm(self.sections):
            self.draft_chunks.append(self._personalize_section(section.section))

        self.draft = "\n\n".join(self.draft_chunks)


    def _personalize_section(self, section:str) -> None:
        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest}. Your task is to modify the explanations and examples in the provided CS textbook chapter section (written in Markdown) using {self.user_interest} concepts. Ensure the layout of your personalized section exactly follows the layout of the original section. Do not leave out any paragraph, code block, etc.",
                },
                {
                    "role": "user",
                    "content": f"{section}",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        return res.text


    def create_overview(self) -> None:
        logger.info(f"{self.name} creating overview...")

        class Overview(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful computer science (CS) professor. Given the following CS textbook chapter, write a brief overview of the concepts taught. Create an h1 title for the chapter and at most 2 paragraphs of overview. Your output should be in markdown format. Refrain from generating irrelevant details such as the chapter number.",
                },
                {
                    "role": "user",
                    "content": self.draft,
                },
            ],
            response_format=Overview,
        )

        res = completion.choices[0].message.parsed

        self.draft_chunks.insert(0, res.text.strip())
        self.draft = "\n\n".join(self.draft_chunks)
        self._save_draft()


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
