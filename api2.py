import pandas as pd
import requests as rq
import numpy as np

username = "jonibek_99"
url = f"https://www.codewars.com/api/v1/users/{username}"
response=rq.get(url)
data=response.json()
id=data['id']
username_data = data["username"]
total_completed = data["codeChallenges"]["totalCompleted"]
fullname = data["name"]
df=pd.DataFrame([{
    'id':id,
    'username_data':username_data,
    'fullname':fullname,
    'total_completed':total_completed,

}])
df.to_csv('codewars.csv')
a=pd.read_csv('codewars.csv')
print(a.T)