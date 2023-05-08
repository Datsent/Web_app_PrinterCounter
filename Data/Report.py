from Data.Utils.utils import *
from Data import Data_Base
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
from datetime import date

def send_err_mail(ip_print, n_print):
    # Email details
    sender_email = SMTP_USER
    receiver_email = ADMIN_MAIL
    subject = 'No connection to Printer'
    body = ip_print + ' ' + n_print + ' No connection or can`t read data'

    # Office 365 SMTP settings
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = SMTP_USER
    smtp_password = SMTP_PASS

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Create a SMTP session
    smtp_session = smtplib.SMTP(smtp_server, smtp_port)
    smtp_session.starttls()
    smtp_session.login(smtp_username, smtp_password)

    # Send the email
    smtp_session.sendmail(sender_email, receiver_email, message.as_string())

    # Close the SMTP session
    smtp_session.quit()

def send_mail():
    # Email details
    sender_email = SMTP_USER
    receiver_email = RECEIVER_MAIL
    subject = 'UNI Printer Count'
    body = "Printers Count File"

    # Office 365 SMTP settings
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    smtp_username = SMTP_USER
    smtp_password = SMTP_PASS

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['CC'] = ADMIN_MAIL
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Add attachment to email
    with open(Data_Base.export_to_csv('Printers'), 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=f"Printers_{str(date.today())}.csv")
        part['Content-Disposition'] = f'attachment; filename=f"Printers_{str(date.today())}.csv"'
        message.attach(part)

    # Create a SMTP session
    smtp_session = smtplib.SMTP(smtp_server, smtp_port)
    smtp_session.starttls()
    smtp_session.login(smtp_username, smtp_password)

    # Send the email
    smtp_session.sendmail(sender_email, [receiver_email, ADMIN_MAIL], message.as_string())

    # Close the SMTP session
    smtp_session.quit()

if __name__ == '__main__':
    send_mail()