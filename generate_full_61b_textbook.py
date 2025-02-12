from gen import main
from pathlib import Path
from tqdm import tqdm

# DFS go through every file in og-textbooks/berkeley-cs61b, and find all .md files
if __name__ == "__main__":
    INTERESTS = ["astrophysics", "chemistry", "history"]
    files = list(Path("og-textbooks/berkeley-cs61b").rglob("*.md"))
    for interest in INTERESTS:
        for file in tqdm(files, desc="total markdown files"):
            print(file)
            main(str(file), interest, "complete")
