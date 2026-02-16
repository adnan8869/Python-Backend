# import re

# test = "I have your number, which starts from 0302. I'm right now, right? Ok, I'm telling 03025998553 Tesal: (999)-333-7777 "

# pattern = r"\(\d{3}\)-\d{3}-\d{4}|\d{11}"

# matches = re.findall(pattern, test)
# print(matches)



import re

text = "Contact us at support@example.com or info@site.org"

all_emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(all_emails)








# result = re.findall("P..t", "Pinvgugt Peit Pit Pot")
# print(result)