from abc import ABC, abstractmethod

class GraphicShape(ABC):

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius * self.radius)
    
    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return (self.side * self.side)
    
    def toJSON(self):
        return f"{{'Square': {str(self.calcArea())}}}"

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
print(s.toJSON())
print(c.toJSON())