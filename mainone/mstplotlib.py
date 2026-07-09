import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.array([2023,2024,2025,2026])
y1 = np.array([13,12,11,10])
y2 = np.array([13,10,6,10])
y3 = np.array([13,2,6,10])

plt.grid(linewidth="2", color="green", linestyle="dashed")
plt.title("Road trip", fontsize=15, family ="Arial" , fontweight = "bold")
plt.xlabel("FREEDOM", fontweight="bold")
plt.ylabel("DEMOCRASY",  fontweight="bold")
plt.tick_params(axis="both", colors="red")
Line_Style = dict( marker="v", markersize = "10", markerfacecolor = "cyan",markeredgecolor="Blue",linestyle="solid",linewidth="2")

plt.plot(x,y1, **Line_Style)
plt.plot(x,y2, **Line_Style)
plt.plot(x,y3, **Line_Style)

plt.show()


#BarChart

