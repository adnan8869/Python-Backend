# Finds pattern anywhere in string.
import re

text = "I love Python programming"

result = re.search("Python", text)

print(result)
print(result.group())