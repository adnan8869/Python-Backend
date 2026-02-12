# Defaultdict: It automatically assigns a default value to keys that do not exist.

# | Type | Use             |
# | ---- | --------------- |
# | int  | counting        |
# | list | grouping        |
# | set  | unique grouping |



from collections import defaultdict


# COUNTING
d = defaultdict(int)

a = [1,2,3,4,2,4,1,2]
for i in a:
    d[i] += 1
print(d)

# GROUPING
d = defaultdict(list)

words = ["cat", "dog", "cow", "duck"]

for w in words:
    d[w[0]].append(w)

print(d)

# UNIQUE GROUPING
d = defaultdict(set)
for w in words:
    d[w[0]].add(w)

print(d)
