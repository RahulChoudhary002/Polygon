import math

# Base class
class Polygon:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Rectangle
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

# Square
class Square(Polygon):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Parallelogram
class Parallelogram(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height

# Function to calculate area
def calculate_area(polygon):
    print(f"The area of the {polygon.__class__.__name__} is: {polygon.area():.2f}")

# Sample usage
if __name__ == "__main__":
    t = Triangle(10, 5)
    r = Rectangle(10, 4)
    s = Square(6)
    c = Circle(7)
    p = Parallelogram(12, 6)

    for shape in [t, r, s, c, p]:
        calculate_area(shape)
