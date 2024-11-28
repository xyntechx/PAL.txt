from openai import OpenAI

from dotenv import load_dotenv
from argparse import ArgumentParser
from pathlib import Path
from tqdm import tqdm
from datetime import datetime

from pipeline import extract_concepts, create_overview, personalize, judge, personalize_refine
from utils import read


def main(og_chapter_src:str, user_interest:str):
    load_dotenv()

    # Create Personalization LLM
    p_client = OpenAI()
    # Create Judge LLM
    j_client = OpenAI() # TODO: implement + make togglable for testing

    # Read original chapter markdown
    content = read(og_chapter_src)

    # Setting logistics
    course_name, chapter_title = og_chapter_src.split("/")[1:3]
    chapter_title = "-".join(chapter_title.split(".")[:-1])
    curr_date = datetime.now()
    save_dir = f"output/{course_name}/{chapter_title}/{curr_date.year}{curr_date.month}{curr_date.day}"
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    # # ? Feedback whole chapter below
    # # ? (draft is whole text)
    # # Evaluate first-pass personalization
    # print("Judge LLM giving feedback...")
    # feedback = ""
    # judge_evals = judge(j_client, user_interest, content, draft)
    # for eval in judge_evals:
    #     feedback += f"# Evaluation category: {eval.category}\n\nScore: {eval.score}/3\n\nFeedback: {eval.explanation}\n\n"
    
    # # Second pass to Personalization LLM
    # print("Improving personalization based on feedback...")
    # final_draft = personalize_refine(p_client, user_interest, draft, feedback)
    # # ? Feedback whole chapter above


    # Extract the programming language (if any) and technical concepts from the original chapter
    print("Extracting concepts...")
    language, concepts = extract_concepts(p_client, content)

    # Save specs as a txt file
    with open(f"{save_dir}/specs.txt", "w") as file:
        file.write(f"Language: {language}\n\nConcepts: {concepts}")
        print(f"Specs (language and concepts) saved in {save_dir}/specs.txt")

    # First pass to Personalization LLM -- create overview
    print("Crafting overview...")
    draft = [create_overview(p_client, concepts)]

    # First pass to Personalization LLM -- concept-by-concept personalization
    print("Personalizing concept-by-concept...")
    for concept in tqdm(concepts):
        section = personalize(p_client, language, concept, user_interest)
        draft.append(section)
    
    # Save draft personalized chapter as a markdown file
    with open(f"{save_dir}/draft.md", "w") as file:
        file.write("\n\n".join(draft))
        print(f"Draft personalized chapter saved in {save_dir}/draft.md")

    # ? Feedback concept-by-concept below
    # Evaluate first-pass personalization
    print("Judge LLM giving feedback...")
    feedback = ""
    judge_evals = judge(j_client, user_interest, content, "\n\n".join(draft))
    for eval in judge_evals:
        feedback += f"# Evaluation category: {eval.category}\n\nScore: {eval.score}/3\n\nFeedback: {eval.explanation}\n\n"
    
    # Save feedback as a markdown file
    with open(f"{save_dir}/feedback.md", "w") as file:
        file.write(feedback)
        print(f"Judge feedback saved in {save_dir}/feedback.md")

    # Second pass to Personalization LLM
    print("Improving personalization based on feedback...")
    final_draft = []
    for section in tqdm(draft[1:]): # exclude overview from refinement
        final_draft.append(personalize_refine(p_client, user_interest, section, feedback))
    # ? Feedback concept-by-concept above

    # Save final personalized chapter as a markdown file
    with open(f"{save_dir}/final_draft.md", "w") as file:
        file.write("\n\n".join(final_draft))
        print(f"Final personalized chapter saved in {save_dir}/final_draft.md")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--chapter", dest="chapter", help="The original textbook chapter to personalize", required=True)
    parser.add_argument("-i", "--interest", dest="interest", help="Your personal/professional interest", required=True)
    args = parser.parse_args()

    main(args.chapter, args.interest)
