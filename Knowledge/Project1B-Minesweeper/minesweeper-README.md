# Minesweeper

An AI that plays Minesweeper using knowledge-based inference, representing each revealed cell as a logical sentence of the form `{cells} = count`.

## What it does

Every time a safe cell is clicked, the AI adds a new sentence to its knowledge base (its neighboring cells and how many of them are mines). It then repeatedly infers new safe cells and mines — both from single sentences that become conclusive (count = 0 or count = number of cells) and by combining sentences via the subset method — looping until no new inferences can be made.

## My implementation

- `Sentence.known_mines`, `known_safes`, `mark_mine`, `mark_safe`: update a single logical sentence given new information
- `MinesweeperAI.add_knowledge`: the core inference engine — marks the cell, builds the new sentence (excluding already-known cells), then loops applying single-sentence inference and subset-based inference until reaching a fixed point
- `make_safe_move`, `make_random_move`: move selection

## Run it

```
pip3 install -r requirements.txt
python runner.py
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Knowledge
