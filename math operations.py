import numpy as np #Import numpy liberary as np
import pandas as pd #Import Pandas liberary as pd

a1 = np.array([11,12,13,14]) #Array 1
a2 = np.array([1,2,3,4]) #Array 2
s1 = pd.Series(a1, index = [1,2,3,4]) #Series 1 with array one for data
s2 = pd.Series(a2, index = [1,2,3,4]) #Series 2 with array two for data

#print(s1, s2) #Print both s1 and s2
#print(s1+s2) #Print the sum of s1 and s2
#print(s1-s2) #Print the difference of s1 and s2
#print(s1*s2) #Print the product of s1 and s2
#print(s1/s2) #Print the division of s1 and s2