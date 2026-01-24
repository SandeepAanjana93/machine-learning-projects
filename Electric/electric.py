import pandas as pd
from sklearn import linear_model

df = pd.read_csv("bill.csv")

x = df[["AC_Usage","UnitsConsumed"]]
y = df["MonthlyBill"]

reg = linear_model.LinearRegression()
reg.fit(x,y)
bill = reg.predict([[9,350]])
print("total predicted electricity bill: ",round(bill[0],2))