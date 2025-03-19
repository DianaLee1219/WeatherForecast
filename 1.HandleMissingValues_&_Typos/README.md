# Handling Missing Values and Typos
## How does it work?

A significant number of typos in the **country** and **location_name (city)** fields were identified. 

To speed up this correction process, a powerful built-in tool has been applied:


➡ **Google Sheets → Data → Data Cleanup Recommendations**

Additionally, while analyzing the column data, more typos were identified by detecting rows with only **one or two** timestamps, whereas most records contained around **300 entries**.

## How were corrections made?
* Verified locations by searching their **latitude and longitude** on **Google Maps**.
* Double-checked the results using the corresponding **time zone** information to ensure accuracy.
  
By following this approach, missing values were effectively handled and the data consistency has improved.

## History of Corrections

* All corrections were based on latitude, longitude, and time zone validation.
* Rows with only one data point were removed to maintain dataset consistency.
* Google Sheets' Data Cleanup Tool and manual Google Maps verification were used for accuracy.
* Detailed correction history can be found in History.txt.

## MissingValue.py: Identifying Missing Values

To further improve data quality, I wrote a Python script (MissingValue.py) to detect missing values in the dataset.

**How It Works**: This script reads the dataset from a CSV file and checks for any missing (empty) values in each column.

Key Features:

* Reads the dataset from a CSV file.
* Handles encoding errors (prevents issues caused by special characters).
* Detects missing values (NaN) in each column.
* Displays only columns with missing values, making it easier to identify and fix them.
