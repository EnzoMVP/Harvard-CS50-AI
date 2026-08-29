# Knights

An AI that solves Knights and Knaves logic puzzles using propositional logic and model checking.

## What it does

Each character in the puzzle is either a Knight (always tells the truth) or a Knave (always lies). Given what each character says, the program uses `model_check` to deduce, with logical certainty, who is a Knight and who is a Knave — for four increasingly complex puzzles.

## My implementation

- `knowledge0` through `knowledge3`: translated each puzzle's game structure (each character is exactly one of Knight/Knave) and each character's statement into propositional logic (`And`, `Or`, `Not`, `Biconditional`), letting `model_check` derive the solution rather than hardcoding the answer

## Starter code (not mine)

- `logic.py` (Symbol, And, Or, Not, Implication, Biconditional classes, and the `model_check` algorithm)

## Run it

```
python puzzle.py
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Knowledge
