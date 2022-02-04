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
        print('Lenght:')
        return float(self.point_start + self.point_end)
    
    def setlenght(self, point_new_start, point_new_end):
        if point_new_start is None:
            self.point_start = Point().y
        else:
            self.point_start = point_new_start
        if point_new_end is None:
            self.point_end = Point().y
        else:
            self.point_end = point_new_end
        #print('Lenght:')
        return float(point_new_start + point_new_end)


#Объявляем Class Share
class Share:
    
    a = 9
    b = 16
    c = 25
    
    def __init__(self, side_a = a, side_b = b):
        if side_a is None or side_a == '':
            self.side_a = self.a
        else:
            self.side_a = side_a
        
        if side_b is None or side_b == '':
            self.side_b = self.b
        else:
            self.side_b = side_b
    
    def getarea(self):
        #print('Area:')
        return float(self.side_a * self.side_b)

    def getperimeter(self):
        #print('Perimeter:')
        return float((self.side_a + self.side_b)*2)

# Объявляем Class Rect и наследуем от Класса Share
class Rect(Share):
    
    def show(self):
        area = super().getarea()
        perimeter = super().getperimeter()
        return f'"Площадь rect"={area}, "Периметр rect"={perimeter}'

    def setRect(self, point_a1, point_b1, point_a2, point_b2):
        self.side_a = Line().setlenght(point_a1, point_a2)
        self.side_b = Line().setlenght(point_b1, point_b2)
        return f'side_a={self.side_a}, side_b={self.side_b}'


# Объявляем Class Square и наследуем от Классов Share, Line 
class Square(Share, Line):
    
    def show(self):
        area = super().getarea()
        perimeter = super().getperimeter()
        return f'"Площадь square"={area}, "Периметр square"={perimeter}'

    def setSquare(self, point_a1, point_b1, point_a2, point_b2):
        
        self.side_a = super().setlenght(point_a1, point_a2)
        self.side_b = super().setlenght(point_b1, point_b2)
        return f'side_a={self.side_a}, side_b={self.side_b}'


# Объявляем Class Square и наследуем от Классов Share
class Cube(Square):
    
    def setCube(self, point_c1, point_c2):
        self.side_c = super().setlenght(point_c1, point_c2)
        rez = self.side_a * self.side_b * self.side_c
        return f'"Объем cube"={rez}'
    
#point = Point()
#print(Point.mro())
#print(point.getpoint())

#line = Line()
#print(Line.mro())
#print(line.getlenght())
#print(line.setlenght(16,25))
#print(line.getlenght())

#share = Share()
#print(Share.mro())
#print(share.getarea())
#print(share.getperimeter())

#rect = Rect(11,12)
#print(Rect.mro())
#print(rect.show())
#print(rect.setRect(3,5,3,5))
#print(rect.show())

#square = Square()
#print(Square.mro())
#print(square.show())
#print(square.setSquare(7,9,7,9))
#print(square.show())

cube = Cube(3, 5)
print(Cube.mro())
print(cube.setCube(2,2))