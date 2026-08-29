# Shopping

A k-nearest-neighbor classifier that predicts whether an online shopping session will end in a purchase, evaluated by sensitivity (true positive rate) and specificity (true negative rate) rather than raw accuracy alone.

## What it does

Loads ~12,000 labeled shopping sessions (pages visited, bounce rates, visitor type, month, weekend, etc.), trains a k=1 nearest-neighbor model, and reports how well it distinguishes purchasers from non-purchasers on held-out data.

## My implementation

- `load_data`: parses the CSV into evidence/label lists, converting every column to the exact type the spec requires (int vs float, month name → index, boolean-like columns → 0/1)
- `train_model`: fits a `KNeighborsClassifier` with k=1
- `evaluate`: computes sensitivity and specificity from true vs predicted labels

## Run it

```
python shopping.py shopping.csv
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Learning
