# A Closure is a function object that "remembers" values in the enclosing (parent) scope even if they are no longer in memory.
def outer(num):
    def inner(x):
        return num + x
    return inner



closure_func1 = outer(10)
closure_func2 = outer(20)
print(closure_func1(5))
print(closure_func2(15))