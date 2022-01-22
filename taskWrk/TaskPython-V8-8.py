# *** OOP

# Множественное наследование 

# super(), mro()

class Pos:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        print('pos')
        
    def show_pos(self):
        print(f'{self.x} {self.y}') 

class Style:
    
    def __init__(self, width):
        self.width = width

    def draw(self):
        print('style')
        
    def show_width(self):
        print(f'width {self.width}') 
        
    
class Line(Pos, Style):
    #pass
    
    def __init__(self, x, y, width):
        #super(Pos, self).__init__(x, y)
        #super(Style, self).__init__(width)
        Pos.__init__(self, x, y)
        Style.__init__(self, width)
    
    def draw(self):
        print(f'Draw line on pop {self.x}, {self.y} with width {self.width}')
    
    def show(self):
        # supper()
        super().show_pos()
        super().show_width()
        
        # Насделование
        #self.show_pos()
        #self.show_width()


# Функция mro(), возвращает список, в каком порядке будут искаться методы
#print(Line.mro())

line = Line(1, 5, 4)


line.draw()
line.show()


# End