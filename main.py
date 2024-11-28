from dotenv import load_dotenv
from argparse import ArgumentParser
from datetime import datetime
from loguru import logger

from pipeline import pipeline
from utils import read


def main(og_chapter_src:str, user_interest:str):
    # Read original chapter markdown
    reference_text = read(og_chapter_src)

    # Setting logistics
    course_name, chapter_title = og_chapter_src.split("/")[1:3]
    chapter_title = "-".join(chapter_title.split(".")[:-1])
    curr_date = datetime.now()
    save_dir = f"output/{course_name}/{chapter_title}/{curr_date.year}{curr_date.month}{curr_date.day}"

    # Initialize LLMs
    p_a_llm = pipeline.CoP("A", user_interest, reference_text, save_dir)
    p_b_llm = pipeline.ChP("B", user_interest, reference_text, save_dir)
    j_llm = pipeline.Judge(user_interest, reference_text, save_dir)

    # Run content-by-content Personalization LLM -- draft
    p_a_llm.extract_concepts()
    p_a_llm.create_overview()
    p_a_llm.personalize()

    # Give feedback to content-by-content Personalization LLM
    j_llm.give_feedback(p_a_llm)

    # Run whole-chapter Personalization LLM -- draft
    p_b_llm.personalize()

    # Give feedback to whole-chapter Personalization LLM
    j_llm.give_feedback(p_b_llm)

    # Run content-by-content Personalization LLM -- refinement
    p_a_llm.refine()

    # Run whole-chapter Personalization LLM -- refinement
    p_b_llm.refine()

    # Compare refined drafts
    j_llm.compare(p_a_llm, p_b_llm)

    logger.success(f"Personalization completed! All work is saved in {save_dir}")


if __name__ == "__main__":
    load_dotenv()

    parser = ArgumentParser()
    parser.add_argument("-c", "--chapter", dest="chapter", help="The original textbook chapter to personalize", required=True)
    parser.add_argument("-i", "--interest", dest="interest", help="Your personal/professional interest", required=True)
    args = parser.parse_args()

    main(args.chapter, args.interest)
