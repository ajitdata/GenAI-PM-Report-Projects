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

# Ensure columns are available in the data
if 'Report Status' not in data.columns or 'Task Group' not in data.columns:
    print("\nReport Status or Task Group not found in the data.")
    exit()

# Get count of rows for each combination of Column1 and Column2 values
grouped_counts = data.groupby(['Task Group', 'Report Status']).size().reset_index(name='Count')


# Display the results
print("\nCount of distinct values in Column1 for each value in Column2:")
print(grouped_counts)
