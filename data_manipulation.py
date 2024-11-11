#some practice code for this project
import pandas as pd

data = {
    'rocket' : [
        'Falcon 1',
        'Falcon 9',
        'Falcon Hevy',
    ],
    'launches' : [5, 100, 3],
}

df = pd.DataFrame(data)

print(df)

print(df['rocket'])

falcon9_df = df[df['rocket'] == 'Falcon 9']

df['success_rate'] = [0.4,0.98,1.0]

print(data)