# PeTII
Personalizing Textbooks on Individual Interests

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

## Running (Example)
Personalizing UC Berkeley CS61B Chapter 4 on astrophysics interest
```
python main.py -c og-textbooks/berkeley-cs61b/4.-sllists.md -i astrophysics
```
