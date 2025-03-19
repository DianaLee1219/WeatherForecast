# Weather Forecasting model

* Built a basic forecasting model and evaluate its performance using different metrics.
* Enhanced the performance by multiple iterations and hyperparameter tuning
* Feature Importance Analysis was conducted

## Summary

I've made significant progress via multiple iterations of model enhancement.

| Model Version | MAE | MSE | RMSE | Key Features |
| --- | --- | --- | --- | --- |
| Initial Model (Baseline) | 2.928 | 19.75 | 4.444 | Basic RF, 24 lags |
| Enhanced Model | 2.816 (↓3.8%) | 17.84 (↓9.7%) | 4.224 (↓4.9%) | Feature engineering + scaling |
| Optimized Model | 2.755 (↓5.9%) | 17.43 (↓11.7%) | 4.175 (↓6.1%) | Hyperparameter tuning |

Feature Importance Analysis: Lagged temperature from 24 hours prior is the most influential.
## Initial Model
* Basic **RandomForestRegressor** model
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

## Optimized Model with RandomizedSearchCV
* Hyperparameter Optimization:
   * n_estimators: [100, 200, 300]
   * max_depth: [10, 20, 30, 40]
   * min_samples_split: [2, 5, 10]
   * min_samples_leaf: [1, 2, 4]
   * max_features: ['auto', 'sqrt', 'log2']
   * bootstrap: [True, False]
   * Best Parameters Identified:
   * n_estimators: 300
   * min_samples_split: 2
   * min_samples_leaf: 2
   * max_features: 'sqrt'
   * max_depth: 40
   * bootstrap: False
* Model Performance (ref: the Initial Model)
   * MAE: 2.755 (↓ 5.9%)
   * MSE: 17.43 (↓ 11.7%)
   * RMSE: 4.175 (↓ 6.1%)

## Additional: Feature Importance Analysis
* GridSearchCV + Feature Importance Analysis
* Key Finding:
   * lag_24 had the highest importance (0.5) → Lagged temperature from 24 hours prior is the most influential.
   * Most other features had importance < 0.1, indicating lower contribution.
![image](https://github.com/user-attachments/assets/9af79d12-360a-4440-b79c-94b0cc1a9775)

## Further Studies and Next Steps
There are several additional methods to enhance performance. Thus, I propose the following areas for further studies:

* Model Blending
   * Combining multiple models (RandomForest + XGBoost + LightGBM) can often improve accuracy.
 
* Switch to Gradient Boosting Models
   * Algorithms such as XGBoost or LightGBM may outperform RandomForest in time series forecasting tasks.
