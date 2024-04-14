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

# Read HTML content from the configured file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Prepare list of recipients
recipient_details = config['RECIPIENTS']
to_emails = [email for name, email in recipient_details.items()]  # List of all recipient emails

# Establish SMTP connection
try:
    smtp = smtplib.SMTP(smtp_host, smtp_port)
    smtp.starttls()
    smtp.login(smtp_email, smtp_password)
    
    # Create and send the email to all recipients
    message = MIMEMultipart('alternative')
    message['From'] = smtp_email
    message['Subject'] = email_subject
    message['To'] = ", ".join(to_emails)
    message.attach(MIMEText(html_content, 'html'))
    smtp.sendmail(smtp_email, to_emails, message.as_string())
    
except smtplib.SMTPDataError as e:
    print(f"Failed to send email: {e}")
except smtplib.SMTPServerDisconnected as e:
    print(f"Server disconnected unexpectedly: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    try:
        smtp.quit()
    except Exception as e:
        print(f"Error closing the connection: {e}")