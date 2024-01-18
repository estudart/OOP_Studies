from abc import ABC

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    def calcArea(self):
        if isinstance(self, Circle):
            # print(self.radius)
            return 3.14 * (self.radius * self.radius)
        elif isinstance(self, Square):
            # print(self.side)
            return (self.side * self.side)


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side


g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())