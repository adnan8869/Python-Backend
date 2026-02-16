# It takes the function you provide and "maps" it onto each element of the data. 
# It returns a map object, which is an iterator. To see the results as a list, you usually wrap it in list().

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]

# Apply the square function to every number
result = map(square, numbers)

print(list(result)) # [1, 4, 9, 16, 25]


# Lanbda function 
# numbers = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled) # [2, 4, 6, 8]





# Mapping Multiple Iterables(It will stop as soon as the shortest list is exhausted)
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # Add elements from two lists together
# sums = list(map(lambda x, y: x + y, list1, list2))
# print(sums) # [11, 22, 33]





# str_nums = ["1", "2", "3"]
# ints = list(map(int, str_nums)) 
# print(ints) # [1, 2, 3]





