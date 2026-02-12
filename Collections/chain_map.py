from collections import ChainMap

d1 = {"a": 1}
d2 = {"b": 2}

cm = ChainMap(d1, d2)

print(cm)
# Return the dictionaries in tuple form





# d3 = {"c": 3}
# d4 = d3.update({"d": 4})
# print(d3)