import pandas as pd

data = pd.read_csv("file.csv")

# Q-1) Find all the unique "Wind Speed" values in data.

df_q1 = data['Wind Speed_km/h'].unique()

# print(df_q1)

# Q-2) Find the number of times when the "Weather is exactly Clear."

df_q2 = data['Weather'].value_counts()

# filtering

df_q2 =data[data.Weather == 'Clear']

# groupby

df_q2 = data.groupby('Weather').get_group('Clear')

# print(df_q2)

# Q-3) Find the number of times when the "Wind Speed was exactly 4km/h."

df_q3 = data[data['Wind Speed_km/h'] == 4]

# print(df_q3)

# Q-4) Find out all the Null Values in the data.

df_q4 = data.isnull().sum() # 0
df_q4 = data.notnull().sum() # 8784

# print(df_q4)

