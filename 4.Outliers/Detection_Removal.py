import pandas as pd
import numpy as np

# Load the data
file_path = "WeatherForecast_CleanedUnits.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Define realistic limits for each variable
limits = {
    "degC": (-90, 57),
    "wind_kph": (0, 410),
    "pressure_mb": (870, 1085),
    "precip_mm": (0, 2000),
    "humidity": (0, 100),
    "feels_like_celsius": (-100, 60),
    "visibility_km": (0, 100),
    "uv_index": (0, 24),
    "air_quality_Ozone": (0, 400),
    "air_quality_Nitrogen_dioxide": (0, 300),
    "air_quality_PM2.5": (0, 600)
}
# IQR method list
iqr_columns = ["pressure_mb", "air_quality_Ozone", "air_quality_Nitrogen_dioxide", "air_quality_PM2.5"]

# Z-score method list
zscore_columns = ["degC", "feels_like_celsius"]


# Feature Clipping
def clip_values(df, limits):
    for col, (lower, upper) in limits.items():
        if col in df.columns:
            df[col] = df[col].clip(lower=lower, upper=upper)
    return df


# IQR-Based Outlier Detection & Removal
def detect_outliers_iqr(df, columns):
    for col in columns:
        if col in df.columns:
            Q1, Q3 = df[col].quantile([0.25, 0.75])
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Print identified outliers
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            if not outliers.empty:
                print(f"\n {col}: IQR Outliers Detected ({len(outliers)} rows)")
                print(outliers[["location_name", col]].head(10))  # Show sample outliers

            # Remove Outliers
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# Z-Score Outlier Detection & Removal
def detect_outliers_zscore(df, columns, threshold=3):
    df = df.copy()  # Avoid SettingWithCopyWarning
    for col in columns:
        if col in df.columns:
            mean = df[col].mean()
            std = df[col].std()
            df["z_score"] = (df[col] - mean) / std
            
            # Identify outliers
            outliers = df[abs(df["z_score"]) > threshold]
            if not outliers.empty:
                print(f"\n {col}: Z-Score Outliers Detected ({len(outliers)} rows)")
                print(outliers[["location_name", col, "z_score"]].head(10))  # Show sample outliers
            
            # Remove outliers
            df = df[abs(df["z_score"]) <= threshold]
    return df

df = detect_outliers_zscore(df, zscore_columns)
df = clip_values(df, limits)
df = detect_outliers_iqr(df, iqr_columns)

# Save the cleaned data
df.to_csv("WeatherForecast_CleanedOutliers.csv", index=False)
print("Processed data saved as WeatherForecast_CleanedOutliers.csv")
