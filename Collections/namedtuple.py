from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "cgpa"])

s = Student("Adnan", 22, 3.9)

print(s.name)
print(s.cgpa)








