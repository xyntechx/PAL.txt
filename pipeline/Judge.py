from openai import OpenAI
from pydantic import BaseModel

from loguru import logger
from pathlib import Path


class Judge():
    def __init__(self, user_interest:str, reference_text:str, save_dir:str):
        self.client = OpenAI()
        self.user_interest = user_interest
        self.reference_text = reference_text
        self.save_dir = save_dir

        self.final_choice = ""
        self.final_explanation = ""


    def give_feedback(self, PLLM, PLLM_other=None, compete:bool=False) -> None:
        logger.info("Judge LLM giving feedback...")

        class Eval(BaseModel):
            category: str
            score: int
            explanation: str

        class Evals(BaseModel):
            evals: list[Eval]

        class EvalsCompetitive(BaseModel):
            evals: list[Eval]
            summary: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in {self.user_interest} and computer science. Please act as an objective judge and evaluate the quality of a modified computer science (CS) textbook chapter outputted by an AI assistant, which explains CS concepts using {self.user_interest} concepts. You will be given a reference textbook chapter that explains CS concepts without modifications. Your task is to score the modified textbook on four categories on a scale of 1 to 3, where 1 is unsatisfactory, 2 is semi-satisfactory, and 3 is satisfactory. In your output, include the category, the score, and your explanation for why you gave that score. The categories are:\n\n- All CS concepts from the reference chapter have been accurately explained\n- The {self.user_interest} concepts are sufficiently used\n- The {self.user_interest} concepts are accurately used\n- The {self.user_interest} concepts do not overshadow the CS concepts (the main subject to be taught is CS)\n\nDo not allow the length of the responses to influence your evaluation. Be as objective as possible.{' In your output, include a summary of what the AI assistant accomplished in making the modified chapter, as well as what you like and dislike about the modified chapter.' if compete else ''}",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Reference Chapter]\n{self.reference_text}\n[The End of Reference Chapter]\n\n[The Start of Modified Chapter]\n{PLLM.draft}\n[The End of Modified Chapter]",
                },
            ],
            response_format=EvalsCompetitive if compete else Evals,
        )

        res = completion.choices[0].message.parsed

        for eval in res.evals:
            PLLM.judge_feedback += f"# Evaluation category: {eval.category}\n\nScore: {eval.score}/3\n\nFeedback: {eval.explanation}\n\n"

        if compete:
            PLLM_other.judge_summ_opp = res.summary
            self._save_summary(PLLM, PLLM_other)

        self._save_feedback(PLLM)


    def compare(self, PLLM_a, PLLM_b) -> None:
        logger.info("Judge LLM comparing Personalizer outputs...")

        class Verdict(BaseModel):
            choice: str
            explanation: str

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"Please act as an impartial judge and evaluate the quality of the modified computer science (CS) textbook chapters outputted by two AI assistants. The chapters explain CS concepts using {self.user_interest} concepts. Your evaluation is from the perspective of someone who is interested in {self.user_interest} but is new to the CS concepts. Your job is to evaluate which assistant's chapter is more effective for you to learn CS.\n\nAvoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict in the 'choice' field by strictly following this format: '{PLLM_a.name}' if assistant {PLLM_a.name} is better, '{PLLM_b.name}' if assistant {PLLM_b.name} is better, and 'TIE' for a tie. Include a brief explanation of your choice in the output.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Assistant {PLLM_a.name}'s Chapter]\n{PLLM_a.final_draft}\n[The End of Assistant {PLLM_a.name}'s Chapter]\n\n[The Start of Assistant {PLLM_b.name}'s Chapter]\n{PLLM_b.final_draft}\n[The End of Assistant {PLLM_b.name}'s Chapter]",
                },
            ],
            response_format=Verdict,
        )

        res = completion.choices[0].message.parsed

        self.final_choice = res.choice
        self.final_explanation = res.explanation

        self._save_verdict()


    def score(self, PLLM) -> None:
        logger.info("Judge LLM scoring...")

        class Eval(BaseModel):
            category: str
            score: int
            explanation: str

        class Evals(BaseModel):
            evals: list[Eval]

        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in {self.user_interest} and computer science. Please act as an objective judge and evaluate the quality of a modified computer science (CS) textbook chapter outputted by an AI assistant, which explains CS concepts using {self.user_interest} concepts. You will be given a reference textbook chapter that explains CS concepts without modifications. Your task is to score the modified textbook on four categories on a scale of 1 to 3, where 1 is unsatisfactory, 2 is semi-satisfactory, and 3 is satisfactory. In your output, include the category, the score, and your explanation for why you gave that score. The categories are:\n\n- All CS concepts from the reference chapter have been accurately explained\n- The {self.user_interest} concepts are sufficiently used\n- The {self.user_interest} concepts are accurately used\n- The {self.user_interest} concepts do not overshadow the CS concepts (the main subject to be taught is CS)\n\nDo not allow the length of the responses to influence your evaluation. Be as objective as possible.",
                },
                {
                    "role": "user",
                    "content": f"[The Start of Reference Chapter]\n{self.reference_text}\n[The End of Reference Chapter]\n\n[The Start of Modified Chapter]\n{PLLM.final_draft}\n[The End of Modified Chapter]",
                },
            ],
            response_format=Evals,
        )

        res = completion.choices[0].message.parsed

        for eval in res.evals:
            PLLM.judge_score += f"# Evaluation category: {eval.category}\n\nScore: {eval.score}/3\n\nFeedback: {eval.explanation}\n\n"

        self._save_score(PLLM)


    def _save_feedback(self, PLLM) -> None:
        Path(f"{self.save_dir}/{PLLM.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{PLLM.name}/feedback.md", "w", encoding="utf-8") as file:
            file.write(PLLM.judge_feedback)
            logger.info(f"Judge feedback for {PLLM.name} saved in {self.save_dir}/{PLLM.name}/feedback.md")


    def _save_score(self, PLLM) -> None:
        Path(f"{self.save_dir}/{PLLM.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{PLLM.name}/score.md", "w", encoding="utf-8") as file:
            file.write(PLLM.judge_score)
            logger.info(f"Judge scores for {PLLM.name} saved in {self.save_dir}/{PLLM.name}/score.md")


    def _save_summary(self, PLLM, PLLM_other) -> None:
        Path(f"{self.save_dir}/{PLLM_other.name}").mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/{PLLM_other.name}/opp_summary.md", "w", encoding="utf-8") as file:
            file.write(PLLM_other.judge_summ_opp)
            logger.info(f"Judge summary for {PLLM.name} given to {PLLM_other.name} saved in {self.save_dir}/{PLLM_other.name}/opp_summary.md")


    def _save_verdict(self) -> None:
        Path(self.save_dir).mkdir(parents=True, exist_ok=True)
        with open(f"{self.save_dir}/verdict.txt", "w", encoding="utf-8") as file:
            verdict = f"Choice: {self.final_choice}\n\nExplanation:\n{self.final_explanation}"
            file.write(verdict)
            logger.info(f"Judge verdict saved in {self.save_dir}/verdict.txt")


if __name__ == "__main__":
    pass
