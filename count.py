import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5,np.NaN,6,7,41,205])

print(s.count())