import pandas as pd

# Load the CSV file
file_path = 'Construction_Data_PM_Tasks_All_Projects.csv'

# Read the data
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Display basic information about the data
print("\nFirst 5 rows of the original data:")
print(data.head())
print("\nColumn names in the original data:")
print(data.columns)

# Check for NaN/NULL values in the column
nan_count = data['OverDue'].isna().sum()
print(f"\nNumber of NaN/NULL values in 'OverDue': {nan_count}")

# Unique values in the column
print("\nUnique values in 'OverDue':")
print(data['OverDue'].unique())

# Define the filtering criteria
desired_value = True

# Filter the data
filtered_data = data[data['OverDue'] == desired_value]

# Display the filtered data
print("\nFiltered data:")
print(filtered_data.head())

# Display the count of filtered rows
print("\nCount of filtered rows:")
print(len(filtered_data))
