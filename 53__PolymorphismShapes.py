class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses must implement draw()")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a circle with radius {self.radius}"
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def draw(self):
        return f"Drawing a rectangle with  {self.length}x{self.breadth}"
    
class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        return f"Drawing a Triangle with  side {self.side}"

def render_shapes(shapes):
    for shape in shapes:
        try:
            print(shape.draw())
        except Exception as e:
            print(f"Effor drawing shape: {e}")


def main():
    shapes = [
        Circle(5),
        Rectangle(12, 5),
        Triangle(6)
    ]

    render_shapes(shapes)


if __name__ == "__main__":
    main()
    

    
    

        