# Overview
1. RoundUpValues – Standardizes latitude and longitude values.
2. ValidateUnits – Converts and validates weather unit measurements.
3. DeleteColumns – Removes redundant columns after unit conversions.
   
## RoundupValues: Standardizing Coordinates

* Latitude and longitude values are multiplied by 10, rounded, and then divided by 10.
* The updated coordinates replace the original ones in the dataset.
* The modified dataset is saved as WeatherForecast_rounded.csv.

## ValidateUnits

- Validate the conversion between two different units containing same information.
