import pandas as pd
import matplotlib.pyplot as plt

# Read the data from a CSV file
data = pd.read_csv('Construction_Data_PM_Forms_All_Projects.csv')

# Ensure that the 'Date' column is a datetime type
data['Created'] = pd.to_datetime(data['Created'])

# Filter the data for rows where 'Status' is 'Opened' 
filtered_data = data[(data['Status'] == 'Opened') ]

# Group by 'Date' and count the occurrences
grouped_data = filtered_data.groupby('Created').size().reset_index(name='Count')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['Created'], grouped_data['Count'], marker='o', linestyle='-', color='skyblue')
plt.xlabel('Date')
plt.ylabel('Count of A')
plt.title('Time Series Plot of Active Category A Over Time')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
