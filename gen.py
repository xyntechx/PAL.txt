from dotenv import load_dotenv
from argparse import ArgumentParser
from datetime import datetime
from loguru import logger
from pathlib import Path

from pipeline import pipeline
from utils import read


def no_recomp(reference_text:str, user_interest:str, save_dir:str):
    # Initialize LLMs
    p_a_llm = pipeline.PC("A", user_interest, reference_text, save_dir)
    p_b_llm = pipeline.PS("B", user_interest, reference_text, save_dir)
    j_llm = pipeline.Judge(user_interest, reference_text, save_dir)

    # Run content-by-content Personalization LLM -- draft
    p_a_llm.extract_concepts()
    p_a_llm.write_outline()
    p_a_llm.create_overview()
    p_a_llm.personalize(with_outline=True)

    # Give feedback to content-by-content Personalization LLM
    j_llm.give_feedback(p_a_llm, PLLM_other=p_b_llm)

    # Run whole-chapter Personalization LLM -- draft
    p_b_llm.extract_sections()
    p_b_llm.personalize()
    p_b_llm.create_overview()

    # Give feedback to whole-chapter Personalization LLM
    j_llm.give_feedback(p_b_llm, PLLM_other=p_a_llm)

    # Run content-by-content Personalization LLM -- refinement
    p_a_llm.refine()

    # Run whole-chapter Personalization LLM -- refinement
    p_b_llm.refine()

    # Compare refined drafts
    j_llm.compare(p_a_llm, p_b_llm)

    # Score each PLLM's final drafts
    j_llm.score(p_a_llm)
    j_llm.score(p_b_llm)


def complete(reference_text:str, user_interest:str, save_dir:str):
    # Initialize LLMs
    p_a_llm = pipeline.PC("A", user_interest, reference_text, save_dir)
    p_b_llm = pipeline.PS("B", user_interest, reference_text, save_dir)
    j_llm = pipeline.Judge(user_interest, reference_text, save_dir)

    # Creating analogy-driven text
    p_a_llm.extract_concepts()
    p_a_llm.create_analogies()

    # Personalize first-pass
    p_b_llm.personalize()
    p_b_llm.extract_sections()
    p_b_llm.insert_analogies(p_a_llm)

    # LLM-as-a-Judge with simulation (student & expert)
    j_llm.give_feedback_student(p_b_llm)
    j_llm.give_feedback_expert(p_b_llm)

    # Improve based on feedback
    p_b_llm.refine_student()
    p_b_llm.refine_expert()
    p_b_llm.finalize()

def no_analogy(reference_text:str, user_interest:str, save_dir:str):
    # Initialize LLMs
    p_b_llm = pipeline.PS("B", user_interest, reference_text, save_dir)
    j_llm = pipeline.Judge(user_interest, reference_text, save_dir)

    # Personalize first-pass
    p_b_llm.personalize()
    p_b_llm.extract_sections()

    # LLM-as-a-Judge with simulation (student & expert)
    j_llm.give_feedback_student(p_b_llm)
    j_llm.give_feedback_expert(p_b_llm)

    # Improve based on feedback
    p_b_llm.refine_student()
    p_b_llm.refine_expert()
    p_b_llm.finalize()

def no_feedback(reference_text:str, user_interest:str, save_dir:str):
        # Initialize LLMs
    p_a_llm = pipeline.PC("A", user_interest, reference_text, save_dir)
    p_b_llm = pipeline.PS("B", user_interest, reference_text, save_dir)
    j_llm = pipeline.Judge(user_interest, reference_text, save_dir)

    # Creating analogy-driven text
    p_a_llm.extract_concepts()
    p_a_llm.create_analogies()

    # Personalize first-pass
    p_b_llm.personalize()
    p_b_llm.extract_sections()
    p_b_llm.insert_analogies(p_a_llm)

    p_b_llm.finalize()

def main(og_chapter_src:str, user_interest:str, strategy_name:str):
    # Get relevant strategy function
    strategy = STRATEGIES[strategy_name]

    # Read original chapter markdown
    reference_text = read(og_chapter_src)

    # Setting logistics
    course_name, chapter_title = og_chapter_src.split("/")[1:3]
    chapter_title = "-".join(chapter_title.split(".")[:-1])
    curr_date = datetime.now()
    timestamp_str = curr_date.strftime("%Y-%m-%d_%H-%M-%S")
    save_dir = f"output/{course_name}/{chapter_title}/{timestamp_str}"

    # Document execution strategy
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    with open(f"{save_dir}/strategy.txt", "w", encoding="utf-8") as file:
        file.write(f"Strategy: {strategy_name}")
        logger.info(f"Strategy logged in {save_dir}/strategy.txt")

    strategy(reference_text, user_interest, save_dir)
    logger.success(f"Personalization completed! All work is saved in {save_dir}")


if __name__ == "__main__":
    load_dotenv()

    STRATEGIES = {
        "complete": complete, # all components included
        "no_recomp": no_recomp, # all components included except Reinforcement Competition
        "no_analogy": no_analogy, # all components included except Analogy Creation
        "no_feedback": no_feedback, # all components included except Feedback
    }

    parser = ArgumentParser()
    parser.add_argument("-c", "--chapter", dest="chapter", help="The original textbook chapter to personalize", required=True)
    parser.add_argument("-i", "--interest", dest="interest", help="Your personal/professional interest", required=True)
    parser.add_argument("-s", "--strategy", dest="strategy", help="Execution strategy", required=True, choices=list(STRATEGIES.keys()))
    args = parser.parse_args()

    main(args.chapter, args.interest, args.strategy)
