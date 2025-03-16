import pandas as pd

# Load the Excel file
df = pd.read_excel("WeatherForecast_Temperature.xlsx")

# Ensure column names are correct
df = df.rename(columns={"temperature_celsius": "degC", "temperature_fahrenheit": "degF"})

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Calculate converted values
df["calculated_degC"] = df["degF"].apply(fahrenheit_to_celsius)

# Validate conversion (Check difference within a small margin of error)
df["valid"] = abs(df["degC"] - df["calculated_degC"]) < 0.1

# Check for mismatches
mismatch_count = df["valid"].value_counts().get(False, 0)
if mismatch_count > 0:
    print(f"Warning: {mismatch_count} temperature mismatch(es) detected!")
else:
    print("Temerpature: No mismatch has found")
