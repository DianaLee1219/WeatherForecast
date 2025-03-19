import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load the data
file_path = "WeatherForecast_CleanedOutliers.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

scaler = MinMaxScaler()
numerical_columns = ["degC", "wind_kph", "pressure_mb", "precip_mm", "humidity", "feels_like_celsius", "visibility_km", 
                     "uv_index", "air_quality_Ozone", "air_quality_Nitrogen_dioxide", "air_quality_PM2.5"]
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

df.to_csv("EDA_cleaned_weather_data.csv", index=False)
