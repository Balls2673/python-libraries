import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#scatterChart
# x = np.array([2023,2024,2025,2026])
# y1 = np.array([13,12,11,10])
# y2 = np.array([13,10,6,10])
# y3 = np.array([13,2,6,10])

# plt.scatter(x,y1, s=200, color="Blue", label ="Class A")
# plt.scatter(x,y2, s=200, color="Red", label ="Class B")
# plt.scatter(x,y3, s=200, color="Green", label ="Class C")
# plt.legend()
# plt.show()

# histChart

# scores = np.random.normal(loc=80 , scale=10,size= 100)
# scores = np.clip(scores, 20, 100)

# plt.hist(scores, bins = 20)
# plt.show()

# plt.grid(linewidth="2", color="green", linestyle="dashed")
# plt.title("Road trip", fontsize=15, family ="Arial" , fontweight = "bold")
# plt.xlabel("FREEDOM", fontweight="bold")
# plt.ylabel("DEMOCRASY",  fontweight="bold")
# plt.tick_params(axis="both", colors="red")
# Line_Style = dict( marker="v", markersize = "10", markerfacecolor = "cyan",markeredgecolor="Blue",linestyle="solid",linewidth="2")

# plt.plot(x,y1, **Line_Style)
# plt.plot(x,y2, **Line_Style)
# plt.plot(x,y3, **Line_Style)

#plt.show()


#BarChart
 
population  = 8303804326

precenteges = {"Adult":  0.45,"Chaildren": 0.25, "Teeens": 0.15, "Elder": 0.15}

result  = {}

for key , value in precenteges.items():
     result[key] = int(population * value)

Keys = np.array(list(result.keys()))
Values = np.array(list(result.values()))
plt.title("Human Precentege")
plt.bar(Keys,Values)
# #plt.pie(Values, labels=Keys, autopct="%1.1f%%", explode=[0.07,0,0,0],shadow=True)
plt.show()
# print(Values)


#PieChart


#subplots 




