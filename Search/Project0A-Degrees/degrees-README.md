# Degrees of Separation

Finds the shortest path connecting two actors through movies they've starred in together, using breadth-first search (BFS) — inspired by the "Six Degrees of Kevin Bacon" game.

## What it does

Given two actor names, the program models the problem as a graph search: states are actors, actions are movies connecting them, and it returns the shortest chain of `(movie, person)` pairs linking the two.

## My implementation

- `shortest_path`: implemented the full BFS loop (frontier, explored set, path reconstruction by following parent nodes)

## Starter code (not mine)

- `util.py` (Node, StackFrontier, QueueFrontier classes)
- CSV loading and `neighbors_for_person` helper

## Run it

```
python degrees.py small
python degrees.py large
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Search
