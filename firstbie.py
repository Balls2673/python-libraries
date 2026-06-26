from sklearn.linear_model import LinearRegression
import numpy as np

x= np.array([[1],[2], [3], [4]])
y = np.array([5,7,9,15])

model = LinearRegression()

model.fit(x, y)

a = model.coef_[0]
b = model.intercept_

print("a =", a)
print("b =", b)