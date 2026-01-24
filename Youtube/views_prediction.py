import pandas as pd
from sklearn import linear_model

df = pd.read_csv("youtube.csv")

x = df[["ThumbnailQuality","PostingTime"]]
y = df[["Views24Hours"]]

reg = linear_model.LinearRegression()
reg.fit(x,y)
view = reg.predict([[7,4]])
print("views on video in 24 hours",view)