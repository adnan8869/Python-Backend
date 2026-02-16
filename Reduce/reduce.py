from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = reduce(add, numbers)
# Step-by-step:
# 1. add(1, 2) -> 3
# 2. add(3, 3) -> 6
# 3. add(6, 4) -> 10
print(result) # 10

# The initial value is 100, so the reduction starts with 100 and then adds each element of the list to it.
# result = reduce(add, numbers,100)





# numbers = [45, 2, 89, 12, 101]
# max_num = reduce(lambda a, b: a if a > b else b, numbers)
# print(max_num) # 101



# import operator
# result = reduce(operator.mul, [1, 2, 3, 4]) 
# print(result) # 24