# Nim

An AI that teaches itself to play Nim through reinforcement learning (Q-learning), by playing thousands of games against itself.

## What it does

Learns a Q-value for every (state, action) pair — where a state is the current pile sizes and an action is "take N objects from pile i" — purely from experience: no strategy is hardcoded. After training (e.g. 10,000 self-play games), it plays close to optimally against a human.

## My implementation

- `get_q_value`, `update_q_value`: read/write the Q-value table, applying the Q-learning update formula (`old value + alpha * (reward + future reward - old value)`)
- `best_future_reward`: looks ahead at all actions available in a state and returns the best known Q-value among them (0 for unseen actions)
- `choose_action`: implements the epsilon-greedy strategy — mostly picks the best known action, occasionally explores randomly

## Starter code (not mine)

- `Nim` class (game rules) and the `train`/`play` functions

## Run it

```
python play.py
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Learning
