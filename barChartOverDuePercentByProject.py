import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'Construction_Data_PM_Tasks_All_Projects.csv'

# Read the data
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Ensure columns are available in the data
if 'OverDue' not in data.columns or 'project' not in data.columns:
    print("\nColumn1 or Column2 not found in the data.")
    exit()

# Define specific value to focus on in Column1
specific_value = True

# Get count of rows for each combination of Column1 and Column2 values
grouped_counts = data.groupby(['project', 'OverDue']).size().reset_index(name='Count')

# Calculate the total counts for each group in Column2
total_counts = grouped_counts.groupby('project')['Count'].sum().reset_index(name='TotalCount')

# Merge total counts back to grouped_counts DataFrame
grouped_counts = pd.merge(grouped_counts, total_counts, on='project')

# Calculate the percentage
grouped_counts['Percentage'] = (grouped_counts['Count'] / grouped_counts['TotalCount']) * 100

# Filter for the specific value in Column1
specific_value_data = grouped_counts[grouped_counts['OverDue'] == specific_value]

# Creating a bar chart for percentage
plt.figure(figsize=[10,6])
plt.bar(specific_value_data['project'].astype(str), specific_value_data['Percentage'])
plt.title(f'Percentage of {specific_value} in OverDue Grouped by project')
plt.xlabel('project')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
