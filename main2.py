import pandas as pd

data = {
    'Name':['Onisan', 'Onichan', 'Teju','Nano'],
    'Age':[6,30,106,212],
    'Gender': ['F','M','F','F'],
    'Salary':[106,212,6000,2]
}

d = pd.DataFrame(data)

print(d)
print()

print("selecting row by index lables:")
print(d.loc[1:3,['Age','Gender']])
print()

print("selecting row by position:")
print(d.iloc[0:3, 0:3])
print()

print("selecting row based on condition:")
print(d[d['Age']>30])
print()