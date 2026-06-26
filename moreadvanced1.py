import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = np.array([4, 7, 10, 50])

a = 0
b = 0
learning_rate = 0.01
max_iter = 100  # أفضل اسم

plt.scatter(x, y, color='blue')  # النقاط الحقيقية

for i in range(max_iter):
    y_pred = a*x + b
    error = y - y_pred  # الفرق مع الاتجاه (Gradient)
    error = np.clip(error, -10,10)
    a = a + learning_rate * (error * x).mean()
    b = b + learning_rate * ( error).mean()

    plt.plot(x, y_pred, color='red', alpha=0.3)

    if abs(error.mean()) < 0.01:  # شرط التوقف
        break

# التنبؤ للقيمة الجديدة
new_x = float(input("Enter x: "))
prediction = a * new_x + b
print("Predicted y =", prediction)

# الخط النهائي
plt.plot(x, a*x + b, color='red', linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# قيم a و b النهائية
print("a =", a)
print("b =", b)