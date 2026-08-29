# Crossword

An AI that generates crossword puzzles by modeling the problem as a Constraint Satisfaction Problem (CSP) and solving it with backtracking search.

## What it does

Given a crossword structure and a word list, each blank sequence of squares is a variable whose domain is the set of words that fit its length (unary constraint) and that don't conflict with overlapping neighboring words (binary constraint). The AI enforces node and arc consistency (AC-3), then uses backtracking search — with the MRV/degree heuristics for variable selection and least-constraining-value for value ordering — to find a satisfying assignment.

## My implementation

- `enforce_node_consistency`, `revise`, `ac3`: constraint propagation, reducing domains before search
- `assignment_complete`, `consistent`: checks used during search
- `order_domain_values`: orders a variable's domain by least-constraining-value
- `select_unassigned_variable`: picks the next variable via MRV, breaking ties by degree
- `backtrack`: the recursive backtracking search itself

## Starter code (not mine)

- `crossword.py` (Variable and Crossword classes, overlap computation)

## Run it

```
python generate.py data/structure1.txt data/words1.txt output.png
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Optimization
