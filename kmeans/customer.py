import pandas
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

df = pandas.read_csv("customerData.csv")

x = df['Age']
y = df['AnnualIncome(L)']
z = df['SpendingScore']

data = list(zip(x,y,z))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
print(inertias)
    
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

plt.scatter(x, y, z, c=kmeans.labels_)
# ax.set_xlabel("Age")
# ax.set_ylabel("AnnualIncome(L)")
# ax.set_zlabel("Spending Score")
plt.show()
