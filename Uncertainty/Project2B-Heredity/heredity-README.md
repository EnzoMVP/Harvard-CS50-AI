# Heredity

An AI that assesses the likelihood a person has a particular genetic trait, using a Bayesian Network over family trees and Bayes' rule.

## What it does

Given a family's data (who's whose parent, and who is observed to have a trait like hearing impairment), the program computes the full probability distribution — for every person — over how many copies of a gene they have (0, 1, or 2) and whether they express the trait, accounting for inheritance probabilities and random mutation.

## My implementation

- `joint_probability`: computes the joint probability of one specific full scenario (gene counts + trait for everyone), handling both people with no parents in the dataset (using population priors) and people with parents (combining each parent's gene-passing probability, including mutation)
- `update`: accumulates a computed joint probability into each person's running gene/trait distribution
- `normalize`: scales each person's final distributions so they sum to 1

## Run it

```
python heredity.py data/family0.csv
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Uncertainty
