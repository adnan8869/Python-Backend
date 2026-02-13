# Used for repalcing text in a string

import re

text = "I love Java"

new = re.sub("Java", "Python", text)

print(new)
