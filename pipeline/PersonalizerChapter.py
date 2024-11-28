from openai import OpenAI
from pydantic import BaseModel

from loguru import logger
from pathlib import Path


class PersonalizerChapter():
    def __init__(self, name:str, user_interest:str, reference_text:str, save_dir:str):
        self.client = OpenAI()
        self.name = name
        self.user_interest = user_interest
        self.reference_text = reference_text
        self.save_dir = save_dir

        self.draft = ""
        self.judge_feedback = ""

        self.final_draft = ""


    def personalize(self) -> None:
        logger.info(f"{self.name} personalizing chapter all at once...")

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest}. Personalize the provided CS textbook chapter based on {self.user_interest} content. Keep your output as faithful to the original chapter as possible while including a sufficient amount of {self.user_interest} content.",
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


    def refine(self) -> None:
        logger.info(f"{self.name} refining draft based on feedback...")

        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest} who is open to feedback. You have previously crafted the provided CS textbook chapter for a friend who is interested in {self.user_interest}. Address the provided feedback to improve the CS textbook chapter. The improved chapter should be similar in structure to the old chapter; your improvements does not need to drastically change the old chapter.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Old Chapter]\n{self.draft}\n[The End of Old Chapter]\n\n[The Start of Feedback]\n{self.judge_feedback}\n[The End of Feedback]",
                },
            ],
            response_format=Content,
        )

        res = completion.choices[0].message.parsed
        self.final_draft = res.text
        self._save_final()


    def _save_draft(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/draft.md", "w") as file:
            file.write(self.draft)
            logger.info(f"Draft personalized chapter saved in {self.save_dir}/{self.name}/draft.md")


    def _save_final(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/final_draft.md", "w") as file:
            file.write(self.final_draft)
            logger.info(f"Final personalized chapter saved in {self.save_dir}/{self.name}/final_draft.md")


if __name__ == "__main__":
    pass
