import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "HandleMissingValues_&_Typos_Result.csv"  

try:
    df = pd.read_csv(file_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="ISO-8859-1") 

# Count the number of occurrences for each city
city_counts = df["location_name"].value_counts()

# Print cities with fewer than 200 entries
cities_to_remove = city_counts[city_counts < 200]
print("Cities with less than 200 entries:")
print(cities_to_remove)

# Plot before removing data
plt.figure(figsize=(15, 6))
city_counts.plot(kind="bar", color="blue", alpha=0.7)
plt.xlabel("City Names")
plt.ylabel("Number of Data Entries")
plt.title("Number of Data Entries Before Cleaning")
plt.xticks(rotation=90)
plt.show()

# Remove cities with less than 200 entries
df_cleaned = df[~df["location_name"].isin(cities_to_remove.index)]

# Count again after removal
city_counts_after = df_cleaned["location_name"].value_counts()

# Plot after removing data
plt.figure(figsize=(15, 6))
city_counts_after.plot(kind="bar", color="green", alpha=0.7)
plt.xlabel("City Names")
plt.ylabel("Number of Data Entries")
plt.title("Number of Data Entries After Cleaning")
plt.xticks(rotation=90)
plt.show()

# Save cleaned dataset
df_cleaned.to_csv("cleaned_data.csv", index=False)
print("Data cleaning complete. Saved as 'cleaned_data.csv'.")
