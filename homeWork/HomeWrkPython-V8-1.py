# Задание 1:  Реализовать следуюшие классы и продемострировать их работоспособность: area & perimeter должны быть акссесорами (@property).


# Объявляем Class Point:
class Point:
    
    x = 4
    y = 16
    
    def __init__(self, point_x = x, point_y = y):
        if point_x is None or point_x == '':
            self.point_x = self.x
        else:
            self.point_x = point_x
            
        if point_y is None or point_y == '':
            self.point_y = self.y
        else:
            self.point_y = point_y
            
    def getpoint(self):
        print(f'Значения: x={float(self.point_x)}, y={float(self.point_y)}')
        
        return float(self.point_x), float(self.point_y)


# Объявляем Class Line и агрегируем с классом Point:
class Line:
    
    def __init__(self, point_start :float =None, point_end :float =None):
        if point_start is None or point_start == '':
            self.point_start = Point().x
        else:
            self.point_start = point_start
            
        if point_end is None or point_end == '':
            self.point_end = Point().y
        else:
            self.point_end = point_end
        
    def getlenght(self):
        
        return float(self.point_start + self.point_end)
        

#Объявляем Class Share
class Share:
    
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def getarea(self):
        return float(self.side_a * self.side_b)

    def getperimeter(self):
        return float((self.side_a + self.side_b)*2)

# Объявляем Class Rect и наследуем от Класса Share
class Rect(Share):
    
    def setRect(self):
        side = Line().getlenght()
        #print(f'{side}')
        self.side_a = Line().getlenght()
        self.side_b = Line().getlenght()
        return side
    
    def show(self):
        area = super().getarea()
        perimeter = super().getperimeter()
        return f'Площадь={area}, Периметр={perimeter}'

point = Point(10,None)
#print(point.getpoint())


line = Line()
#print(line.getlenght())


#share = Share(9,16)
#print(share.getarea())
#print(share.getperimeter())

rect = Rect(3,4)
#rect.setRect()
#print(rect.setRect())
print(rect.show())

#cube = Cube(3,4,5)
#print(cube.getvolume())

        
#square = Square(3,None,5)
#print(square.getarea())
#print(square.getperimeter())


#rect = Rect()
#print(rect.getarea())
#print(rect.getperimeter())