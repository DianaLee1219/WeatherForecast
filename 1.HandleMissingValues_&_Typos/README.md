# Handling Missing Values and Typos
## How does it work?

I corrected typos using Python code and identified missing values afterward.

Most of the work related to correcting typos was done manually.

I noticed a significant number of typos in the **country** and **location_name (city)** fields. 

To speed up the correction process, I used a powerful built-in tool:


➡ **Google Sheets → Data → Data Cleanup Recommendations**

Additionally, while analyzing column data, I identified more typos by detecting rows with only **one or two** timestamps, whereas most records contained around **300 entries**.

## How were corrections made?
* I verified locations by searching their **latitude and longitude** on **Google Maps**.
* I double-checked the results using the corresponding **time zone** information to ensure accuracy.
  
By following this approach, I effectively handled missing values and improved data consistency.

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
