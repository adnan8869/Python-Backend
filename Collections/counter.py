from collections import Counter


str = Counter('gallahad')
print(str)

lst = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(lst)
print(lst.most_common(2))   # first two most common elements

dict = Counter({'a': 3, 'b': 2, 'c': 1})
print(dict)

c = Counter(a=3, b=2, c=1)
print(c)
# print(list(c.elements()))


f = Counter(a=4, b=2, c=0, d=-2)
d= Counter(a=1, b=2, c=3, d=4)
f.subtract(d)
print(f)
f.update(d)
print(f)
print(f+d)
print(f-d)
print(f & d)   # intersection
print(f | d)   # union