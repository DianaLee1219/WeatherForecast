import pandas as pd

# Load the data from the Excel file
file_path = 'cleaned_data.cvs'

try:
    df = pd.read_csv(file_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="ISO-8859-1") 


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
output_file_path = 'WeatherForecast_rounded.cvs'
df.to_excel(output_file_path, index=False, sheet_name=sheet_name)

print(f"\nModified data saved to {output_file_path}")
