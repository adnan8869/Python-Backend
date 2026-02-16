# A Generator is a special type of function in Python that allows you to return
# a stream of values one at a time, instead of returning them all at once
# yield: Pauses the function, saves all its local variables (state), and sends a value back. 
# When the generator is called again, it resumes exactly where it left off




# Simple function:
def get_numbers(n):
    result = []
    for i in range(n):
        result.append(i)
    return result # Returns the entire list at once

print(get_numbers(3)) # [0, 1, 2]


# Generator function:
def gen_numbers(n):
    for i in range(n):
        yield i # Returns one number and "pauses"

g = gen_numbers(3)
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2




# GENEARTOR EXPRESSION
# It uses parentheses instead of square brackets and is more memory efficient than a list comprehension
#  because it generates items one at a time.

my_gen = (x**2 for x in range(1000000))

print(next(my_gen)) # 0
print(next(my_gen)) # 1
print(next(my_gen)) # 4
print(next(my_gen)) # 9