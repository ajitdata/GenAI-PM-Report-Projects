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
if 'Status' not in data.columns or 'Task Group' not in data.columns:
    print("\nStatus or Task Group not found in the data.")
    exit()
# Define specific values to filter in Column1
specific_values = ['Open', 'Closed']

# Filter data for specific values in Column1
filtered_data = data[data['Status'].isin(specific_values)]

# Get count of rows for each combination of Column1 and Column2 values
grouped_counts = data.groupby(['Task Group', 'Status']).size().reset_index(name='Count')

# Sort the data based on Column2
grouped_counts = grouped_counts.sort_values(by='Task Group')

# Plot bars for each specific value in Column1
for value in specific_values:
    subset = grouped_counts[grouped_counts['Status'] == value]
    plt.bar(subset['Task Group'].astype(str) + f" ({value})", subset['Count'], label=str(value))

plt.title('"Open" and "Closed" Status Count Grouped by "Task Group"')
plt.xlabel('Task Group')
plt.ylabel('Count')
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
