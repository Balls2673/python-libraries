import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x = np.array([[1],
              [2],
              [3],
              [4],
              [5],
              [10]])
y = np.array([0,0,0,1,1,1])

model = LogisticRegression()
model.fit(x,y)

prediction = model.predict_proba([[1],
                            [2],
                            [3],
                            [4],
                            [5],
                            [6],
                            ])

print(prediction)



x_test = np.linspace(0,6,100).reshape(-1,1)

probabilities = model.predict_proba(x_test)[:,1]

plt.scatter(x, y)
plt.plot(x_test, probabilities)

plt.xlabel("Hours")
plt.ylabel("Probability")
plt.show()
