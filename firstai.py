import numpy as np
import matplotlib.pyplot as plt


y_true = np.array([5,7,9,11])
y_pred = np.array([5,7,9,15])

error = (y_true - y_pred) **2

print(error)
print("tottal error = ", error.sum())