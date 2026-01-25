Spam Email Detection using Decision Tree

This project implements a Spam Detection System using Machine Learning in Python.
It uses text vectorization (Bag of Words) and a Decision Tree Classifier to classify emails as:

Spam

Ham (Not Spam)

The model is trained on a dataset (emails.csv) and evaluated using a confusion matrix.

## Project Structure
Spam_Detection/
│
├── spam_classifier.py
├── emails.csv
└── README.md

## Dataset Format (emails.csv)

The CSV file must contain two columns:

message,label


Where:

message → email text

label → spam or ham

Example:
Win free prize now,spam
Hello how are you,ham

# Libraries Used

pandas

matplotlib

scikit-learn

## How to Run the Project
1. Install required packages

Run:

pip install pandas matplotlib scikit-learn

2. Execute the script

Open terminal in the project folder:

python Spam_filter.py

# Workflow

Load email dataset using pandas

Convert labels (spam / ham) into numeric form

Vectorize text using CountVectorizer

Split data into training and testing sets

Train a Decision Tree classifier

Predict on test data

Display Confusion Matrix

Test with a new custom email message

# Output

Printed Confusion Matrix

Graphical Confusion Matrix plot

Prediction for custom message:

Prediction: SPAM

or

Prediction: HAM

# Limitations

Uses simple Bag-of-Words approach

Decision Tree may overfit on small datasets

No text preprocessing (stopword removal, stemming)

No model persistence (saving model)

## Author

Sandeep Aanjana

![Output Screenshot](output/Confusion.png)