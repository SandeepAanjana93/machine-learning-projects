import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("repair.csv")

P = {'Low': 0, 'High': 1}
df['Repair_Cost'] = df['Repair_Cost'].map(P)
E = {'New': 1, 'Old': 0}
df['Phone_Age'] = df['Phone_Age'].map(E)
C = {'Premium': 1, 'Normal': 0}
df['Brand_Type'] = df['Brand_Type'].map(C)
A = {'Repair': 1, 'Replace': 0}
df['Decision'] = df['Decision'].map(A)

features = ['Phone_Age','Repair_Cost','Brand_Type']

x = df[features]
y = df['Decision']

dtree = DecisionTreeClassifier()
dtree.fit(x, y)
predict = dtree.predict([[2,1,1]])
print("predicted result is: ",predict)