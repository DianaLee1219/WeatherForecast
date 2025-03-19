import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Data loading
df = pd.read_csv('WeatherForecast_CleanedOutliers.csv')

# Conversion
df['last_updated'] = pd.to_datetime(df['last_updated'])
df.set_index('last_updated', inplace=True)

# Target variable
target = df['degC']

# Resampling
target = target.resample('H').mean().fillna(method='ffill')

# Feature engineering
target_df = pd.DataFrame(target)

# Add datetime features
target_df['day'] = target_df.index.day
target_df['weekday'] = target_df.index.weekday
target_df['is_weekend'] = target_df['weekday'].isin([5, 6]).astype(int)

# Extract hour and month before cyclic encoding
target_df['hour'] = target_df.index.hour
target_df['month'] = target_df.index.month

# Cyclic encoding
target_df['hour_sin'] = np.sin(2 * np.pi * target_df['hour'] / 24)
target_df['hour_cos'] = np.cos(2 * np.pi * target_df['hour'] / 24)
target_df['month_sin'] = np.sin(2 * np.pi * target_df['month'] / 12)
target_df['month_cos'] = np.cos(2 * np.pi * target_df['month'] / 12)

# Drop original hour and month
target_df.drop(['hour', 'month'], axis=1, inplace=True)

# Create lag features for 72 hours
for i in range(1, 73):
    target_df[f'lag_{i}'] = target_df['degC'].shift(i)

# Remove NaN values
target_df.dropna(inplace=True)

# Store datetime for plotting
target_df['datetime'] = target_df.index

# Prepare features and target
X = target_df.drop(['degC', 'datetime'], axis=1)
y = target_df['degC']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test, dt_train, dt_test = train_test_split(
    X_scaled, y, target_df['datetime'], test_size=0.2, shuffle=False
)

# Model training
model = RandomForestRegressor(n_estimators=200, max_features='sqrt', random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')

# Plotting with datetime
plt.figure(figsize=(10, 6))
plt.plot(dt_test, y_test, label='Actual')
plt.plot(dt_test, y_pred, label='Predicted')
plt.legend()
plt.show()
