
# Open Closed Principle 
# allow to add new features without changing the existing code
# eg. calculate the erea of a rectangle, circle, triangle, etc.

# two ways to add new features:
# 1. using abstract classes, and interfaces
# 2. making a new copy of the class, and adding new features

# it prevents the tisting process to old code

# Liskov substitution principle 
# is completion of the Open Closed Principle
# the child class should be able to replace the parent class without changing the code
# shape:Shape = Rectangle()
# the factory pattern is a good example of Liskov substitution principle


from zope.interface import implementer, Interface
from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def number_of_sides(self):
        pass 

    @abstractclassmethod
    def perimeter(self):
        pass

    @abstractclassmethod
    def color(self):
        pass

    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):

    NUMBER_OF_SIDES = 4
    DEFAULT_COLOR = "BLUE"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def number_of_sides(self):
        return self.NUMBER_OF_SIDES

    def perimeter(self):
        return 2 * (self.width + self.height)

    def color(self):
        return self.DEFAULT_COLOR

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} and height {self.height}")


class Circle(Shape):

    PI = 3.14159
    NUMBER_OF_SIDES = 0
    DEFAULT_COLOR = "RED"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.PI 

    def number_of_sides(self):
        return Circle.NUMBER_OF_SIDES

    def perimeter(self):
        return Circle.PI * self.radius * 2

    def color(self):
        return self.DEFAULT_COLOR

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Triangle(Shape):
    
        NUMBER_OF_SIDES = 3
        DEFAULT_COLOR = "GREEN"
    
        def __init__(self, base, height):
            self.base = base
            self.height = height
    
        def area(self):
            return self.base * self.height / 2
    
        def number_of_sides(self):
            return self.NUMBER_OF_SIDES
    
        def perimeter(self):
            return (self.base + self.height) * 2

        def color(self):
            return self.DEFAULT_COLOR

        def draw(self):
            print(f"Drawing a triangle with base {self.base} and height {self.height}")


class Square(Rectangle):
    
    DEFAULT_COLOR = "YELLOW"

    def __init__(self, side):
        super().__init__(side, side)

    def color(self):
        # override the color method and change in depeding on the O/C principle
        return self.DEFAULT_COLOR



class Cube(Shape):

    DEFAULT_COLOR = "BLACK"

    def __init__(self, side):
        self.side = side

    def color(self):
        return self.DEFAULT_COLOR

    def volume(self):
        return self.side^3

class Factory:
    # follows liskov substitution principle
    @staticmethod# cannot call instance or class methods and attributes
    def create_shape(shape_type:Shape, **kwargs) -> Shape:
        if shape_type == "rectangle":
            return Rectangle(**kwargs)
        elif shape_type == "circle":
            return Circle(**kwargs)
        elif shape_type == "triangle":
            return Triangle(**kwargs)
        elif shape_type == "square":
            return Square(**kwargs)
        elif shape_type == "cube":
            return Cube(**kwargs)
        else:
            raise ValueError(f"{shape_type} is not a valid shape")


class Report(implementer(Interface)):
    @abstractclassmethod
    def generate(**information):
        pass

class StudentRegistrationReport(Report):
    def generate(**information):
        return "Student Registration Report, {}".format(information)

class StudentAttendanceReport(Report):
    def generate(**information):
        return "Student Attendance Report, {}".format(information)


if __name__ == "__main__":
    
    # following the Liskov substitution principle
    shape:Shape = Factory.create_shape("rectangle", width=10, height=20)
    print(shape.area())
    print(shape.number_of_sides())
    print(shape.perimeter())
    print(shape.color())
    shape.draw()

    rectangle: Rectangle = Square(10)
    print(rectangle.area())
    print(rectangle.number_of_sides())
    print(rectangle.perimeter())
    print(rectangle.color())
    rectangle.draw()

    