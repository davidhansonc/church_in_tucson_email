import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from OLD.weekly_update_template import subject, message_html, message_text
# from email_list import email_list

# Email configuration
sender_email = 'office@churchintucson.org'
sender_password = input('your password: ')
# receiver_email = 'office@churchintucson.org'
receiver_email = 'davidhanson.c@gmail.com'
subject = 'Church in Tucson Weekly Update'
html_message = message_html 

# Create a MIMEText object for the HTML content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the HTML message to the email with 'html' content type
msg.attach(MIMEText(html_message, 'html'))

# Establish a connection to the GoDaddy SMTP server
smtp_server = 'smtpout.secureserver.net'
smtp_port = 587  # SMTP port for GoDaddy

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)  # Log in to your email account

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    print('HTML Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')