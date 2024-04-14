import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# SMTP settings
smtp_host = config['SMTP']['host']
smtp_port = int(config['SMTP']['port'])
smtp_email = config['SMTP']['email']
smtp_password = config['SMTP']['password']

# Email settings
email_subject = config['EMAIL']['subject']
html_file_path = config['EMAIL']['html_file']
to_emails = config['RECIPIENTS']['emails'].split(',')  # Split the string into a list of emails

# Create the SMTP session
smtp = smtplib.SMTP(smtp_host, smtp_port)
smtp.starttls()
smtp.login(smtp_email, smtp_password)

# Read HTML content from the configured file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Create MIME structure
message = MIMEMultipart('alternative')
message['From'] = smtp_email
message['Subject'] = email_subject

# Attach the HTML content
message.attach(MIMEText(html_content, 'html'))

# Send the email to each recipient
for to_email in to_emails:
    message['To'] = to_email
    smtp.sendmail(smtp_email, to_email, message.as_string())

# Close the SMTP session
smtp.quit()