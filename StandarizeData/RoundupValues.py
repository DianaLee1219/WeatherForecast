import pandas as pd

# Load the data from the Excel file
file_path = 'WeatherForcast_Crosscheck.xlsx'
sheet_name = 'GlobalWeatherRepository'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Function to round latitude and longitude to 0.1 resolution
def round_coordinates(value):
    return round(value * 10) / 10

# Apply the rounding function to latitude and longitude columns
df['latitude'] = df['latitude'].apply(round_coordinates)
df['longitude'] = df['longitude'].apply(round_coordinates)

# Print the first 10 rows of the modified table
print("First 10 rows with rounded latitude and longitude:")
print(df.head(10).to_string(index=False))

# Save the modified DataFrame to a new Excel file
output_file_path = 'WeatherForcast_rounded.xlsx'
df.to_excel(output_file_path, index=False, sheet_name=sheet_name)

print(f"\nModified data saved to {output_file_path}")
