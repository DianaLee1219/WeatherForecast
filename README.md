# WeatherForecast Project - Data Science
A data science project that analyze and forecasts weather conditions using machine learning models. 
This project covers **data cleaning & preprocessing, exploratory data analysis (EDA)**, **model building**, and **evaluation**. 

Details are described in each section.

## 🛠️ **Technologies Used**
- **Languages:** Python  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`
- **Dataset:** [Kaggle World Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository/code)
- **Modeling:** RandomForestRegressor 
- **Evaluation Metrics:** MAE (Mean Absolute Error), MSE (Mean Squared Error), and RMSE (Root Mean Squared Error)

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

7. The forecasting model is built using **RandomForestRegressor** and evaluated using MAE, MSE, and RMSE
