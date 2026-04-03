import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From, To, ReplyTo, Content

load_dotenv()

message = Mail()

message.from_email = From(os.getenv("FROM_EMAIL"), "Adnan")

message.to = To(os.getenv("TO_EMAIL"))

message.reply_to = ReplyTo(os.getenv("FROM_EMAIL"), "Adnan")

message.subject = "Test Email - Python SendGrid Integration"

plain_text = """Hello,

This is a test email sent using SendGrid API with Python.

This email includes both plain text and HTML versions for better deliverability.

Best regards,
Adnan"""

message.content = [
    Content("text/plain", plain_text),
]

try:
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(f"Email sent successfully!")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.body}")
    print(f"Response Headers: {response.headers}")
except Exception as e:
    print(f"Error sending email: {str(e)}")
