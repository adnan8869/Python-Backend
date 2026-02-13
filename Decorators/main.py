# def decorator(func):
#     def wrapper():
#         print("Before the Transcation")
#         func()
#         print("After the Transcation")

#     return wrapper


# @decorator
# def say_hello():
#     print("...Executing all the steps...")

# say_hello()



def add_sprinkle(func):
    def wrapper(*arg, **kwargs):
        print("Adding sprinkles to your ice cream")
        func(*arg, **kwargs)
    return wrapper

def add_chocolate(func):
    def wrapper(*arg, **kwargs):
        print("Adding chocolate to your ice cream")
        func(*arg, **kwargs)
    return wrapper

@add_chocolate      # First add chocolate syrup, then add sprinkles
@add_sprinkle
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("Vanilla")



