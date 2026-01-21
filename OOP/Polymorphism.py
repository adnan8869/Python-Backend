# definition of overloading
# When the same oprator is allowed to have different meanings based on the context
# Example: + operator can be used to add two numbers or concatenate two strings
# 1+2=3
# "Hello " + "World" = "Hello World"
# [1,2] + [3,4] = [1,2,3,4]


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show(self):
        return f"{self.real} + {self.imag}i"

    # Overloading the + operator
    def __add__(self, other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
        return Complex(self.real, self.imag)
    def __sub__(self, other):
        self.real = self.real - other.real
        self.imag = self.imag - other.imag
        return Complex(self.real, self.imag)

print("Addition:")    
c1 = Complex(2, 3)
print(c1.show())
c2 = Complex(4, 5)
print(c2.show())
c3 = c1 + c2  
print(c3.show())  



print("Subtraction:")
print(c2.show())
print(c1.show())
c4 = c2 - c1
print(c4.show())
 