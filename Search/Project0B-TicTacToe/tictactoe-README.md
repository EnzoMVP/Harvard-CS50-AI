# Tic-Tac-Toe

An AI that plays Tic-Tac-Toe optimally using the Minimax algorithm with alpha-beta pruning.

## What it does

Implements the full game logic (whose turn it is, valid moves, applying a move, checking for a winner/tie) plus a Minimax search that always finds the optimal move — meaning a human can never beat it, only tie or lose.

## My implementation

- `player`, `actions`, `result`, `winner`, `terminal`, `utility`: core game logic
- `minimax`: full recursive Minimax with `max_value`/`min_value` helper functions, including alpha-beta pruning for efficiency

## Starter code (not mine)

- `runner.py` (pygame graphical interface)

## Run it

```
pip3 install -r requirements.txt
python runner.py
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Search
