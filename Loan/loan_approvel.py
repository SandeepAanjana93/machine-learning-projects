import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv("loan.csv")

P = {'Low': 0, 'High': 1, 'Medium': 2}
df['Income_Level'] = df['Income_Level'].map(P)
E = {'Good': 1, 'Bad': 0}
df['CIBIL_Score'] = df['CIBIL_Score'].map(E)
C = {'Private': 1, 'Govt': 0}
df['Job_Type'] = df['Job_Type'].map(C)
A = {'Yes': 1, 'No': 0}
df['Loan_Approved'] = df['Loan_Approved'].map(A)

features = ['Income_Level','CIBIL_Score','Job_Type']

x = df[features]
y = df['Loan_Approved']

dtree = DecisionTreeClassifier()
dtree.fit(x, y)
predict = dtree.predict([[2,1,1]])
print("predicted result is: ",predict)