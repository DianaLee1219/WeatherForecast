import pandas as pd

# Load the dataset
df = pd.read_csv("WeatherForecast_rounded.csv", encoding="ISO-8859-1")

# List of original columns that were converted and should be removed
columns_to_remove = [
    "degF", "wind_mph", "pressure_in", "precip_in", "feels_like_fahrenheit", "visibility_miles"
]

# Remove these columns from the DataFrame (if they exist)
df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)

# Save the cleaned DataFrame to a new CSV file
output_file_path = "WeatherForecast_CleanedUnits.csv"
df.to_csv(output_file_path, index=False, encoding="ISO-8859-1")

# Print confirmation message
print(f"\n✅ Removed original columns: {columns_to_remove}")
print(f"📁 Updated file saved as: {output_file_path}")
