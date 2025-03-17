# Delete Insufficient Data

## Why it is necessary?

For weather forecasting models, having sufficient data is crucial for accurate analysis and predictions.

While examining missing values and typos, I identified that some cities contained only one or two timestamps, whereas most records had around 300 entries.

To ensure data consistency and reliability, I decided to analyze the number of data entries for each city. If a city had fewer than 200 entries, I excluded it from the dataset to maintain a meaningful analysis.

## How does it work?

1. Count the number of data entries for each city.
2. Remove the corresponding rows from the dataset if a city has fewer than 200 entries.
3. Visualize the results by plotting a before-and-after graph:
   * x-axis is city names
   * y-axis is the number of data

## Results
![image](https://github.com/user-attachments/assets/205c8241-ba2f-4973-8cd0-3770959d26eb)
![image](https://github.com/user-attachments/assets/70ba77ea-da92-40b1-9982-078ef0500df6)
