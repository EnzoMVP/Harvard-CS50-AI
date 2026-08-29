# PageRank

An AI that ranks web pages by importance, using two different approaches: sampling a Markov Chain random surfer, and iteratively applying the PageRank formula.

## What it does

Given a corpus of interlinked web pages, it estimates each page's PageRank two ways:
1. **Sampling**: simulates a random surfer clicking links (with a damping factor for teleporting to a random page), and counts visit frequency across many samples
2. **Iteration**: repeatedly recalculates each page's rank from the current ranks of pages linking to it, until the values converge

## My implementation

- `transition_model`: computes the probability distribution over which page to visit next, given the damping factor
- `sample_pagerank`: builds the Markov chain of samples and estimates rank as visit frequency
- `iterate_pagerank`: applies the PageRank formula repeatedly until convergence (< 0.001 change)

## Starter code (not mine)

- `crawl` function (parses HTML files into a corpus dictionary)

## Run it

```
python pagerank.py corpus0
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Uncertainty
