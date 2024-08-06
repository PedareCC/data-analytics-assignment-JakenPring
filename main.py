import pandas as pd
import numpy as np

#Read the CSV file into a DataFrame
df = pd.read_csv('Tourism.csv')

tripTotal2019 = df['Trips Ending March 2019'].sum()
tripTotal2024 = df['Trips Ending March 2024'].sum()
comparison = {
    "2019": {},
    "2024": {}
}

for i in range(len(df)):
    comparison["2019"][df.loc[i, "Country"]] = df.loc[i, 'Trips Ending March 2019']
    comparison["2024"][df.loc[i, "Country"]] = df.loc[i, 'Trips Ending March 2024']

print(f"In 2019, there were a total of {tripTotal2019} trips around the world.")
print(f"In 2024, there were a total of {tripTotal2024} trips around the world.")

for i in comparison["2019"]:
    print(f"In 2019 in {i} there were {comparison['2019'][i]} tourists")
for i in comparison["2024"]:
    print(f"In 2024 in {i} there were {comparison['2024'][i]} tourists")