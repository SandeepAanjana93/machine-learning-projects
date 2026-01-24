import pandas as pd 
from sklearn import linear_model

df = pd.read_csv("mobile.csv")

x = df[["ScreenTime","Brightness"]]
y = df[["BatteryBackup"]]

reg = linear_model.LinearRegression()
reg.fit(x,y)
backup = reg.predict([[8,65]])
print("predicted battery backup: ",backup)