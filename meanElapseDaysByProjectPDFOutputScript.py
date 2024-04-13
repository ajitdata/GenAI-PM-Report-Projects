import pandas as pd
import datetime
import matplotlib.pyplot as plt
from fpdf import FPDF

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

# Step 1: Visualize the DataFrame
plt.figure(figsize=(10, 6))
plt.bar(mean_elapsed_per_category['Project'], mean_elapsed_per_category['Elapsed Days'])
plt.xlabel('Project')
plt.ylabel('Mean Elapsed Days')
plt.title('Mean Elapsed Days per Project')
plt.tight_layout()

# Step 2: Save the visualization as an image
image_path = 'output_image.png'
plt.savefig(image_path)

plt.show()

# Step 3: Convert the image to PDF
pdf = FPDF()
pdf.add_page()
pdf.image(image_path, x = 10, y = 20, w = 190)
pdf_output_path = 'output_report.pdf'
pdf.output(pdf_output_path)

print(f"Report saved to {pdf_output_path}")