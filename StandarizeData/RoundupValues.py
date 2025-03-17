import pandas as pd

# Load the data from the csv file
df = pd.read_csv("cleaned_data.csv", encoding="ISO-8859-1")

# Function to round latitude and longitude to 0.1 resolution
def round_coordinates(value):
    return round(value * 10) / 10

# Apply the rounding function to latitude and longitude columns
df['latitude'] = df['latitude'].apply(round_coordinates)
df['longitude'] = df['longitude'].apply(round_coordinates)

# Save the modified DataFrame to a new Excel file
output_file_path = 'WeatherForecast_rounded.csv'
df.to_csv(output_file_path, index=False, encoding="ISO-8859-1")

print(f"\nModified data saved to {output_file_path}")
