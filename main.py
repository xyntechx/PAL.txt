from openai import OpenAI

from dotenv import load_dotenv
from argparse import ArgumentParser
from pathlib import Path
from tqdm import tqdm

from pipeline import extract_concepts, create_overview, personalize
from utils import read


def main(og_chapter_src:str, user_interest:str):
    load_dotenv()

    # Create Personalization LLM
    p_client = OpenAI()
    # Create Judge LLM
    j_client = OpenAI() # TODO: implement + make togglable for testing

    # Read original chapter markdown
    content = read(og_chapter_src)

    # Extract the programming language (if any) and technical concepts from the original chapter
    print("Extracting concepts...")
    language, concepts = extract_concepts(p_client, content)
    print(f"Language: {language}\tConcepts: {concepts}")

    # First pass to Personalization LLM -- concept-by-concept
    print("Crafting overview...")
    draft = create_overview(p_client, concepts) + "\n\n"

    print("Personalizing concept-by-concept...")
    for concept in tqdm(concepts):
        section = personalize(p_client, language, concept, user_interest)
        draft += section + "\n\n"

    # Save personalized chapter as a markdown file
    course_name, chapter_title = og_chapter_src.split("/")[1:3]
    save_dir = f"personalized-textbooks/{course_name}"
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    with open(f"{save_dir}/{chapter_title}", "w") as file:
        file.write(draft)
        print(f"Draft saved in {save_dir}/{chapter_title}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--chapter", dest="chapter", help="The original textbook chapter to personalize", required=True)
    parser.add_argument("-i", "--interest", dest="interest", help="Your personal/professional interest", required=True)
    args = parser.parse_args()

    main(args.chapter, args.interest)
