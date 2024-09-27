"""
This project is about creating aviation data, add more columns to the same dataframe with more information and storing result in a mysql database.
Author: Kartikay Singh
"""
import pandas as pd

# sample aviation data
data = {
    'flight_number': ['AI101', 'EK202', 'LH303', 'BA404'],
    'origin':['Delhi', 'Dubai', 'Frankfurt', 'London'],
    'Destination': ['New York', 'Los Angeles', 'Mumbai', 'Paris'],
    'flight_duration': [15.5, 16.0, 8.5, 7.0]
}

df = pd.DataFrame(data)
print(df)

# Now lets add a new column to the existing dataframe.
long_haul_flights_df = df[df['flight_duration'] > 8]
print(f"Below are the long haul flights")
print(long_haul_flights_df)
