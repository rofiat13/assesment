import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

days_of_the_week = {
    'Monday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE',
               'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Tuesday': ['ASH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED',
                'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    'Wednesday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE',
                  'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    'Thursday': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE',
                 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Friday': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED',
               'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']}

df = pd.DataFrame(days_of_the_week)
print(df)

print(df.describe())  # shows the frequency and count

# shows the value count for each colour during the week
monday_colour_count = df['Monday'].value_counts()
print(monday_colour_count)

tuesday_colour_count = df['Tuesday'].value_counts()
print(tuesday_colour_count)

wednesday_colour_count = df['Wednesday'].value_counts()
print(wednesday_colour_count)

thursday_colour_count = df['Thursday'].value_counts()
print(thursday_colour_count)

friday_colour_count = df['Friday'].value_counts()
print(friday_colour_count)

# converting to numerical variable
encoded_data = df[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']] = df[
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].apply(LabelEncoder().fit_transform)
print(encoded_data)

print(encoded_data.describe())
print(df)

# shows the variance
print(encoded_data.var())

# saving in postgres
'CREATE TABLE colours(colour VARCHAR(50),count INT);'
"INSERT INTO colours(colour, count) VALUES(['BLUE','GREEN','YELLOW','ORANGE','WHITE','BROWN','PINK','CREAM','RED'], [6,3,2,2,2,1,1,1,1]);"
