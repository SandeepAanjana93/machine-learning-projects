import pandas as pd
from sklearn import linear_model

df = pd.read_csv("student.csv")

x = df[["StudyHr","PreexamMark"]]
y = df[["FinalMarks"]]

regr = linear_model.LinearRegression()
regr.fit(x,y)

predict = regr.predict([[4,67]])
print("predicted score is: ",predict)