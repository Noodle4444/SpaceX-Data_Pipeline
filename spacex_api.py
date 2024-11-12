# import requests
# import pandas as pd

# #Fetch the Data from the Space X API
# response = requests.get('https://api.spacexdata.com/v4/launches')
# data = response.json()

# #convert to dataframe and print the first five rows

# df = pd.DataFrame(data)

# print(df.head())

#below is updated data fetching with pandas
import pandas as pd

url = 'https://api.spacexdata.com/v4/launches'

df = pd.read_json(url)

print(df.head())

#check the columns
print(df.columns)

#get the data types
print(df.dtypes)
