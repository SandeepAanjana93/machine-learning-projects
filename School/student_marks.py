import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("school.csv")

P = {'Low': 0, 'High': 1, 'Medium': 2}
df['Attendance'] = df['Attendance'].map(P)
df['Study_Hours'] = df['Study_Hours'].map(P)
E = {'Pass': 1, 'Fail': 0}
df['Internal_Test_Result'] = df['Internal_Test_Result'].map(E)
df['Final_Result'] = df['Final_Result'].map(E)

features = ['Attendance','Study_Hours','Internal_Test_Result']

x = df[features]
y = df['Final_Result']

dtree = DecisionTreeClassifier()
dtree.fit(x, y)
predict = dtree.predict([[2,1,1]])
print("predicted result is: ",predict)