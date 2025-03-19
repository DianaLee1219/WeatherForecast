# Forecas
ting model

* Built a basic forecasting model and evaluate its performance using different metrics.
* Used lastupdated feature for the time series analysis.

## How it works?

I've made significant progress via multiple iterations of model enhancement.

## Initial Model
* Basic **RandomFresetRegressor** model
  * 24 lag features (24 hours)
  * Simple datetime features (hour/day/month)
  * **train_test_split()** without scaling or hyperparameter tuning

* Model performance:
  * MAE: 2.928
  * MSE: 19.75
  * RMSE: 4.444
 ![image](https://github.com/user-attachments/assets/3ececb1b-4b4c-4932-8f81-7f509373f697)

* Trouble shooting:
  * Lack of cyclic encoding for datetime features
  * No scaling (hard to converge)
  * No hyperparameter tuning → Suboptimal model performance
  * Limited lag features → Insufficient temporal information

## Enhanced Model
* Feature Modeling:
  * Added cyclic encoding for hour and month to preserve temporal relationships
  * Added weekday and weekend binary feature to capture weekly patterns
* Increased to 72 lag features (3days)
* Feature Scaling:
  * Applied StandardScaler() → Normalizes feature values, improving model stability
* Model Modifications:
  * Increased n_estimators from 100 → 200
  * Added max_features='sqrt' → Prevents overfitting
* Model Performance:
  * MAE: 2.816 (↓ 3.8% improvement)
  * MSE: 17.84 (↓ 9.7% improvement)
  * RMSE: 4.224 (↓ 4.9% improvement)
 
![image](https://github.com/user-attachments/assets/374000d5-d917-457c-9f82-22f964c290e1)
