# Exploratory Data Analysis (EDA)
## How it works?
* It performs EDA to uncover the trends, correlations, and patterns. Including visualizations for temperature and precipitation.

📂 Input File: WeatherForecast_CleanedOutliers.cvs 

## Results

![image](https://github.com/user-attachments/assets/554e7ac9-c762-4881-8193-a84348e389dd)

[Graph 1. the correlation heatmap showing correlation between all the numerical data in the dataset]
* Positive correlation
  * 'Temperature' was stronlgy correlated with 'feels like temperater'(0.97) and was moderately correlated with 'UV index' (0.49), which is moderately related with 'feels like temperater'(0.40). 
* Negative correlation
  * 'Humidity' was moderately related to 'UV index' (-0.57) and 'air quality (Ozone)' (-0.5).
  * 'Air quality (NO2)' was moderately related to 'temperature' (-0.43) and 'feels like temperater'(-0.42).

![image](https://github.com/user-attachments/assets/24044ca9-9916-4d73-a681-d4e40246cd3a)

[Graph 2. The temperature distribution graph after removing outliers]
* Mean: 23.64 °C
* Median: 25.40 °C
* Mode: 28.20 °C
* Standard Deviation: 7.83
* Min Temperature: -6.60 °C 
* Max Temperature: 47.80 °C
* Range: 54.40 °C
* Skewness: -0.94 (Left-skewed)
* Kurtosis: 0.98 (Light-tailed)

![image](https://github.com/user-attachments/assets/5d25c38e-3509-4eea-accf-d89739dde7e3)

[Graph3. The air quality PM2.5 distribution graph after removing outliers.]
* Mean: 12.58 (µg/m3)
* Median: 9.62 (µg/m3)
* Mode: 0.50 (µg/m3)
* Standard Deviation: 10.67
* Min PM2.5: 0.18 (µg/m3)
* Max PM2.5: 46.80 (µg/m3)
* Range: 54.40 (µg/m3)
* Skewness: 1.11 (Left-skewed)
* Kurtosis: 0.58 (Light-tailed)

![image](https://github.com/user-attachments/assets/1fa5d251-6343-4e21-bab1-6c9baf9b62f8)

[Graph 4. The temerature trend over time]
As you can see on the graph, the temperature drops down during winter season and it goes up during summer season.

![image](https://github.com/user-attachments/assets/28f4a9e3-dd5e-47dd-ac37-e01baff15f7b)

📅 Monthly Average Temperatures (°C ):
* 2024-05-31     25.29
* 2024-06-30     26.22
* 2024-07-31     26.41
* 2024-08-31     26.51
* 2024-09-30     24.83
* 2024-10-31     22.61
* 2024-11-30     21.57
* 2024-12-31     20.38
* 2025-01-31     20.49
* 2025-02-28     20.41
* 2025-03-31     21.10

![image](https://github.com/user-attachments/assets/5c3b4a03-d01f-4e15-8d1f-cd0b01d2eacb)

[Graph5. The temperature distribution by weather condition]

🌤️ Average Temperature (°C ) by Weather Condition (examples):
* Blowing snow                                   -2.02
* Heavy snow                                      0.39
* Fog                                            18.91
* Light rain                                     19.01
* Clear                                          19.16
* Mist                                           19.76
* Moderate rain                                  20.08
* Heavy rain                                     22.51
* Cloudy                                         22.84
* Partly cloudy                                  24.52
* Sunny                                          25.12

  -> More information  AverageTemperaturebyWeatherCondition.txt

![image](https://github.com/user-attachments/assets/7e0368d8-8553-46ee-b12f-d6c661d98f22)

![image](https://github.com/user-attachments/assets/d86383bb-6638-4113-9602-6c7323878491)

* One data has clipped into 410 (originally it was 2963)
* Other data such as 272, 258, 205, 172 were identified as hurricane (>120kph)

![image](https://github.com/user-attachments/assets/d326eab6-4355-42ed-96e9-580e32bced88)

*
