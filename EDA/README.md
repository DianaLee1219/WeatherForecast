# Exploratory Data Analysis (EDA)
## How it works?
* It performs EDA to uncover the trends, correlations, and patterns. Including visualizations for temperature and precipitation.

📂 Input File: WeatherForecast_CleanedOutliers.cvs 

## Results

![image](https://github.com/user-attachments/assets/554e7ac9-c762-4881-8193-a84348e389dd)

This is the correlation heatmap showing correlation between all the numerical data in the dataset.
* Positive correlation
  * 'Temperature' was stronlgy correlated with 'feels like temperater'(0.97) and was moderately correlated with 'UV index' (0.49), which is moderately related with 'feels like temperater'(0.40). 
* Negative correlation
  * 'Humidity' was moderately related to 'UV index' (-0.57) and 'air quality (Ozone)' (-0.5).
  * 'Air quality (NO2)' was moderately related to 'temperature' (-0.43) and 'feels like temperater'(-0.42).

![image](https://github.com/user-attachments/assets/24044ca9-9916-4d73-a681-d4e40246cd3a)

This is the temperature distribution graph after removing outliers. 
* Mean: 23.64 °C
* Median: 25.40 °C
* Mode: 28.20 °C
* Standard Deviation: 7.83
* Min Temperature: -6.60 °C 
* Max Temperature: 47.80 °C
* Range: 54.40 °C
* Skewness: -0.94 (Left-skewed)
* Kurtosis: 0.98 (Light-tailed distribution)

![image](https://github.com/user-attachments/assets/5d25c38e-3509-4eea-accf-d89739dde7e3)
This is the air quality PM2.5 distribution graph after removing outliers. 
* Mean: 12.58 (µg/m3)
* Median: 9.62 (µg/m3)
* Mode: 0.50 (µg/m3)
* Standard Deviation: 10.67
* Min PM2.5: 0.18 (µg/m3)
* Max PM2.5: 46.80 (µg/m3)
* Range: 54.40 (µg/m3)
* Skewness: 1.11
* Kurtosis: 0.58
