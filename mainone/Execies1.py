import numpy as np
import pandas as pd


EmployeeData = {
    "Names": [
        "Oliver", "Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia", "Lucas", "Mia",
        "Mason", "Isabella", "Logan", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth",
        "James", "Benjamin", "Jacob", "Michael", "Elijah", "Alexander", "William", "Daniel", "Henry", "Jackson",
        "Sebastian", "Jack", "Aiden", "Matthew", "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt",
        "John", "Luke", "Grace", "Chloe", "Zoey", "Lily", "Hannah", "Ella"
    ], 
    "Ages": [], 
    "Department": [], 
    "Salary": [], 
    "Experience": []
}




depermantes = ["Cooker","CLearner","Technetion", "Bodyguard" ,"Random Worker"]
Lenghts = len(EmployeeData["Names"])
rng = np.random.default_rng()
for i in range(Lenghts):
    EmployeeData["Ages"].append(rng.integers(20,61))
    EmployeeData["Salary"].append(rng.integers(500,5001))
    EmployeeData["Experience"].append(rng.integers(0,36))
    EmployeeData["Department"].append(rng.choice(depermantes))


	
Enumper = []
for i in range(Lenghts):
	Enumper.append(i + 1)
DF = pd.DataFrame(EmployeeData, Enumper)
DF.loc[DF["Salary"] < 1000, "Salary"] = 1000
DF["Tax"] = "10%"
DF["Net Salary"] = DF["Salary"] - (DF["Salary"] * 10/100)
DF = DF.sort_values(by="Salary", ascending =False)
DFC = DF.loc[(DF["Ages"] > 40) & (DF["Salary"] > 3000)]
print(np.mean(DF["Salary"]))
print(np.max(DF["Salary"]))
print(np.min(DF["Salary"]))
print(DF["Department"].value_counts())

print(DF)
print(DFC)
DF.to_csv("Employee Data.csv" , index=False)


New_Row = pd.DataFrame([{"Names": "Greg","Ages": 23, "Department":"CLearner",    "Salary":2000, "Experience":6 }])
DFC = pd.concat([DF,New_Row])
print(DFC)