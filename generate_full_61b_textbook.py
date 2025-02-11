from gen import main
from pathlib import Path

# DFS go through every file in og-textbooks/berkeley-cs61b, and find all .md files
if __name__ == "__main__":
    INTERESTS = ["astrophysics", "chemistry", "history"]
    for interest in INTERESTS:
        for file in Path("og-textbooks/berkeley-cs61b").rglob("*.md"):
            print(file)
            main(file, interest, "complete")
