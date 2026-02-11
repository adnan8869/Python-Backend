# @property = Decorator used to define a method as a property (It can be accessed like an attribute but it is actually a method)
# Benefit: Add additional functionality when read, write, or delete an attribute.
# Gives you Getter, Setter and Deleter method.


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be non-negative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter  
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(10, 5)
rectangle.width = 15
rectangle.height = 20
print(rectangle._width)  
print(rectangle._height)  