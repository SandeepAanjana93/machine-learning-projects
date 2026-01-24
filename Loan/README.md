Loan Approval Prediction using Decision Tree

This project uses a Decision Tree Classifier to predict whether a loan application will be approved based on:

Income Level

CIBIL Score

Job Type

The output is:

Loan Approved: Yes / No

## Dataset Requirements (loan.csv)

The CSV file must contain the following columns:
Column Name	Description	Values

Income_Level	Income category	     Low / Medium / High
CIBIL_Score	    Credit score status	 Good / Bad
Job_Type	    Employment type	     Govt / Private
Loan_Approved	Final decision	     Yes / No

## Encoding Used

Categorical values are converted into numbers:

# Income_Level

Low → 0

High → 1

Medium → 2

# CIBIL_Score

Good → 1

Bad → 0

# Job_Type

Private → 1

Govt → 0

# Loan_Approved

Yes → 1

No → 0

## Requirements

Install required libraries:

pip install pandas scikit-learn

## How to Run

1. Place loan.csv in the same folder as the Python script

2. Run the program:

python loan_approvel.py

3. Example output:

predicted result is:  [1]


1 = Loan Approved
0 = Loan Not Approved

# Prediction Example

The following input is used in the code:

dtree.predict([[2, 1, 1]])


Which means:

Income_Level = Medium

CIBIL_Score = Good

Job_Type = Private

# Model Information

Algorithm: Decision Tree Classifier

Library: scikit-learn

## Author

Sandeep Aanjana

![Output Screenshot](output/loan.png)