import pandas as pd

data = {
    'Name':['Onisan', 'Onichan', 'Teju','Nano'],
    'Age':[6,30,106,212],
    'City': ['soura','Hyderpora','Sanatnagar','Furin'],
    'Salary':[106,212,6000,-20000]
}

d = pd.DataFrame(data)

d['Gender'] = ['F','M','F','F']
print(d)

d = d.drop(columns = 'Name')

d = d.rename(columns={'City' : 'country'})

d = d.drop(columns={'Age','Salary'})

print(d.head)
print(d.tail)
print(d)