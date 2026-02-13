# Check only at beggining of the string


import re

text = "Python is great"

result = re.match("Python", text)   #  Match
print(result.group())

result = re.match("is", text)       #  No match
print(result)