import pandas as pd

threshold_temperature = 0.1 # [degC]
threshold_wind = 0.3 # [kph]
threshold_pressure = 1 #[mb]
threshold_precip = 1 # [mm]
threshold_feels_like = 0.1 # [degC]
threshold_visibility = 2 # [km]

# Load the Excel file
df = pd.read_excel("WeatherForecast_Assessment.xlsx")

#Rename
df = df.rename(columns={"temperature_celsius": "degC", "temperature_fahrenheit": "degF"})


# Function to convert 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def mph_to_kph(mph):
    return mph * 1.60934

def in_to_mb(pressure_in):
    return pressure_in * 33.8639
    
def in_to_mm(precip_in):
    return precip_in * 25.4

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def miles_to_km(miles):
    return miles * 1.60934


# Perform conversions 

df["calculated_degC"] = df["degF"].apply(fahrenheit_to_celsius)
df["calculated_kph"] = df["wind_mph"].apply(mph_to_kph)
df["calculated_pressure_mb"] = df["pressure_in"].apply(in_to_mb)
df["calculated_precip_mm"] = df["precip_in"].apply(in_to_mm)
df["calculated_feels_like_c"] = df["feels_like_fahrenheit"].apply(fahrenheit_to_celsius)
df["calculated_visibility_km"] = df["visibility_miles"].apply(miles_to_km)

# Validate conversions
df["valid"] = abs(df["degC"] - df["calculated_degC"]) < temperature_threshold
df["valid"] = abs(df["wind_kph"] - df["calculated_kph"]) < threshold_wind
df["valid_pressure"] = abs(df["pressure_mb"] - df["calculated_pressure_mb"]) < threshold_pressure
df["valid_precip"] = abs(df["precip_mm"] - df["calculated_precip_mm"]) < threshold_precip
df["valid_feels_like"] = abs(df["feels_like_celsius"] - df["calculated_feels_like_c"]) < threshold_feels_like
df["valid_visibility"] = abs(df["visibility_km"] - df["calculated_visibility_km"]) < threshold_visibility

# Check for mismatches
mismatch_count = df["valid"].value_counts().get(False, 0)
if mismatch_count > 0:
    print(f"Warning: {mismatch_count} temperature mismatch(es) detected!")
else:
    print("Temerpature: No mismatch has found")

mismatch_count_wind = df["valid"].value_counts().get(False, 0)
if mismatch_count_wind > 0:
    print(f"Warning: {mismatch_count_wind} wind speed mismatch(es) detected!")
else:
    print("Wind: No mismatch has found")


for column, label in [("valid_pressure", "Pressure"), ("valid_precip", "Precipitation"), ("valid_feels_like", "Feels-Like Temperature"), ("valid_visibility", "Visibility")]:
    mismatch_count = df[column].value_counts().get(False, 0)
    if mismatch_count > 0:
        print(f"Warning: {mismatch_count} {label} mismatch(es) detected!")
    else:
        print("No mismatch has found")
