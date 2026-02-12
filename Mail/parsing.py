from email import policy
from email.parser import BytesParser

with open("mail.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

print(msg["From"])
print(msg["Subject"])
print(msg.get_body().get_content())
