# Email Verification
import re
email = "test8890@gmail.com"

pattern = r"^[\w\d\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")



text = "Call me at 0302-1234567"

pattern = r"\d{4}-\d{7}"

print(re.findall(pattern, text))
