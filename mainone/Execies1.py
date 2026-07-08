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
print(DF)
