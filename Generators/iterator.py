# Iterator is an object which implements the iterator protocol, which consists of the methods __iter__() and __next__().
# nums = [2,3,4,56,78,90]
# it = iter(nums)
# print(next(it)) # 2
# print(next(it)) # 3
# print(it.__next__()) # 4
# print(it.__next__()) # 56






# Custom Iterator:
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
values = TopTen()
# for i in values:
#     print(i)

# We can also use next() to get values one by one:
print(next(values)) # 1
print(next(values)) # 2 
print(next(values)) # 3
print(next(values)) # 4
print(next(values)) # 5
print(next(values)) # 6
print(next(values)) # 7
print(next(values)) # 8
print(next(values)) # 9
print(next(values)) # 10
print(next(values)) # StopIteration raised here