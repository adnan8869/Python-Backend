# Frequency Counter
# Given a list, count the frequency of each character.

# count= {}
# def frequency_counter(lst):
#     for ele in lst:
#         count[ele] = count.get(ele, 0) + 1
#     return count
# list = ['adnan','ali','ahmad','adnan','arsal','arsal','alyan']
# print(frequency_counter(list))





# Find Missing Number

# A list contains numbers from 1 to n with one missing number.
# Find the missing number.
# def find_missing_number(lst, n):
#     total_sum = n * (n + 1) // 2   # arithmetic series. For n=8, this gives: 8 × 9 ÷ 2 = 36
#     actual_sum = sum(lst)          #List sum is 36
#     return total_sum - actual_sum
# numbers = [1, 2, 4, 6, 3, 7, 8]
# n = 8
# print(find_missing_number(numbers, n))  




# Pattern Printing
# def Pattern(n):
#     for i in range(n+1):
#         print(i* "*")
# Pattern(5)



# First Non-Repeating Character
# Given a string, find the first character that does not repeat.
# def first_non_repeating_character(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     for char in s:
#         if char_count[char] == 1:
#                 return char
#     return None

# string = "aabbccdeff"
# print(first_non_repeating_character(string))



# Rotate List
# Rotate a list to the right by k steps.
# def rotate_list(lst, k):
#     k = k % len(lst)  # Handle cases where k is greater than the list length
#     return lst[-k:] + lst[:-k]    
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# print(rotate_list(numbers, k))



# Merge 3 lists iterations into a single list without mismatch 
# name = ["adnan", "ali", "ayesha", "arsal","usman"]
# age = [20, 21, 19, 22]
# gender = ["Male", "Male", "Female"]
# merged_list = list(zip(name, age, gender))
# for name,age,gender in merged_list:
#     print(f"Name: {name}, Age: {age}, Gender: {gender}")






# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# # set_a is subset of set_b ?
# print(set_a.issubset(set_b))  # False


# fromkeys()
# keys = ['a', 'b', 'c']
# new_dict = dict.fromkeys(keys, 0) 
# print(new_dict) 



# class Robot:
#     pass

# r = Robot()
# setattr(r, "battery_level", 100)
# print(getattr(r, "battery_level") ) # 100
# print(hasattr(r, "battery_level"))  # True



# my_list = [0, 1, 2, 3, 4, 5]
# last_three = slice(1, 4) # A reusable slice object
# print(my_list[last_three]) # [1, 2, 3]



# users = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 20}]
# # Sort by age
# sorted_users = sorted(users, key=lambda u: u["age"])
# print(sorted_users)  



# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

# my_dog = Dog("Rex", "Collie")
# print(vars(my_dog))
# vars(object) returns the values of all attributes of the object as a dictionary.



# names = ["Alice", "Bob"]
# scores = [85, 92]
# # Zipping
# combined = list(zip(names, scores))
# print(combined) 
# # Unzipping
# names , scores = zip(*combined)
# print(names)   # ('Alice', 'Bob')
# print(scores)  # (85, 92) 


# # for name, score in combined:
# for name, score in zip(names, scores):
#     print(f"{name} got {score} scores.")



# keys = ['name', 'age', 'city']
# values = ['Alice', 30, 'New York']
# # Zipping keys and values into a dictionary
# my_dict = dict(zip(keys, values))
# print(my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# #Unzipping dictionary into keys and values
# unzipped_keys, unzipped_values = zip(*my_dict.items())
# print(unzipped_keys)   # ('name', 'age', 'city')
# print(unzipped_values) # ('Alice', 30, 'New York')




