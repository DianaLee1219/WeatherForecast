## Why it is important?
Removing unnecessary data is the first step in data cleaning. By eliminating irrelevant information, you can focus on handling only the essential data, improving efficiency and accuracy in data analysis.

## What is the standard for relevant data?

To define relevant weather data, I analyzed the Weather app on my iPhone 12 and identified its key features. Based on the app’s layout (from top to bottom), I categorized the features into two levels:

1. Basic Features: Time series, location, temperature, condition
2. Advanced Features: Feels-like temperature, air quality (PM2.5, ozone, NO₂), precipitation, UV index, sunrise, sunset, wind direction, humidity, visibility, and pressure

After downloading the dataset from Kaggle (World Weather Repository: https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code), 

I removed irrelevant columns from the GlobalWeatherRepository.csv file. The following features were excluded:

•	Wind degree
•	Cloud coverage
•	Gust speed
•	Air quality indices (CO₂, SO₂, PM10, US-EPA index, GB-DEFRA index)
•	Moonrise/Moonset times

By filtering out unnecessary data, the dataset becomes more structured and aligned with real-world weather applications.


## Additional Information - Air Quality
1️⃣ PM2.5 (Fine Particulate Matter)
•	Why important? PM2.5 particles are small enough to enter deep into the lungs and even the bloodstream, causing severe respiratory and cardiovascular issues.
•	Health Effects: Increases risks of asthma, lung disease, and heart attacks.
•	Source: Emissions from vehicles, industrial processes, wildfires, and combustion.

2️⃣ Ozone (O₃)
•	Why important? Ground-level ozone is a primary component of smog and can cause severe lung irritation and breathing issues.
•	Health Effects: Can trigger asthma attacks and reduce lung function over time.
•	Source: Forms when pollutants react with sunlight (commonly from vehicle emissions).

3️⃣ Nitrogen Dioxide (NO₂)
•	Why important? NO₂ is a major air pollutant that contributes to respiratory diseases and forms secondary pollutants like ozone and PM2.5.
•	Health Effects: Causes airway inflammation, lung damage, and increased vulnerability to respiratory infections.
•	Source: Emissions from vehicles, power plants, and industrial activities.
