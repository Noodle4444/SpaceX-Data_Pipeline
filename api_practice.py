import requests
import pandas as pd

#Fetch the Data from the Space X API
response = requests.get('https://api.spacexdata.com/v5/launches')
data = response.json()

#convert to dataframe and print the first five rows

df = pd.DataFrame(data)

print(df.head())

