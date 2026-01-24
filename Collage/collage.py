import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("collage.csv")

P = {'Low': 0, 'High': 1, 'Medium': 2}
df['Percentage12th'] = df['Percentage12th'].map(P)
E = {'Pass': 1, 'Fail': 0}
df['EntranceExam'] = df['EntranceExam'].map(E)
C = {'General': 1, 'Reserved': 0}
df['Category'] = df['Category'].map(C)
A = {'Yes': 1, 'No': 0}
df['Admission'] = df['Admission'].map(A)

features = ['Percentage12th','EntranceExam','Category']

x = df[features]
y = df['Admission']

dtree = DecisionTreeClassifier()
dtree.fit(x, y)
predict = dtree.predict([[2,1,1]])
print("predicted result is: ",predict)