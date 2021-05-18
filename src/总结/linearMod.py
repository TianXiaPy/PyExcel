import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
print(X)
y = np.dot(X, np.array([1, 2]))
# y = np.array([2, 6, 8, 10])
print(y)
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[20, 2]])))
