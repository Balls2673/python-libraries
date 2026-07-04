import pandas as pd
import numpy as np

print(pd.__version__)

#series

data = [11,23,42,21]
names = ["Ali", "soing", "Sara","jassam"]
series = pd.Series(data, index=names)
series.loc["soing"] = 320
print(series[series >= 20])
print(series.loc["soing"])

learninghour = {"Day1": 3.0, "Day2": 5.4, "Day3":6.2}
series1 = pd.Series(learninghour)
series1.loc["Day3"] +=  1.3
print(series1)

#data frames

employee = {"Names": ["Jason","Mark","besos","black"],
            "Ages":  []}
rng = np.random.default_rng()
for i in range(len(employee["Names"])): employee["Ages"].append(rng.integers(18,65))
numemp= []
for i in range(len(employee["Names"])): numemp.append(f"Employee{i+1}")
df = pd.DataFrame(employee, index=numemp)
df["job"] = ["cooker","cleaner","server","casher"]
print(df)


