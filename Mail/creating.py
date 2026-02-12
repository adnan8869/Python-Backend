from email.message import EmailMessage

msg = EmailMessage()

msg["From"] = "sender@gmail.com"
msg["To"] = "receiver@gmail.com"
msg["Subject"] = "Test Email"

msg.set_content("Hello! This is my first email.")

print(msg)
