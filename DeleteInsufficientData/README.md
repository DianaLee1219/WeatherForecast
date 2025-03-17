# Delete Insufficient Data

## Why it is necessary?

For an accurate weather forecasting model, having a sufficient amount of data per city is essential. Inconsistent or insufficient data can lead to unreliable analysis and predictions.

During handling missing values and typos, I noticed that while most cities had around 300 data entries, some had fewer than 200, with a few containing only one or two timestamps. Such sparse data points are not useful for meaningful analysis.

To ensure data consistency and improve model performance, I decided to remove cities with fewer than 200 data entries.


## How does it work?

1. **Count the number of data entries** for each city using the location_name column.
2. Identify cities with **fewer than 200 entries** and print their names along with their data counts.
3. **Remove** these cities from the dataset to maintain statistical reliability.
4. **Visualize** the data **before and after** cleaning using bar graphs:
   * x-axis is city names
   * y-axis is the number of data

## Results

Below are the visualizations of data distribution before and after cleaning. The first graph shows the number of data entries per city before filtering, while the second graph shows the distribution after removing cities with insufficient data. After this process, the cleaned dataset is saved as cleaned_data.csv. 

![image](https://github.com/user-attachments/assets/205c8241-ba2f-4973-8cd0-3770959d26eb)
![image](https://github.com/user-attachments/assets/70ba77ea-da92-40b1-9982-078ef0500df6)
