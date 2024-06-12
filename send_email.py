import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email_sender, email_to, email_subject, email_body, smtp_user, smtp_password):
    """
    Send an email using SMTP.

    Args:
        email_sender (str): The sender's email address.
        email_to (str): The recipient's email address.
        email_subject (str): The subject of the email.
        email_body (str): The body of the email.
        smtp_user (str): The SMTP user (sender's email address).
        smtp_password (str): The SMTP password.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create email
    message = MIMEMultipart()
    message['From'] = email_sender
    message['To'] = email_to
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'plain'))

    try:
        # Connect to SMTP server and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(email_sender, email_to, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        return False

if __name__ == "__main__":
    # Load sensitive data from environment variables
    email_sender = os.environ.get('EMAIL_SENDER')
    email_to = os.environ.get('EMAIL_TO')
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    email_subject = "Sample subject"
    # Add email body
    email_body = """
    Dear recipient,

    This is a sample email sent via Python's smtplib module.

    Here are some key points:
    - Python's smtplib module is used for sending emails.
    - This email is sent programmatically.
    - It includes a structured email body.

    You can find more information at: 
    - [GitHub Repository](https://github.com/saikiran9392/Python-Automation.git)

    Feel free to customize this code for your own use!

    Best regards,
    Your Name
    """

    # Send email
    if email_sender and email_to and smtp_user and smtp_password:
        if send_email(email_sender, email_to, email_subject, email_body, smtp_user, smtp_password):
            print("Email sent successfully!")
        else:
            print("Failed to send email. Please check the configuration.")
    else:
        print("Missing required environment variables. Please check the configuration.")
