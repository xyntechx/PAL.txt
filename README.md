# PAL.txt
Personalizations for Associative Learning on Textbooks

## Setup
Create virtual env
```
python -m venv .venv
```

Install packages
```
pip install --upgrade pip wheel
pip install -r requirements.txt
```

## Usage

Generate personalized chapter(s)
```
python gen.py -c path/to/original_chapter.md -i "user interest"
```

Evaluate/compare personalized chapters
```
python eval.py -a path/to/final_draft_one.md -b path/to/final_draft_two.md -i "user interest"
```
