import pandas as pd
import matplotlib.pyplot as plt

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
if 'Status' not in data.columns or 'Type' not in data.columns:
    print("\n'Status' or 'Type' column not found in the data.")
    exit()

# Filtering data for a specific value in Column1
specific_value = "Open"
filtered_data = data[data['Status'] == specific_value]

# Group by 'Column2' and count occurrences
grouped_data = filtered_data.groupby('Type').size().reset_index(name='Count')

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Type'], grouped_data['Count'], color='skyblue')
plt.xlabel('Type')
plt.ylabel('Count of ' + specific_value)
plt.title(f'Count of {specific_value} Grouped by Type')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping labels/ title
plt.show()
