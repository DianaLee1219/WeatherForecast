# Identifying outliers

## How it works?

The table below is useful outlier handling methods for each column, considering real-world constraints and meteorological records.

## Temperature [°C]
* Normal Range: -89.2°C (lowest recorded) to 56.7°C (highest recorded)
* Clipping + Z-Score Method: Cap values between -90°C and 57°C to remove extreme anomalies. Also, use Z > 3 as an outlier threshold based on historical distributions.

## Feels-Like Temperature [°C]
* Normal Range: Should be close to actual temperature, but affected by wind chill and humidity.
* Check Deviation: Flag as outlier if feels-like temperature deviates by >15°C from actual.
* Feature Clipping + Z-score detection: Keep within -100°C to 60°C (to include extreme wind chill) and check extreme values.
  
## Wind Speed [kph]
* Normal Range: 0 to 407 kph (highest recorded, Hurricane Olivia)
* Clipping: Cap wind speed at 410 kph (allowing buffer for extreme storms).

## Pressure [mb]
* Normal Range: 870 mb (lowest, Typhoon Tip) to 1085 mb (highest, Mongolia)
* Clipping + IQR: Set limits between 870 mb and 1085 mb. Apply IQR to detect anomalies.

## Precipitation [mm]
* Normal Range: 0 mm (no rain) to 1825 mm/day (highest, India)
* Clipping: Cap daily precipitation at 2000 mm.

## Humidity [%]
* Normal Range: 0% (extreme desert) to 100% (fully saturated air)
* Clipping: Ensure values stay within 0–100%.

## Visibility [km]
* Normal Range: 0 km (dense fog) to 100 km (clear air)
* Clipping: Limit visibility between 0 and 100 km.

## UV indext
* Normal Range: 0 (no sunlight) to 20+ (extreme UV radiation)
* Clipping: Limit values between 0 and 24 (the highest UV ever recorded was 23.5 in the Andes).
* Rolling Average Check: Sudden fluctuations should be smoothed over time.

## Air Quality (Ozone, NO₂, PM2.5)
* Ozone (O₃) Normal Range: 0–400 ppb (extreme pollution events)
* NO₂ Normal Range: 0–300 ppb (urban high pollution)
* PM2.5 Normal Range: 0–600 µg/m³ (severe pollution)
* Clipping + IQR Method: Set reasonable upper limits based on historical records and remove values beyond Q3 + 1.5*IQR.
