import numpy as np
import pandas as pd


EmployeeData = [{
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
}]


rng = np.random.default_rng()
for i in range(len(EmployeeData["Names"])):
	EmployeeData["Ages"].append(rng.integers(20,61))
for i in range(len(EmployeeData["Names"])):
	EmployeeData["Names"].append(rng.integers(500,5001))

for i in range(len(EmployeeData["Names"])):
	EmployeeData["Names"].append(rng.integers(0,36))
	
Enumper = []
for i in range(len(EmployeeData["Names"])):
	Enumper.append(rng.integers(i + 1))
DF = pd.DataFrame(EmployeeData,index=Enumper)
print(DF)
