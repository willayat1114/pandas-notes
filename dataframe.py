import pandas as pd
import numpy as np

#df = pd.DataFrame()

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
a3 = np.array([9,10,11,12])

df = pd.DataFrame([a1,a2,a3], columns = ['A','B','C','D'] )



print(df)