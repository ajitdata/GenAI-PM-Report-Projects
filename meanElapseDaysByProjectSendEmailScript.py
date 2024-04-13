import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import datetime

def send_email(subject, body):
    sender_email = "xxxxxx@gmail.com"
    receiver_email = "xxxxxx@gmail.com"
    password = "xxxxxxxxxxxxxxx"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Your data processing code
file_path = 'Construction_Data_PM_Forms_All_Projects.csv'
data = pd.read_csv(file_path)
data['Created'] = pd.to_datetime(data['Created'])
current_datetime = datetime.datetime.now()
data['Elapsed Days'] = (current_datetime - data['Created']).dt.days
mean_elapsed_per_category = data.groupby('Project')['Elapsed Days'].mean().reset_index()
table = mean_elapsed_per_category.to_html(classes="table table-striped table-bordered")

# Send the email
subject = "Mean Elapsed Time by Project"
send_email(subject, table)

print("Email sent successfully!")
