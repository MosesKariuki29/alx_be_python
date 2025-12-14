import math


class Shape:
    def area(self):
        """
        Base method to be overridden
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Rectangle shape
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Area of rectangle
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Circle shape
        """
        self.radius = radius

    def area(self):
        """
        Area of circle
        """
        return math.pi * (self.radius ** 2)
