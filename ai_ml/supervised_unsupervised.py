from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)
print("Supervised prediction:", model.predict([[5]]))

