import pandas as pd

file_path = "HandleMissingValues_&_Typos_Result.csv"  

try:
    df = pd.read_csv(file_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="ISO-8859-1") 

# Finding empty values
missing_values = df.isnull().sum()

# Results
print("Missing Values per Column:")
print(missing_values[missing_values > 0])
