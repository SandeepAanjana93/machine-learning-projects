College Admission Prediction using Decision Tree

This project uses a Decision Tree Classifier from scikit-learn to predict whether a student will get admission based on:

Percentage in 12th grade

Entrance Exam result

Category

The output is:

Admission: Yes / No

## Dataset Requirements (collage.csv)

The CSV file must contain the following columns:
Column Name	Description	Values

Percentage12th	12th Percentage category	Low / Medium / High
EntranceExam	Entrance test result	    Pass / Fail
Category	    Student category	        General / Reserved
Admission	    Final decision	            Yes / No

## Encoding Used

Categorical values are converted into numbers:
# Percentage12th

Low → 0

Medium → 2

High → 1

# EntranceExam

Pass → 1

Fail → 0

# Category

General → 1

Reserved → 0

# Admission

Yes → 1

No → 0

## Requirements

Install required libraries:

pip install pandas scikit-learn

## How to Run

1. Place collage.csv in the same folder as the Python script

2. Run the program:

python collage.py


3. The output will be:

predicted result is:  [1]


1 means Admission = Yes
0 means Admission = No

# Prediction Example

The following input is used in the code:

dtree.predict([[2, 1, 1]])

Which means:

Percentage12th = Medium

EntranceExam = Pass

Category = General

# Model Used

Algorithm: Decision Tree Classifier

Library: scikit-learn

## Author

Sandeep Aanjana

![Output Screenshot](output/collage.png)