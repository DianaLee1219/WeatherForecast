# Overview
0. RoundUpValues – Standardizes latitude and longitude values.
1. ValidateUnits – Converts and validates weather unit measurements.
2. RemoveUnits – Removes redundant columns.


  📁 Input File: cleaned_data.csv
  
  📁 Final Output File: WeatherForecast_CleanedUnits.csv
  
## RoundupValues: Standardizing Coordinates

* Latitude and longitude values are multiplied by 10, rounded, and then divided by 10.
* The updated coordinates replace the original ones in the dataset.
* The modified dataset is saved as WeatherForecast_rounded.csv.

## ValidateUnits: Converting & Validating Weather Data

To ensure consistency, we convert all values to a standard unit and verify the accuracy.

After conversion, the script compares the original and calculated values. If the difference exceeds a predefined threshold, a warning message is displayed.

| Measurement | Original Unit | Converted To |
| --- | ----|
| Temperature | Fahrenheit (°F) | Celsius (°C) |
| Wind Speed | Miles per hour (mph) | Kilometers per hour (kph) |
| Pressure | Inches (in) | Millibars (mb) |
| Precipitation | Inches (in) | Millimeters (mm) |
| Feels-like-Temp | Fahrenheit (°F) | Celsius (°C) |
| Visibility | Miles (miles) | Kilometers (km) |

## RemoveUnits: Deleting Redundant Data

After successful validation, the original columns (which contained data in different units) are no longer needed. 

To **avoid redundancy**, they are removed from the dataset.

Deleted Columns:
* degF
* wind_mph
* pressure_in
* precip_in
* feels_like_fahrenheit
* visibility_miles
  
