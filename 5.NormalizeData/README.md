# Why Normalize Weather Data?
- Improves Model Performance: Many machine learning models (e.g., neural networks, gradient boosting) perform better when inputs are on a similar scale.
- Prevents Bias: Some variables (like pressure in mb) have much larger numerical values than others (like UV index), which can bias learning models.
- Speeds Up Convergence: Algorithms like gradient descent converge faster when data is normalized.
- Handles Outliers Better: Normalization helps in detecting and managing extreme values (outliers).

# Normalization Techniques
- Min-Max Scaling (Feature Scaling)
- Z-Score Normalization (Standardization)
- Log Transformation
- Max Abs Scaling

For this project, min-max scaling has applied to generate a heatmap!
