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

[Graph 2. The temperature distribution after removing outliers]
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

[Graph 3. The air quality PM2.5 distribution after removing outliers.]
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

[Graph 4. The temperature trend over time: The temperature drops down during winter season and it goes up during summer season.]

More information: MonthlyAverageTemperatures.txt

![image](https://github.com/user-attachments/assets/28f4a9e3-dd5e-47dd-ac37-e01baff15f7b)

[Graph 5. The temperature data has scaled to see the variation clearly]

![image](https://github.com/user-attachments/assets/1031cfa6-5b41-4135-a941-d5bd9c5bb2da)

[Graph 6. The temperature distribution by weather condition]

| Weather Condition  | Average Temperature (°C ) |
| ------------- | ------------- |
| Blowing snow | -2.02 |
| Heavy snow | 0.39 |
| Fog | 18.91 |
| Light rain | 19.01 |
| Clear | 19.16 |
| Mist | 19.76 |
| Moderate rain | 20.08 |
| Heavy rain | 22.51 |
| Cloudy | 22.84 |
| Partly cloudy | 24.52 |
| Sunny | 25.12 |

More information:  AverageTemperaturebyWeatherCondition.txt

![image](https://github.com/user-attachments/assets/fa176916-b270-4427-a59f-ca3ecff58d87)

[Graph 7. Wind speed data frequncy]
* One data has clipped into 410 during outlier removal process (originally it was 2963)
* Other data such as 272, 258, 205, 172 were identified as hurricane (>120kph)
![image](https://github.com/user-attachments/assets/217a9a44-4158-48af-8c87-c13e33b02d63)

[Graph 8. Correlation between temperature and humidity]
* Temperature and humidity is negatively correlated according to the graph.
  
![image](https://github.com/user-attachments/assets/d326eab6-4355-42ed-96e9-580e32bced88)

[Graph 9. Average temperature by country]

* Mean: 23.67 °C
* Median: 24.80 °C
* Min Temperature: 5.85 °C
* Max Temperature: 42.11 °C
* Standard Deviation: 5.97 °C
* Skewness: -0.27 (left-tailed)
* Kurtosis: 0.48 (Light-tailed)

![image](https://github.com/user-attachments/assets/706dd611-86c7-4736-aabb-d03caf83549f)
[Graph 10. Randomly selected 10 countries and boxploted showing temperature distributuion]
* Each time you run the script, different countries will appear in the plot, providing more diverse insights.


![image](https://github.com/user-attachments/assets/e13ca009-7a06-4250-a43b-d96f8c229a95)
[Graph 11. Distribution of precipitation (mm)]

📊 Precipitation Statistics:
* Mean: 0.16 mm
* Median: 0.00 mm
* Mode: 0.00 mm
* Skewness: 18.80 (>1, highly right-skewed)
* Kurtosis: 719.34 (>3, heavy-tailed distribution)
