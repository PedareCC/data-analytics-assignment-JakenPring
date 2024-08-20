import pandas as pd
import matplotlib.pyplot as plt

trips_2019_heading = "Trips Ending March 2019"
trips_2024_heading = "Trips Ending March 2024"
spend_2019_heading = "Spend Ending March 2019"
spend_2024_heading = "Spend Ending March 2024"

# Read the original CSV file into a DataFrame
df = pd.read_csv('Tourism.csv')
reason_df = pd.read_csv('Reasons_For_Travel.csv')

# Convert columns to numeric types
df[trips_2019_heading] = pd.to_numeric(df[trips_2019_heading], errors='coerce')
df[trips_2024_heading] = pd.to_numeric(df[trips_2024_heading], errors='coerce')
df[spend_2019_heading] = pd.to_numeric(df[spend_2019_heading], errors='coerce')
df[spend_2024_heading] = pd.to_numeric(df[spend_2024_heading], errors='coerce')
reason_df[trips_2019_heading] = pd.to_numeric(reason_df[trips_2019_heading], errors='coerce')
reason_df[trips_2024_heading] = pd.to_numeric(reason_df[trips_2024_heading], errors='coerce')
reason_df[spend_2019_heading] = pd.to_numeric(reason_df[spend_2019_heading], errors='coerce')
reason_df[spend_2024_heading] = pd.to_numeric(reason_df[spend_2024_heading], errors='coerce')

# Handle NaN values (optional)
df.fillna(0, inplace=True) # Replaces NaNs with 0s
reason_df.fillna(0, inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Tourism_cleaned.csv', index=False)
reason_df.to_csv('Reasons_For_Travel_cleaned.csv', index=True)

# Read the cleaned CSV file into a new DataFrame
new_df = pd.read_csv('Tourism_cleaned.csv')
new_reason_df = pd.read_csv('Reasons_For_Travel_cleaned.csv')

# Print the cleaned data to the console
print(new_df)
print(new_reason_df)

# Calculate the total number of people that traveled in 2019
total_2019 = new_df[trips_2019_heading].sum()

# Calculate the total number of people that traveled in 2024
total_2024 = new_df[trips_2024_heading].sum()

# Print the totals
print(f'Total number of travelers in 2019: {total_2019}')
print(f'Total number of travelers in 2024: {total_2024}')

# Top 5 countries
top5_2019 = new_df.sort_values(trips_2019_heading, ascending=False)['Country'].head(5)
top5_2024 = new_df.sort_values(trips_2024_heading, ascending=False)['Country'].head(5)

# Print top 5 countries
print(f"The most tourists in 2019 came from: \n{top5_2019}")
print(f"The most tourists in 2024 came from: \n{top5_2024}")

# Create a bar chart for tourism.csv
plt.figure(figsize=(8, 6))
plt.bar(['2019', '2024'], [total_2019, total_2024], color=['blue', 'orange'])
plt.xlabel('Year')
plt.ylabel('Total Number of Travelers')
plt.ylim(6000, 8750)
plt.title('Total Number of Travelers in 2019 vs. 2024')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a PNG file
plt.savefig('Travelers_Comparison.png')

# Show the plot
plt.show()

# Information for reasons for travel bar chart
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

# Create a bar chart for reasons_for_travel.csv in 2019
plt.figure(figsize=(8, 6))
plt.bar(['Holiday', 'Visiting', 'Business', 'Employment', 'Education', 'Other'], [total_holiday_2019, total_visiting_2019, total_business_2019, total_employment_2019, total_education_2019, total_other_2019], color=['red','green','blue','yellow','purple','orangered'])
plt.xlabel('Reason')
plt.ylabel('Total number of travelers')
# plt.ylim(6000, 8000)
plt.title('Travel reasons in 2019')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Travelers_Reasons_2019.png')
plt.show()

# Create a bar chart for reasons_for_travel.csv in 2019
plt.figure(figsize=(8, 6))
plt.bar(['Holiday', 'Visiting', 'Business', 'Employment', 'Education', 'Other'], [total_holiday_2024, total_visiting_2024, total_business_2024, total_employment_2024, total_education_2024, total_other_2024], color=['lightcoral','palegreen','paleturquoise','palegoldenrod','violet','lightsalmon'])
plt.xlabel('Reason')
plt.ylabel('Total number of travelers')
# plt.ylim(6000, 8000)
plt.title('Travel reasons in 2024')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Travelers_Reasons_2024.png')
plt.show()

# Create a bar chart for reasons_for_travel.csv comparing 2019 and 2024
plt.figure(figsize=(22, 6))
plt.bar(['Holiday 2019', 'Holiday 2024', 'Visiting 2019', 'Visiting 2024', 'Business 2019', 'Business 2024', 'Employment 2019', 'Employment 2024', 'Education 2019', 'Education 2024', 'Other 2019', 'Other 2024'], [total_holiday_2019, total_holiday_2024, total_visiting_2019, total_visiting_2024, total_business_2019, total_business_2024, total_employment_2019, total_employment_2024, total_education_2019, total_education_2024, total_other_2019, total_other_2024], color=['red','lightcoral','green','palegreen','blue','paleturquoise','goldenrod','palegoldenrod','purple','violet','orangered','lightsalmon'])
plt.xlabel('Reason')
plt.ylabel('Total number of travelers')
# plt.ylim(6000, 8000)
plt.title('Travel reasons in 2019 and 2024')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('Travelers_Reasons_Comparison.png')
plt.show()

# Find the total spending in 2019 and 2024
total_spending_2019 = new_df[spend_2019_heading].sum()
total_spending_2024 = new_df[spend_2024_heading].sum()

# Print total spending in 2019 and 2024
print(f"The total spending from tourists in 2019 is ${total_spending_2019.round(2)}")
print(f"The total spending from tourists in 2024 is ${total_spending_2024.round(2)}")

# Find the average spending per person in 2019 and 2024
average_spending_2019 = total_spending_2019 / total_2019
average_spending_2024 = total_spending_2024 / total_2024

# Print average spending per person
print(f"Average spending per person in 2019: ${average_spending_2019.round(2)}")
print(f"Average spending per person in 2024: ${average_spending_2024.round(2)}")

# Percentage of tourists on holiday in 2019 and 2024
holiday_percent_2019 = ((total_holiday_2019/total_2019)*100).round(2)
holiday_percent_2024 = ((total_holiday_2024/total_2019)*100).round(2)

# Print pergentage of tourists on holiday
print(f"In 2019, {holiday_percent_2019}% of tourists were here for a holiday.")
print(f"In 2024, {holiday_percent_2024}% of tourists were here for a holiday.")