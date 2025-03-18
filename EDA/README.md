# Exploratory Data Analysis (EDA)
## How it works?
The EDA performs data analysis on weather data, uncovering trends, correlations, and patterns through statistical computations and visualizations. It provides insights into temperature, precipitation, wind speed, air quality, etc.

📂 Input File: WeatherForecast_CleanedOutliers.cvs

📊 Output: Graphical visualizations and statistical summaries

Key analysis
* **Correlation heatmaps** identifying related variables.
* **Temperature** trends based on **seasonal changes**.
* **Weather condition** analysis related to **temperature** for different conditions.
* Randomized country selection ensuring diverse visualizations.
* **Precipitation** and **wind** analysis identifying **extreme weather events**.

## Results

![image](https://github.com/user-attachments/assets/554e7ac9-c762-4881-8193-a84348e389dd)

[Graph 1. The correlation heatmap shows relationships between weather variables]
* Positive correlations:
  * **Temperature** strongly correlates with **Feels Like Temperature** (0.97) and moderately with **UV Index** (0.49).
* Negative correlations:
  * **Humidity** shows a moderate inverse relationship with **UV Index** (-0.57) and **Air Quality (Ozone)** (-0.50).
  * **Air Quality (NO₂)** is moderately negatively correlated with **Temperature** (-0.43) and **Feels Like Temperature** (-0.42).

![image](https://github.com/user-attachments/assets/24044ca9-9916-4d73-a681-d4e40246cd3a)

[Graph 2. Temperature distribution]
* Mean: 23.64 °C
* Median: 25.40 °C
* Mode: 28.20 °C
* Standard Deviation: 7.83
* Skewness: -0.94 (Left-skewed)
* Kurtosis: 0.98 (Light-tailed)

![image](https://github.com/user-attachments/assets/5d25c38e-3509-4eea-accf-d89739dde7e3)

[Graph 3. Air quality PM2.5 distribution]
* Mean: 12.58 (µg/m3)
* Median: 9.62 (µg/m3)
* Mode: 0.50 (µg/m3)
* Standard Deviation: 10.67
* Skewness: 1.11 (Left-skewed)
* Kurtosis: 0.58 (Light-tailed)

![image](https://github.com/user-attachments/assets/1fa5d251-6343-4e21-bab1-6c9baf9b62f8)

[Graph 4. Temperature Trend Over Time]
* The temperature fluctuates seasonally
* This trend plot implies potential climate patterns over the year.

![image](https://github.com/user-attachments/assets/28f4a9e3-dd5e-47dd-ac37-e01baff15f7b)

[Graph 5. The temperature data has scaled to see the variation clearly]

![image](https://github.com/user-attachments/assets/1031cfa6-5b41-4135-a941-d5bd9c5bb2da)

[Graph 6. The temperature distribution by weather condition]

The average temperature varies significantly by weather type:

* **Cold Conditions**: Blowing snow (-2.02 °C) and Heavy snow (0.39 °C).
* **Moderate Weather**: Light rain (19.01 °C) and Cloudy (22.84 °C).
* **Hot Weather**: Sunny (25.12 °C) and Partly cloudy (24.52 °C).

![image](https://github.com/user-attachments/assets/217a9a44-4158-48af-8c87-c13e33b02d63)

[Graph 7. Correlation between temperature and humidity]
* Temperature and humidity is negatively correlated according to the graph.
  
![image](https://github.com/user-attachments/assets/d326eab6-4355-42ed-96e9-580e32bced88)

[Graph 8. Temperature by country]

* Mean: 23.67 °C
* Median: 24.80 °C
* Min Temperature: 5.85 °C
* Max Temperature: 42.11 °C
* Standard Deviation: 5.97 °C
* Skewness: -0.27 (slightly left-tailed)
* Kurtosis: 0.48 (Light-tailed)

![image](https://github.com/user-attachments/assets/706dd611-86c7-4736-aabb-d03caf83549f)
[Graph 9. Random Country Temperature Distribution]
* Each time you run the script, different countries will appear in the plot, providing more diverse insights.


![image](https://github.com/user-attachments/assets/e13ca009-7a06-4250-a43b-d96f8c229a95)
[Graph 10. Distribution of precipitation]

* Mean: 0.16 mm/h
* Median: 0.00 mm/h
* Mode: 0.00 mm/h
* Skewness: 18.80 (>1, highly right-skewed)
* Kurtosis: 719.34 (>3, heavy-tailed)

The precipitation data shows extreme skewness and kurtosis due to outliers from heavy showers (10-50 mm/h). Most of the data corresponds to light or no precipitation.


![image](https://github.com/user-attachments/assets/fa176916-b270-4427-a59f-ca3ecff58d87)

[Graph 11. Wind Speed Outliers]

* Outliers were detected and clipped during preprocessing:
** One extreme value was clipped to 410 kph (original: 2963 kph).
** Other hurricane-level winds (e.g., 272, 258, 205, 172 kph) were also identified.
