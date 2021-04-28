from twilio.rest import Client
import smtplib
from email.message import EmailMessage
import datetime as dt
import requests


class NotificationManager:
    def __init__(self, msg_sid, msg_token,smtp_connection, smtp_email, email_password, ):
        self.sid = msg_sid
        self.token = msg_token
        self.smtp_connection = smtp_connection
        self.email = smtp_email
        self.password = email_password

    def send_msg(self, from_num, to_num, msg):
        client = Client(self.sid, self.token)
        message = client.messages \
            .create(
            body=msg,
            from_=from_num,  # TWILIO NUMBER
            to=to_num  # VERIFIED NUMBER
        )
        return message.sid

    def get_email_list(self, endpoint, header):
        users_response = requests.get(url=endpoint, headers= header)
        users_response.raise_for_status()
        email_list = []
        response = users_response.json()
        for user in response['users']:
            email_list.append(user['email'])
        return email_list

    def send_emails(self, emails_list, content):
        msg = EmailMessage()
        current_date = dt.datetime.now().strftime('%m/%d/%Y')
        msg['Subject'] = f"Flight Deals for {current_date}!"
        msg.set_content(content)
        msg['From'] = self.email
        msg['Bcc'] = ','.join(emails_list)
        with smtplib.SMTP(self.smtp_connection) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.send_message(msg)

