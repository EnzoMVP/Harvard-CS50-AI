# Traffic

A convolutional neural network (CNN) that classifies German traffic sign images (GTSRB dataset, 43 categories) using TensorFlow.

## What it does

Loads and resizes thousands of labeled road sign images, trains a CNN to classify them into one of 43 sign types, and reports accuracy on held-out test data.

## My implementation

- `load_data`: reads every image from the labeled subdirectories using OpenCV, resizing each to a fixed `IMG_WIDTH x IMG_HEIGHT`
- `get_model`: builds and compiles a CNN — convolution + pooling layers (including a "Conv-Conv-Pool" block, found through experimentation to train more stably than a single convolution per pooling stage), a flatten step, a dense hidden layer with dropout, and a softmax output layer for the 43 categories
- `model_metrics.py` (extra, not required by the spec): loads a saved trained model and generates a confusion matrix and per-category precision/recall/F1 report, to diagnose which sign categories the model confuses most

See `EXPERIMENTS.md` for the full experimentation log (architectures tried, what worked, what didn't, and why some configurations suffered from "dead ReLU" on certain random initializations).

## Run it

```
pip3 install -r requirements.txt
python traffic.py gtsrb
```

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) — Neural Networks
