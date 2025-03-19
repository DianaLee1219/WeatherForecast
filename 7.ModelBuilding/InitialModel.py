import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
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

target_df = pd.DataFrame(target)
target_df['hour'] = target_df.index.hour
target_df['day'] = target_df.index.day
target_df['month'] = target_df.index.month

for i in range(1, 25):  # Create lag features for the past 24 hours
    target_df[f'lag_{i}'] = target_df['degC'].shift(i)

target_df.dropna(inplace=True)

X = target_df.drop('degC', axis=1)
y = target_df['degC']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')

plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test, label='Actual')
plt.plot(y_test.index, y_pred, label='Predicted')
plt.legend()
plt.show()
