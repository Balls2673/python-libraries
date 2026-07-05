import pandas as pd
import numpy as np
import os 

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
#add column
df["job"] = ["cooker","cleaner","server","casher"]
#new row
new_row = pd.DataFrame([{"Names": "zucherburg", "job": "Nicker"}])
DF = pd.concat([df, new_row])
print(DF)


#importing

dfc = pd.read_csv("mainone/data.csv")
#print(dfc[["Weight", "Type1"]].to_string())

#selection

dcf = pd.read_csv("mainone/data.csv", index_col="Name" )
print(dcf.loc["Bulbasaur":"Caterpie", ["Height", "Weight"]])

print(dfc.iloc[0:11, 0:4])

popokemon = input("enter a pokemon name: ")

try:
 print( dcf.loc[popokemon])

except KeyError:
 print(f"{popokemon} not found")




