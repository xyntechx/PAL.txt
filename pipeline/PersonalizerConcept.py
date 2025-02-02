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

        self.concepts = []
        self.draft_dict = {}
        self.draft_chunks = []
        self.draft = ""


    def extract_concepts(self) -> None:
        logger.info(f"{self.name} extracting concepts...")

        class Info(BaseModel):
            concepts: list[str]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful computer science professor. Extract the main technical concepts taught in the following computer science textbook chapter written in markdown format. The main technical concepts are likely in the headers.",
                },
                {
                    "role": "user",
                    "content": f"{self.reference_text}",
                },
            ],
            response_format=Info,
        )

        res = completion.choices[0].message.parsed

        self.concepts = res.concepts
        self._save_specs()


    def create_analogies(self) -> None:
        logger.info(f"{self.name} personalizing chapter concept-by-concept...")

        for concept in tqdm(self.concepts):
            self.draft_dict[concept] = self._create_analogy(concept)
            self.draft_chunks.append(self._create_analogy(concept))

        self.draft = "\n\n".join(self.draft_chunks)
        self._save_draft()


    def _create_analogy(self, concept:str, layout:str=None) -> str:
        class Content(BaseModel):
            text: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in computer science (CS) and {self.user_interest}. Introduce the provided CS concept to a student interested in {self.user_interest}. Do not generate headers. Do not generate code blocks.",
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


    def _save_specs(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/specs.txt", "w", encoding="utf-8") as file:
            file.write(f"{self.concepts}")
            logger.info(f"Concepts saved in {self.save_dir}/{self.name}/specs.txt")


    def _save_draft(self) -> None:
        Path(f"{self.save_dir}/{self.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{self.name}/draft.md", "w", encoding="utf-8") as file:
            file.write(self.draft)
            logger.info(f"Draft personalized chapter saved in {self.save_dir}/{self.name}/draft.md")


if __name__ == "__main__":
    pass
