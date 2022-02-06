# dataclasses

class Vector: 
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getLength(self):
        return (self.x**2 + self.y*2)**(1/2)

    def __str__(self):
        return f"Class Vector(x={self.x}, y={self.y})"
    
    #__repr__()
    
vector = Vector(3,5)
print(f"Output fucnction to str: {vector}")
print(f"analog to str: {str(vector)}")
print(vector.getLength())



from dataclasses import dataclass

@dataclass
class Wector:
    x: float
    y: float
    z: float
    
    @property
    def getLength(self):
        return (self.x**2 + self.y**2)**(1/2)


wector = Wector(3,5,4)
print(f"Output fucnction to str: {wector}")
print(f"analog to str: {str(wector)}")
#print(wector.getLength())


# End