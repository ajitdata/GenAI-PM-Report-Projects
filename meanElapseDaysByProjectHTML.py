from flask import Flask, render_template_string
import pandas as pd
import datetime

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    # Load the CSV file
    file_path = 'Construction_Data_PM_Forms_All_Projects.csv'

    # Read the data
    try:
        data = pd.read_csv(file_path)
        message = "Data loaded successfully!"
    except FileNotFoundError:
        return f"File not found: {file_path}"

    # Ensure columns are available in the data
    if 'Created' not in data.columns or 'Project' not in data.columns:
        return "\n'Created' or 'Project' column not found in the data."

    # Convert 'Created' column to datetime format
    data['Created'] = pd.to_datetime(data['Created'])

    # Get today's date
    current_datetime = datetime.datetime.now()

    data['Elapsed Days'] = (current_datetime - data['Created']).dt.days

    # Calculate mean elapsed time for each category
    mean_elapsed_per_category = data.groupby('Project')['Elapsed Days'].mean().reset_index()

    # Convert the dataframe to HTML format
    table = mean_elapsed_per_category.to_html(classes="table table-striped table-bordered")

    # HTML template
    template_string = """
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h2>Mean Elapsed Time by Project</h2>
                {{ table|safe }}
            </div>
        </body>
    </html>
    """
    
    return render_template_string(template_string, table=table)

if __name__ == '__main__':
    app.run(debug=True)
