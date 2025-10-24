import pandas as pd
import numpy as np
# from pprint import pprint as print
import requests
# df=pd.read_json('json.json')
# print(df)
r = requests.get("https://api.github.com/repos/jonibek99/numpy")
data=r.json()
df=pd.DataFrame([data])
df.to_csv('my.csv')
a=pd.read_csv('my.csv')
print(a.head(3))


