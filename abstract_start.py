from abc import ABC, abstractmethod

class GraphicShape(ABC):

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius * self.radius)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return (self.side * self.side)

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())