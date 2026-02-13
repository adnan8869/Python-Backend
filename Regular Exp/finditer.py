
import re

text = "I like Python and Python"

for match in re.finditer("Python", text):
    print(match.start(), match.end(), match.group())
