import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, length, breadth):
        if length < 0 or breadth < 0:
            raise ValueError("Length and breadth cannot be negative")
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

def main():
    try:
        circle = Circle(5)
        rectangle = Rectangle(4, 6)
        
        print(f"Circle area: {circle.area():.2f}")
        print(f"Rectangle area: {rectangle.area():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()