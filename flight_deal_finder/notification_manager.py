from twilio.rest import Client


class NotificationManager:
    def __init__(self, sid, token):
        self.sid = sid
        self.token = token

    def send_msg(self, from_num, to_num, msg):
        client = Client(self.sid, self.token)
        message = client.messages \
            .create(
            body=msg,
            from_=from_num,  # TWILIO NUMBER
            to=to_num  # VERIFIED NUMBER
        )
        return message.sid
