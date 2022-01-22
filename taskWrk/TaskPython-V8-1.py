# *** OOP

# Наследование

class Horse:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def run(self):
        print(f'{self.name} running')


class Pegasus(Horse):
    
    def __init__(self, color, name, length_of_wings):
        Horse.__init__(self, color, name)
        self.length_of_wings = length_of_wings
    
    def fly(self):
        print(f'{self.name} flying')


pegasus = Pegasus('white', 'Pegas', '4m')
pegasus.fly()
pegasus.run() # Наследуем
print('Имя лошади', pegasus.name, ', цвет', pegasus.color, 'размер крыла', pegasus.length_of_wings)

kon = Horse('Black', 'Kon')
kon.run()
print('Имя лошади', kon.name, ', цвет', kon.color)

# End