import pandas as pd

s1 = pd.Series(['Lal Chowk','London','US','Paris'], index = ['India','UK','US','Niaggas in'])

print(s1)

s1.index = [1,2,3,4]

print(s1)