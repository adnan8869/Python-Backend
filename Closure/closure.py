# A Closure is a function object that "remembers" values in the enclosing (parent) scope even if they are no longer in memory.
# def outer(num):
#     def inner(x):
#         return num + x
#     return inner



# closure_func1 = outer(10)
# closure_func2 = outer(20)
# print(closure_func1(5))
# print(closure_func2(15))






# We can read the variables from the outer function, but we cannot modify them directly. 
# To modify the variables, we need to use the 'nonlocal' keyword.
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter()) # 1
print(counter()) # 2