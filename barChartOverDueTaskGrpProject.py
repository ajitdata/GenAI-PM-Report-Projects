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
    print("\nStatus or Task Group not found in the data.")
    exit()
# Define specific values to filter in Column1
specific_values = [True]

# Filter data for specific values in Column1
filtered_data = data[data['OverDue'].isin(specific_values)]

# Get count of rows for each combination of Column1 and Column2 values
grouped_counts = data.groupby(['project', 'OverDue']).size().reset_index(name='Count')

# Sort the data based on Column2
grouped_counts = grouped_counts.sort_values(by='project')

# Plot bars for each specific value in Column1
for value in specific_values:
    subset = grouped_counts[grouped_counts['OverDue'] == value]
    plt.bar(subset['project'].astype(str) + f" ({value})", subset['Count'], label=str(value))

plt.title('OverDue Tasks Count Grouped by "project code"')
plt.xlabel('Project')
plt.ylabel('Count')
plt.legend(title='OverDue', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
