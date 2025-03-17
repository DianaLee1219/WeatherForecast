# Identifying outliers

## How it works?

The table below is useful outlier handling methods for each column, considering real-world constraints and meteorological records.
![image](https://github.com/user-attachments/assets/542de6e3-5e83-41c2-b93d-d8fd4cd88e20)


## Temperature [°C]
* Normal Range: -89.2°C (lowest recorded) to 56.7°C (highest recorded)
* Clipping: Cap values between -90°C and 60°C to remove extreme anomalies.
* Z-Score Method: Use Z > 3 as an outlier threshold based on historical distributions.

## Feels-Like Temperature [°C]
* Normal Range: Should be close to actual temperature, but affected by wind chill and humidity.
* Check Deviation: Flag as outlier if feels-like temperature deviates by >15°C from actual.
* Feature Clipping: Keep within -100°C to 70°C (to include extreme wind chill).
  
## Wind Speed [kph]
* Normal Range: 0 to 407 kph (highest recorded, Hurricane Olivia)
* Clipping: Cap wind speed at 450 kph (allowing buffer for extreme storms).
* Interquartile Range (IQR): Remove values beyond Q3 + 1.5*IQR

## Pressure [mb]
* Normal Range: 870 mb (lowest, Typhoon Tip) to 1084 mb (highest, Mongolia)
* Clipping: Set limits between 850 mb and 1100 mb.
* Rolling Median: Use a rolling window to smooth unrealistic fluctuations.

## Precipitation [mm]
* Normal Range: 0 mm (no rain) to 1825 mm/day (highest, India)
* Clipping: Cap daily precipitation at 2000 mm.
* Rolling Mean: Compare with the 7-day average to detect inconsistencies.

## Humidity [%]
* Normal Range: 0% (extreme desert) to 100% (fully saturated air)
* Clipping: Ensure values stay within 0–100%.
* Log Transformation: If humidity has an odd distribution, apply log(1+humidity).

## Visibility [km]
* Normal Range: 0 km (dense fog) to 100 km (clear air)
* Clipping: Limit visibility between 0 and 100 km.
* Time-Series Check: A sudden jump from 1 km to 50 km may indicate an error.

## UV indext
* Normal Range: 0 (no sunlight) to 20+ (extreme UV radiation)
* Clipping: Limit values between 0 and 25 (the highest UV ever recorded was 23.5 in the Andes).
* Rolling Average Check: Sudden fluctuations should be smoothed over time.

## Air Quality (Ozone, NO₂, PM2.5)
* Ozone (O₃) Normal Range: 0–500 ppb (extreme pollution events)
* NO₂ Normal Range: 0–300 ppb (urban high pollution)
* PM2.5 Normal Range: 0–1000 µg/m³ (severe pollution)
* IQR Method: Remove values beyond Q3 + 1.5*IQR.
* Feature Clipping: Set reasonable upper limits based on historical records.
