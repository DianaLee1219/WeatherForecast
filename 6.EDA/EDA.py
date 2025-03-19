import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import random
from sklearn.preprocessing import MinMaxScaler

# Load the data
file_path = "EDA_cleaned_weather_data.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Select only numeric columns
numeric_data = df.select_dtypes(include=['number'])

# Compute correlation matrix
corr_matrix = numeric_data.corr()

# Plot heatmap
plt.figure(figsize=(16, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
______________________________________________________________________

# Load the data
file_path = "WeatherForecast_CleanedOutliers.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Basic statistics
mean_temp = df['degC'].mean()
median_temp = df['degC'].median()
mode_temp = df['degC'].mode()[0]
std_temp = df['degC'].std()
min_temp = df['degC'].min()
max_temp = df['degC'].max()
range_temp = max_temp - min_temp
skewness = skew(df['degC'])
kurt = kurtosis(df['degC'])

# Print statistics
print("\n **Temperature Statistics**")
print(f"Mean: {mean_temp:.2f} °C")
print(f"Median: {median_temp:.2f} °C")
print(f"Mode: {mode_temp:.2f} °C")
print(f"Standard Deviation: {std_temp:.2f}")
print(f"Min Temperature: {min_temp:.2f} °C")
print(f"Max Temperature: {max_temp:.2f} °C")
print(f"Range: {range_temp:.2f} °C")
print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurt:.2f}")

# Visualization
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(df['degC'], bins=30, kde=True, color='skyblue')
plt.title("Temperature Distribution (Histogram)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x=df['degC'], color='lightgreen')
plt.title("Temperature Distribution (Boxplot)")
plt.xlabel("Temperature (°C)")

plt.tight_layout()
plt.show()

mean_pm = df['air_quality_PM2.5'].mean()
median_pm = df['air_quality_PM2.5'].median()
mode_pm = df['air_quality_PM2.5'].mode()[0]
std_pm = df['air_quality_PM2.5'].std()
min_pm = df['air_quality_PM2.5'].min()
max_pm = df['air_quality_PM2.5'].max()
range_pm = max_temp - min_temp
skewness = skew(df['air_quality_PM2.5'])
kurt = kurtosis(df['air_quality_PM2.5'])

# Print statistics
print("\n **Air Quality Statistics**")
print(f"Mean: {mean_pm:.2f} (µg/m3)")
print(f"Median: {median_pm:.2f} (µg/m3)")
print(f"Mode: {mode_pm:.2f} (µg/m3)")
print(f"Standard Deviation: {std_pm:.2f}")
print(f"Min PM2.5: {min_pm:.2f} (µg/m3)")
print(f"Max PM2.5: {max_pm:.2f} (µg/m3)")
print(f"Range: {range_pm:.2f} (µg/m3)")
print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurt:.2f}")

# Visualization
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(df['air_quality_PM2.5'], bins=30, kde=True, color='skyblue')
plt.title("PM2.5 Air Quality Distribution (Histogram)")
plt.xlabel("PM2.5 (µg/m3)")
plt.ylabel("Frequency")

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x=df['air_quality_PM2.5'], color='lightgreen')
plt.title("PM2.5 Air Quality Distribution (Boxplot)")
plt.xlabel("PM2.5 (µg/m3)")

plt.tight_layout()
plt.show()

# Convert to datetime and set as index
df['last_updated'] = pd.to_datetime(df['last_updated'])
df.set_index('last_updated', inplace=True)

# Resample data by month and calculate the average temperature
monthly_avg_temp = df['degC'].resample('M').mean()

# Plotting
plt.figure(figsize=(16, 6))
monthly_avg_temp.plot(marker='o', linestyle='-', color='royalblue')
plt.title("Average Monthly Temperature Trend")
plt.xlabel("Date (Year-Month)")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.show()

# Resample by month to get the average temperature
monthly_avg_temp = df['degC'].resample('M').mean()

# Print the average temperature for each month
print("\n Monthly Average Temperatures:")
print(monthly_avg_temp.round(2).to_string())

# Plotting
plt.figure(figsize=(16, 6))

# Daily temperature trend (line plot)
plt.plot(df.index, df['degC'], label='Daily Temperature', color='royalblue', linewidth=0.8)

# Monthly average temperature markers (red markers)
plt.plot(monthly_avg_temp.index, monthly_avg_temp, marker='o', linestyle='-', color='red', label='Monthly Average')

# Labels and legend
plt.title("Temperature Trend with Monthly Averages")
plt.xlabel("Date (Year-Month)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.show()

# Calculate monthly average temperatures
monthly_avg_temp = df['degC'].resample('M').mean()

# Print the average temperature per weather condition (ascending order)
avg_temp_per_condition = df.groupby('condition_text')['degC'].mean().round(2).sort_values()
print("\n🌤️ Average Temperature by Weather Condition (Ascending Order):")
print(avg_temp_per_condition.to_string())

# Boxplot for temperature by condition
plt.figure(figsize=(25, 6))
sns.boxplot(data=df, x='condition_text', y='degC')
plt.title("Temperature Distribution by Weather Condition")
plt.xlabel('Weather Condition', fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)
plt.xticks(rotation=80)
plt.show()

# Load the data
file_path = "WeatherForecast_CleanedOutliers.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Boxplot for wind speed
sns.boxplot(data=df, x='wind_kph')
plt.title("Wind Speed")
plt.ylabel('Frequency', fontsize=14)
plt.xlabel("Wind Speed (kph)", fontsize=14)
plt.show()

# Temperature vs. Humidity
sns.scatterplot(data=df, x='degC', y='humidity')
plt.title("Temperature vs. Humidity")
plt.ylabel('Humidity (%)', fontsize=14)
plt.xlabel("Temperature (°C)", fontsize=14)
plt.show()

# Average temperature by country
avg_temp_by_country = df.groupby('country')['degC'].mean().sort_values()

# Print statistical insights
print("\n🌎 Average Temperature by Country:")
print(f"Mean: {avg_temp_by_country.mean():.2f} °C")
print(f"Median: {avg_temp_by_country.median():.2f} °C")
print(f"Min Temperature: {avg_temp_by_country.min():.2f} °C")
print(f"Max Temperature: {avg_temp_by_country.max():.2f} °C")
print(f"Standard Deviation: {avg_temp_by_country.std():.2f} °C")
print(f"Skewness: {avg_temp_by_country.skew():.2f}")
print(f"Kurtosis: {avg_temp_by_country.kurtosis():.2f}")

# Bar plot
avg_temp_by_country.plot(kind='bar', figsize=(35, 8), color='skyblue')
plt.title("Average Temperature by Country")
plt.xlabel('Country', fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)
plt.show()

# Randomly select top countries
top_countries = df['country'].value_counts().index
random_countries = random.sample(list(top_countries), 10)  # Select 10 random countries

# Boxplot Visualization
plt.figure(figsize=(15, 6))
sns.boxplot(data=df[df['country'].isin(random_countries)],
            x='country', y='degC', palette='coolwarm')

plt.title('Boxplot of Temperature by Random Countries', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
