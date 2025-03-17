## Why it is important?
Removing uneccassary data is the first thing to do in data science.
So that you can focus on handling important data only!

## What is the standard of relevant data?

I benchmarked the weatherforecast application on my iphone 12, and extracted main features.
Then I made a hierachy based on the order (from top to bottom of the app).
1. Basic features: time series, location, temperature, condition
2. Advanced features: feels like temperature, air quality (PM2.5, ozone, NO2), precipitation, UV index, sunrise, sunset, wind direction, humidity, visibility, pressure

Therefore, after I downloaded the dataset from kaggle (World Weather Repository: https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code)
I extracted irrelevant data from the "GlobalWeatherRepository.csv"
•	wind degree, cloud, gust, air quality (CO2, SO2, PM10, us-epa-index, gb-defra-index), moon rise/fall

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
