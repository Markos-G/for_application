import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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
        -0 Administrative, an integer
        -1 Administrative_Duration, a floating point number
        -2 Informational, an integer
        -3 Informational_Duration, a floating point number
        -4 ProductRelated, an integer
        -5 ProductRelated_Duration, a floating point number
        -6 BounceRates, a floating point number
        -7 ExitRates, a floating point number
        -8 PageValues, a floating point number
        -9 SpecialDay, a floating point number
        -10 Month, an index from 0 (January) to 11 (December)
        -11 OperatingSystems, an integer
        -12 Browser, an integer
        -13 Region, an integer
        -14 TrafficType, an integer
        -15 VisitorType, an integer 0 (not returning) or 1 (returning)
        -16 Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    months ={'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3,
            'May': 4,'June': 5, 'Jul': 6, 'Aug': 7,
            'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11,
            }
    evidence = []
    labels = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            evidence.append([int(row['Administrative']),
                            float(row['Administrative_Duration']),
                            int(row['Informational']),
                            float(row['Informational_Duration']),
                            int(row['ProductRelated']),
                            float(row['ProductRelated_Duration']),
                            float(row['BounceRates']),
                            float(row['ExitRates']),
                            float(row['PageValues']),
                            float(row['SpecialDay']),
                            months[row['Month']],
                            int(row['OperatingSystems']),
                            int(row['Browser']),
                            int(row['Region']),
                            int(row['TrafficType']),
                            1 if row['VisitorType'] == 'Returning_Visitor' else 0,
                            1 if row['Weekend'] == 'TRUE' else 0
                            ])
            labels.append(1 if row['Revenue'] == 'TRUE' else 0)

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    return model.fit(evidence, labels)


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
    total0, total1, correct0, correct1 = 0.0, 0.0, 0.0, 0.0
    for label, prediction in zip(labels, predictions):
        if label == 0:
            total0 += 1
            if label == prediction:
                correct0 += 1
        elif label == 1:
            total1 += 1
            if label == prediction:
                correct1 += 1

    sensitivity = correct1 / total1
    specificity = correct0 / total0
    return sensitivity, specificity
    

if __name__ == "__main__":
    main()


