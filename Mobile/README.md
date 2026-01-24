Mobile Battery Backup Prediction using Linear Regression

This project uses Linear Regression from scikit-learn to predict a mobile phone’s battery backup based on:

Screen Time

Brightness Level

Background Apps

The output is:

 Predicted Battery Backup (in hours)

## Dataset Requirements (mobile.csv)

The CSV file must contain the following columns:
Column Name	Description

ScreenTime	    Screen usage time       (hours)
Brightness	    Screen brightness       (%)
BatteryBackup	Battery backup duration (hours)

## Requirements

Install required libraries:

pip install pandas scikit-learn

# How to Run

1. Place mobile.csv in the same folder as the Python script

2. Run the program:

python battery_health.py

3. Example output:

predicted battery backup:  [[4.23]]


(Value may vary depending on training data.)

# Prediction Example

The following input is used in the code:

reg.predict([[8, 65]])


Which means:

Screen Time = 8 hours

Brightness = 65%

# Model Information

Algorithm: Linear Regression

Library: scikit-learn

## Author

Sandeep Aanjana

![Output Screenshot](output/mobile.png)