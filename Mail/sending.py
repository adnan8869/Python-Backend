import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables from .env file
load_dotenv()

message = Mail(
    from_email=os.getenv("FROM_EMAIL"),
    to_emails=os.getenv("TO_EMAIL"),
    subject="Sending with SendGrid is Fun",
    html_content="<strong>This is  a test email sent with SendGrid.</strong>",
)

sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
response = sg.send(message)
print(response.status_code, response.body)
