import pandas as pd
import matplotlib.pyplot as plt
import os

def clear():
    os.system('clear')

# CSV setup
trips_2019_heading = "Trips Ending March 2019"
trips_2024_heading = "Trips Ending March 2024"
spend_2019_heading = "Spend Ending March 2019"
spend_2024_heading = "Spend Ending March 2024"

# Read original CSV file
df = pd.read_csv('Tourism.csv')
reason_df = pd.read_csv('Reasons_For_Travel.csv')

# Convert to numeric
df[trips_2019_heading] = pd.to_numeric(df[trips_2019_heading], errors='coerce')
df[trips_2024_heading] = pd.to_numeric(df[trips_2024_heading], errors='coerce')
df[spend_2019_heading] = pd.to_numeric(df[spend_2019_heading], errors='coerce')
df[spend_2024_heading] = pd.to_numeric(df[spend_2024_heading], errors='coerce')
reason_df[trips_2019_heading] = pd.to_numeric(reason_df[trips_2019_heading], errors='coerce')
reason_df[trips_2024_heading] = pd.to_numeric(reason_df[trips_2024_heading], errors='coerce')
reason_df[spend_2019_heading] = pd.to_numeric(reason_df[spend_2019_heading], errors='coerce')
reason_df[spend_2024_heading] = pd.to_numeric(reason_df[spend_2024_heading], errors='coerce')

# Handle empty values
df.fillna(0, inplace=True)
reason_df.fillna(0, inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Tourism_cleaned.csv', index=False)
reason_df.to_csv('Reasons_For_Travel_cleaned.csv', index=True)

# Read the cleaned CSV file into a new DataFrame
new_df = pd.read_csv('Tourism_cleaned.csv')
new_reason_df = pd.read_csv('Reasons_For_Travel_cleaned.csv')

def list_countries():
    countries = new_df['Country'].tolist()
    for i in range(len(countries)):
        print(f"{i+1}. {countries[i]}")

def get_single_data(country, heading):
    pass

# Menu system
action_loop = True
int_action = 0
clear()
print("Welcome to the tourism tracker, the easiest way to discover all the tourism information you need about Australia, from 2019 and 2024.")
def main_loop():
    global action_loop, int_action
    print("What would you like to do?")
    print("1. Find the number of tourists to a country at a specific time")
    print("2. Create a graph comparing tourists to a country from 2019 and 2024")
    print("3. Create a graph of tourism numbers in a specific year")
    print("4. Stop the program")
    given_action = False
    while not given_action:
        action = input("What would you like to do?: ")
        try:
            int_action = int(action)
            if int_action <= 0 or int_action >= 5:
                print("Invalid action, please input an option from 1-4")
            else:
                given_action = True
        except ValueError:
            print("Please input a number.")
    if int_action == 1:
        print("Which country from this list would you like to see?")
        list_countries()
    elif int_action == 2:
        pass
    elif int_action == 3:
        pass
    elif int_action == 4:
        action_loop = False
while action_loop:
    main_loop()
    clear()
print("Stopping the program...\n\nThank you for using the tourism tracker.")