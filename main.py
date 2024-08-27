import pandas as pd
import matplotlib.pyplot as plt
import os
import time

def clear():
    os.system('clear')

def wait(seconds):
    time.sleep(seconds)

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

total_holiday_2019 = new_reason_df.loc[0, trips_2019_heading]
total_holiday_2024 = new_reason_df.loc[0, trips_2024_heading]
total_visiting_2019 = new_reason_df.loc[1, trips_2019_heading]
total_visiting_2024 = new_reason_df.loc[1, trips_2024_heading]
total_business_2019 = new_reason_df.loc[2, trips_2019_heading]
total_business_2024 = new_reason_df.loc[2, trips_2024_heading]
total_employment_2019 = new_reason_df.loc[3, trips_2019_heading]
total_employment_2024 = new_reason_df.loc[3, trips_2024_heading]
total_education_2019 = new_reason_df.loc[4, trips_2019_heading]
total_education_2024 = new_reason_df.loc[4, trips_2024_heading]
total_other_2019 = new_reason_df.loc[5, trips_2019_heading]
total_other_2024 = new_reason_df.loc[5, trips_2024_heading]

# Menu options
def exitOption():
    input("Press enter to return to menu. ")

def optionOne():
    print(df)
    exitOption()

def optionTwo():
    total_2019 = new_df[trips_2019_heading].sum()
    total_2024 = new_df[trips_2024_heading].sum()
    plt.figure(figsize=(8, 6))
    plt.bar(['2019', '2024'], [total_2019, total_2024], color=['blue', 'orange'])
    plt.xlabel('Year')
    plt.ylabel('Total Number of Travelers')
    plt.ylim(6000, 8750)
    plt.title('Total Number of Travelers in 2019 vs. 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('Travelers_Comparison.png')
    plt.show()
    print("If the graph didn't automatically open, open the Travelers_Comparison.png file to view.")
    exitOption()

def optionThreeA():
    plt.figure(figsize=(8, 6))
    plt.bar(['Holiday', 'Visiting', 'Business', 'Employment', 'Education', 'Other'], [total_holiday_2019, total_visiting_2019, total_business_2019, total_employment_2019, total_education_2019, total_other_2019], color=['red','green','blue','yellow','purple','orangered'])
    plt.xlabel('Reason')
    plt.ylabel('Total number of travelers')
    plt.title('Travel reasons in 2019')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('Travelers_Reasons_2019.png')
    plt.show()
    print("If the graph didn't automatically open, open the Travelers_Reasons_2019.png file to view.")
    exitOption()

def optionThreeB():
    plt.figure(figsize=(8, 6))
    plt.bar(['Holiday', 'Visiting', 'Business', 'Employment', 'Education', 'Other'], [total_holiday_2024, total_visiting_2024, total_business_2024, total_employment_2024, total_education_2024, total_other_2024], color=['lightcoral','palegreen','paleturquoise','palegoldenrod','violet','lightsalmon'])
    plt.xlabel('Reason')
    plt.ylabel('Total number of travelers')
    plt.title('Travel reasons in 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('Travelers_Reasons_2024.png')
    plt.show()
    print("If the graph didn't automatically open, open the Travelers_Reasons_2024.png file to view.")
    exitOption()

def optionThreeC():
    plt.figure(figsize=(22, 6))
    plt.bar(['Holiday 2019', 'Holiday 2024', 'Visiting 2019', 'Visiting 2024', 'Business 2019', 'Business 2024', 'Employment 2019', 'Employment 2024', 'Education 2019', 'Education 2024', 'Other 2019', 'Other 2024'], [total_holiday_2019, total_holiday_2024, total_visiting_2019, total_visiting_2024, total_business_2019, total_business_2024, total_employment_2019, total_employment_2024, total_education_2019, total_education_2024, total_other_2019, total_other_2024], color=['red','lightcoral','green','palegreen','blue','paleturquoise','goldenrod','palegoldenrod','purple','violet','orangered','lightsalmon'])
    plt.xlabel('Reason')
    plt.ylabel('Total number of travelers')
    plt.title('Travel reasons in 2019 and 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('Travelers_Reasons_Comparison.png')
    plt.show()
    print("If the graph didn't automatically open, open the Travelers_Reasons_Comparison.png file to view.")
    exitOption()

def optionFour():
    holiday_percent_2019 = ((total_holiday_2019/total_2019)*100).round(2)
    holiday_percent_2024 = ((total_holiday_2024/total_2019)*100).round(2)
    print(f"In 2019, {holiday_percent_2019}% of tourists were here for a holiday.")
    print(f"In 2024, {holiday_percent_2024}% of tourists were here for a holiday.")

# Menu System
inMenuLoop = True
while inMenuLoop:
    clear()
    print("Welcome to the Tourism Data Analysis Program")
    print("Please select an option from the menu below")
    print("1. Show the dataframe")
    print("2. Create a bar chart comparing 2019 and 2024")
    print("3. Create a bar chart of the reasons for travel")
    print("4. Percentage of tourists for reason")
    chosenOption = input("Select your option: ").lower()
    if chosenOption == "1" or chosenOption == "one":
        optionOne()
    elif chosenOption == "2" or chosenOption == "two":
        optionTwo()
    elif chosenOption == "3" or chosenOption == "three":
        option3year = input("Would you like to see 2019, 2024, or a comparison of both?").lower()
        if option3year == "2019" or option3year == "19":
            optionThreeA()
        elif option3year == "2024" or option3year == "24":
            optionThreeB()
        elif option3year == "both":
            optionThreeC()
        else:
            print("Invalid option.")
    elif chosenOption == "4" or chosenOption == "four":
        optionFour()
    elif chosenOption == "exit":
        exitConfirm = input("Are you sure you want to close the program?: ").lower()
        if exitConfirm == "y" or exitConfirm == "yes":
            inMenuLoop = False
        elif exitConfirm == "n" or exitConfirm == "no":
            exitConfirm
    else:
        print("Invalid Option. Please choose a number listed above.")
print("Program closed.")