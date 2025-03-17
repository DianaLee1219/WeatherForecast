# Handling Missing Values and Typos
## How does it work?

Most of the work related to handling missing values and correcting typos was done manually.

I noticed a significant number of typos in the **country** and **location_name (city)** fields. 

To speed up the correction process, I used a powerful built-in tool:


➡ **Google Sheets → Data → Data Cleanup Recommendations**

Additionally, while analyzing column data, I identified more typos by detecting rows with only **one or two** timestamps, whereas most records contained around **300 entries**.

## How were corrections made?
* I verified locations by searching their **latitude and longitude** on **Google Maps**.
* I double-checked the results using the corresponding **time zone** information to ensure accuracy.
  
By following this approach, I effectively handled missing values and improved data consistency.

## History of Corrections
Notes:

* All corrections were based on latitude, longitude, and time zone validation.
* Rows with only one data point were removed to maintain dataset consistency.
* Google Sheets' Data Cleanup Tool and manual Google Maps verification were used for accuracy.

Can be found in the History.txt file.
