from dotenv import load_dotenv
from argparse import ArgumentParser
from datetime import datetime
from loguru import logger
from pathlib import Path

from pipeline import pipeline
from utils import read


def main(content_one:str, content_two:str, user_interest:str, save_dir:str):
    # Initialize LLMs (Personalization LLM types don't matter)
    p_a_llm = pipeline.CoP("A", user_interest, "", save_dir)
    p_a_llm.final_draft = content_one

    p_b_llm = pipeline.ChP("B", user_interest, "", save_dir)
    p_b_llm.final_draft = content_two

    j_llm = pipeline.Judge(user_interest, "", save_dir)

    # Eval outputs
    j_llm.compare(p_a_llm, p_b_llm)
    j_llm.score(p_a_llm)
    j_llm.score(p_b_llm)


if __name__ == "__main__":
    load_dotenv()

    parser = ArgumentParser()
    parser.add_argument("-a", dest="content_one", help="path/to/final_draft_one.md", required=True)
    parser.add_argument("-b", dest="content_two", help="path/to/final_draft_two.md", required=True)
    parser.add_argument("-i", "--interest", dest="interest", help="Your personal/professional interest", required=True)
    args = parser.parse_args()

    curr_date = datetime.now()
    save_dir = f"evals/{curr_date.year}{curr_date.month}{curr_date.day}{curr_date.time().hour}{curr_date.time().minute}{curr_date.time().second}"

    # Document final draft paths
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    with open(f"{save_dir}/final_draft_paths.txt", "w", encoding="utf-8") as file:
        file.write(f"A: {args.content_one}\nB: {args.content_two}")
        logger.info(f"Final draft paths used logged in {save_dir}/final_draft_paths.txt")

    # Read final draft contents
    content_one = read(args.content_one)
    content_two = read(args.content_two)

    main(content_one, content_two, args.interest, save_dir)
