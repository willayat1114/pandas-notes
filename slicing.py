import pandas as pd

s = pd.Series(['New Delhi', 'DC', 'London', 'Paris','asd','ftft','opop','tux'], index = ['India', 'US', 'UK', 'France','qwe','rfv','sxcf','kio'])

print(s[1:7])