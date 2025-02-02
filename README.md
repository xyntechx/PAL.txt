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
python gen.py -c path/to/original_chapter.md -i "<user interest>" -s "<strategy>"
```

Evaluate/compare personalized chapters
```
python eval.py -a path/to/final_draft_one.md -b path/to/final_draft_two.md -i "user interest"
```



- understand student profile
- understand how to best explain CS to this particular student
- personalize structure-based






LLM A: Simulate student judge
LLM B: Simulate CS professor judge
LLM C: PS

Given a student's bio, extract interest

PS personalize -> LLM A gives feedback & LLM B gives feedback -> PS improve personalization based on both feedbacks (2-step)

"How would you introduce the CS concept of static variables vs instance variables to a student interested in astrophysics?"
"Introduce the CS concept of static variables vs instance variables to a student interested in astrophysics."


Can we just have both? So one structurally similar one and another that is more analogy-driven?

have an relation section at the end of the final draft that is just one/two-paragraph analogies per concept -- analogy paras dont need code