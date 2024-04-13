import pandas as pd
import datetime
from tabulate import tabulate

# Load the CSV file
file_path = 'Construction_Data_PM_Forms_All_Projects.csv'

# Read the data
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Ensure columns are available in the data
if 'Created' not in data.columns or 'Project' not in data.columns:
    print("\n'Created' or 'Project' column not found in the data.")
    exit()

# Convert 'Created' column to datetime format
data['Created'] = pd.to_datetime(data['Created'])

# Get today's date
current_datetime = datetime.datetime.now()

data['Elapsed Days'] = (current_datetime - data['Created']).dt.days

# Calculate mean elapsed time for each category
mean_elapsed_per_category = data.groupby('Project')['Elapsed Days'].mean().reset_index()

# Display the result in a tabular format
print(tabulate(mean_elapsed_per_category, headers='keys', tablefmt='grid'))
