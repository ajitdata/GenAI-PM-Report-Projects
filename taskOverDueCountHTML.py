import pandas as pd

# Load the CSV file
file_path = 'Construction_Data_PM_Tasks_All_Projects.csv'

# Create a placeholder for the HTML content
html_content = ""

# Read the data
try:
    data = pd.read_csv(file_path)
    html_content += "<p>Data loaded successfully!</p>"
except FileNotFoundError:
    html_content += f"<p>File not found: {file_path}</p>"
    # Save the error message to an HTML file
    with open("output.html", "w") as f:
        f.write(html_content)
    exit()

# Append basic information about the data to HTML content
html_content += "<h2>First 5 rows of the original data:</h2>"
html_content += data.head().to_html()
html_content += "<h2>Column names in the original data:</h2>"
html_content += "<p>" + ', '.join(data.columns) + "</p>"

# Check for NaN/NULL values in the column
nan_count = data['OverDue'].isna().sum()
html_content += f"<p>Number of NaN/NULL values in 'OverDue': {nan_count}</p>"

# Unique values in the column
html_content += "<h2>Unique values in 'OverDue':</h2>"
html_content += "<p>" + ', '.join(map(str, data['OverDue'].unique())) + "</p>"

# Define the filtering criteria
desired_value = True

# Filter the data
filtered_data = data[data['OverDue'] == desired_value]

# Append the filtered data to HTML content
html_content += "<h2>Filtered data:</h2>"
html_content += filtered_data.head().to_html()

# Append the count of filtered rows to HTML content
html_content += f"<h2>Count of filtered rows: {len(filtered_data)}</h2>"

# Save the content to an HTML file
with open("output.html", "w") as f:
    f.write(html_content)
