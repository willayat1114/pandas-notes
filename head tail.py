import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3,5,6,7,8,9], index = ['a','b','c','d','e','f','g','h'])

print(s1.head())
print(s1.tail())
print(s1)