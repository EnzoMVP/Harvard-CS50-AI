import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

TEST_SIZE = 0.4

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    df = pd.read_csv(filename)
    evidence = df.drop("Revenue", axis=1)
    label = df["Revenue"]

    evidence["Administrative"] = evidence["Administrative"].astype(int)
    evidence["Administrative_Duration"] = evidence["Administrative_Duration"].astype(float)
    evidence["Informational"] = evidence["Informational"].astype(int)
    evidence["Informational_Duration"] = evidence["Informational_Duration"].astype(float)
    evidence["ProductRelated"] = evidence["ProductRelated"].astype(int)
    evidence["ProductRelated_Duration"] = evidence["ProductRelated_Duration"].astype(float)
    evidence["BounceRates"] = evidence["BounceRates"].astype(float)
    evidence["ExitRates"] = evidence["ExitRates"].astype(float)
    evidence["PageValues"] = evidence["PageValues"].astype(float)
    evidence["SpecialDay"] = evidence["SpecialDay"].astype(float)
    evidence["Month"] = evidence["Month"].map({"Jan": 0,
                                               "Feb": 1,
                                               "Mar": 2,
                                               "Apr": 3,
                                               "May": 4,
                                               "June": 5,
                                               "Jul": 6,
                                               "Aug": 7,
                                               "Sep": 8,
                                               "Oct": 9,
                                               "Nov": 10,
                                               "Dec": 11})
    evidence["OperatingSystems"] = evidence["OperatingSystems"].astype(int)
    evidence["Browser"] = evidence["Browser"].astype(int)
    evidence["Region"] = evidence["Region"].astype(int)
    evidence["TrafficType"] = evidence["TrafficType"].astype(int)
    evidence["VisitorType"] = evidence["VisitorType"].map({"Returning_Visitor": 1, "New_Visitor": 0, "Other": 0})
    evidence["Weekend"] = evidence["Weekend"].map({False: 0, True: 1})
    evidence = evidence.values.tolist()

    label = label.map({True: 1,
                        False: 0})
    label = label.values.tolist()

    return evidence, label

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total = 0
    purchased = 0
    didnt_purchased = 0
    true_positives = 0
    true_negatives = 0
    for actual, predict in zip(labels, predictions):
        total += 1
        if actual == 1:
            purchased += 1
            if predict == actual:
                true_positives += 1
        elif actual == 0:
            didnt_purchased += 1
            if predict == actual:
                true_negatives += 1

    sensitivity = true_positives / purchased
    specificity = true_negatives / didnt_purchased
    return sensitivity, specificity

if __name__ == "__main__":
    main()
