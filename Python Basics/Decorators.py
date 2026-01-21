# STATIC METHOD EXAMPLE (Can't use and change instances or class variables)
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(MathOperations.add(5, 3)) 
print(MathOperations.is_even(10))  
print(MathOperations.is_even(7))  







# CLASS METHOD EXAMPLE (Can access and modify class variables)
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return f"Total people: {cls.population}"
    
    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")


p1 = Person("John")
p2 = Person("Jane")
print(Person.get_population())  
p3 = Person.create_anonymous()
print(p3.name) 






# INSTANCE METHOD EXAMPLE (Can access and modify instance variables)

class MathOperations:
    def add(self, a, b):
        self.a = a
        self.b = b
        return a + b

    def is_even(self,number):
        self.number = number
        return number % 2 == 0


math_ops = MathOperations()
print(math_ops.add(5, 3)) 
print(math_ops.is_even(10)) 
print(math_ops.is_even(7)) 




# Property Decorator Example
class Student:
    def __init__(self,math,chem,phy):
        self._math = math
        self._chem = chem
        self._phy = phy

    @property
    def average(self):
        return str((self._math + self._chem + self._phy) / 3) + "%"
    

s1 = Student(90, 80, 70)
print(s1.average)
s1._math = 100
print(s1.average)