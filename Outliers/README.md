# Identifying and Removing outliers

## How it works?

This script detects and removes outliers in weather data using a combination of **feature clipping, Z-score, and IQR methods**, ensuring that extreme values do not negatively impact analysis. 


## Methods 

* Feature Clipping: Applies predefined limits to deal with extreme values.
* Z-Score Method: Detects and removes outliers with Z > 3 for temperature-related variables.
* IQR Method: Detects and removes outliers beyond 1.5 × IQR for pressure and air quality variables.

1. Temperature [°C]
* Normal Range: -89.2°C (lowest recorded) to 56.7°C (highest recorded)
* Clipping + Z-Score Method: Cap values between -90°C and 57°C to remove extreme anomalies. Also, used Z > 3 as an outlier threshold based on historical distributions.

2. Feels-Like Temperature [°C]
* Normal Range: Should be close to actual temperature, but affected by wind chill and humidity.
* Clipping + Z-score detection: Keep within -100°C to 60°C (to include extreme wind chill) and check extreme values.
  
3. Wind Speed [kph]
* Normal Range: 0 to 407 kph (highest recorded, Hurricane Olivia)
* Clipping: Cap wind speed at 410 kph (allowing buffer for extreme storms).

4. Pressure [mb]
* Normal Range: 870 mb (lowest, Typhoon Tip) to 1085 mb (highest, Mongolia)
* Clipping + IQR: Set limits between 870 mb and 1085 mb. Apply IQR to detect anomalies.

5. Precipitation [mm]
* Normal Range: 0 mm (no rain) to 1825 mm/day (highest, India)
* Clipping: Cap daily precipitation at 2000 mm.

6. Humidity [%]
* Normal Range: 0% (extreme desert) to 100% (fully saturated air)
* Clipping: Ensure values stay within 0–100%.

7. Visibility [km]
* Normal Range: 0 km (dense fog) to 100 km (clear air)
* Clipping: Limit visibility between 0 and 100 km.

8. UV indext
* Normal Range: 0 (no sunlight) to 20+ (extreme UV radiation)
* Clipping: Limit values between 0 and 24 (the highest UV ever recorded was 23.5 in the Andes).

9. Air Quality (Ozone, NO₂, PM2.5)
* Ozone (O₃) Normal Range: 0–400 ppb (extreme pollution events)
* NO₂ Normal Range: 0–300 ppb (urban high pollution)
* PM2.5 Normal Range: 0–600 µg/m³ (severe pollution)
* Clipping + IQR Method: Set reasonable upper limits based on historical records and remove values using IQR.

## Results

📂 Final Cleaned Dataset: WeatherForecast_CleanedOutliers.csv
