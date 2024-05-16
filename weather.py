import pandas as pd

data = pd.read_csv("weather.csv")

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

# Q-5) Rename the column name "Weather" of the dataframe to "Weather Condition".

data.rename(columns={'Weather' : 'Weather Condition'}, inplace= True)

df_q5 = data
# print(df_q5)

# Q-6) What is the mean 'Visibility'.

df_q6 = data['Visibility_km'].mean()

# print(df_q6)

# Q-7) What is the Standart Deviation of 'Pressure' in this data ?

df_q7 = data.Press_kPa.std()

# print(df_q7)

# Q-8) What is the Variance of "Relative Humidity" in this data ?

df_q8 = data['Rel Hum_%'].var()

# print(df_q8)

# Q-9) Find all instances when "Snow" was recorded.

# value_counts()
df_q9 = data['Weather Condition'].value_counts()
# print(df_q9)

# filtering
df_q9 = data[data['Weather Condition'] == 'Snow']
# print(df_q9)

# str.contains
df_q9 = data[data['Weather Condition'].str.contains('Snow')]
# print(df_q9)

# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# Q. 13) Show all the Records where Weather Condition is Fog.

# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# Q. 15) Find all instances when :

# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'