## This code is followed by the EnhancedModel.py

from sklearn.model_selection import RandomizedSearchCV

# Define hyperparameters
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, 40],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2'],
    'bootstrap': [True, False]
}

# Randomized search
rf = RandomForestRegressor(random_state=42)
random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_grid,
    n_iter=50,           # Number of random combinations
    cv=5,                # Cross-validation folds
    scoring='neg_mean_squared_error',
    n_jobs=-1,           # Use all CPUs
    random_state=42
)

# Fit the model
random_search.fit(X_train, y_train)

# Best model and prediction
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Best Parameters:", random_search.best_params_)
print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
