import pandas as pd

# Conversion Thresholds
thresholds = {
    "temperature": 0.1,  # [°C]
    "wind": 0.3,  # [kph]
    "pressure": 1,  # [mb]
    "precip": 1,  # [mm]
    "feels_like": 0.1,  # [°C]
    "visibility": 2  # [km]
}

# Load the dataset
df = pd.read_csv("WeatherForecast_rounded.csv", encoding="ISO-8859-1")

# Rename columns for clarity
df = df.rename(columns={"temperature_celsius": "degC", "temperature_fahrenheit": "degF"})

# Conversion Functions
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def mph_to_kph(mph):
    return mph * 1.60934

def in_to_mb(pressure_in):
    return pressure_in * 33.8639

def in_to_mm(precip_in):
    return precip_in * 25.4

def miles_to_km(miles):
    return miles * 1.60934

# Apply conversions only if the column exists
conversion_mapping = {
    "calculated_degC": ("degF", fahrenheit_to_celsius),
    "calculated_kph": ("wind_mph", mph_to_kph),
    "calculated_pressure_mb": ("pressure_in", in_to_mb),
    "calculated_precip_mm": ("precip_in", in_to_mm),
    "calculated_feels_like_c": ("feels_like_fahrenheit", fahrenheit_to_celsius),
    "calculated_visibility_km": ("visibility_miles", miles_to_km),
}

for new_col, (original_col, func) in conversion_mapping.items():
    if original_col in df.columns:
        df[new_col] = df[original_col].apply(func)

# Validation Checks
validation_mapping = {
    "valid_temperature": ("degC", "calculated_degC", "temperature"),
    "valid_wind": ("wind_kph", "calculated_kph", "wind"),
    "valid_pressure": ("pressure_mb", "calculated_pressure_mb", "pressure"),
    "valid_precip": ("precip_mm", "calculated_precip_mm", "precip"),
    "valid_feels_like": ("feels_like_celsius", "calculated_feels_like_c", "feels_like"),
    "valid_visibility": ("visibility_km", "calculated_visibility_km", "visibility"),
}

for valid_col, (original_col, calculated_col, threshold_key) in validation_mapping.items():
    if original_col in df.columns and calculated_col in df.columns:
        df[valid_col] = abs(df[original_col] - df[calculated_col]) < thresholds[threshold_key]

# Display Validation Results
for valid_col, (_, _, label) in validation_mapping.items():
    mismatch_count = df[valid_col].value_counts().get(False, 0)
    if mismatch_count > 0:
        print(f"⚠ Warning: {mismatch_count} {label.capitalize()} mismatch(es) detected!")
    else:
        print(f"{label.capitalize()}: No mismatch found")
