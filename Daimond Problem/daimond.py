class A:
    def display(self):
        print("Hello from class A")
              
class B(A):
    def display(self):
        print("Hello from class B")

class C(A):
    def display(self):
        print("Hello from class C")


class D(B, C):
    pass

d = D()
d.display()  # First look for display in D, then B, then C, and finally A. So it will print "Hello from class B"
print(D.__mro__)
print(D.mro())