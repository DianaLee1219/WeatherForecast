# WeatherForecast Project - Data Science
A data science project that analyze and forecasts weather conditions using machine learning models. 
This project covers **data cleaning, exploratory data analysis (EDA)**, and **model building** with detailed evaluation. 

Details are described in each section.

## 🛠️ **Technologies Used**
- **Languages:** Python  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`  
- **Modeling:** RandomForestRegressor with `TimeSeriesSplit`  
- **Evaluation Metrics:** MAE, MSE, RMSE  

## Data Cleaning & Preprocessing

0. **Delete irrelevant data** : Drop columns that do not contribute to weather forecasting.  
1. **Handle missing values & Typos** : Apply google auto-tool and column analysis to handle missing values and typos.
2. **Delete insufficient data** : Remove rows with small amount of entries (<200)
3. **Standarize data** : Standarize numerical features (speed or temperature units).
4. **Outlier removal**: Apply **feature clipping**, **z-score**, or **IQR filtering** to detect and remove extreme values.  
5. **Normalize data** : Scale the features using Min-Max Scaler.

## Exploratory Data Analysis (EDA)

6. EDA is performed to **uncover trends, correlations, and patterns** in the data

## Model Building

7. The forecasting model is built using **RandomForestRegressor** and evaluated using MAE (Mean Absolute Error), MSE (Mean Squared Error), and RMSE (Root Mean Squared Error)
