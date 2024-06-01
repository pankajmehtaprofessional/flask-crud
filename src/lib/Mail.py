import dataclasses
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@dataclasses.dataclass
class Mail:

    # Connect to the SMTP server (in this case, Gmail)
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    def send(self, params):
        try:

            # Create a MIMEText object for the email content
            msg = MIMEMultipart()
            msg['From'] = params["sender_email"]
            msg['To'] = params["receiver_email"]
            msg['Subject'] = params["subject"]
            msg.attach(MIMEText(params["message"], 'html')) #html, plain

            server = SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            
            # Send the email
            server.sendmail(params["sender_email"], params["receiver_email"], msg.as_string())

            print("Email sent successfully...")
            return 1
        except KeyError as e:
            print(f"Key error : {str(e)}")
            raise
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise
        finally:
            print("success")
