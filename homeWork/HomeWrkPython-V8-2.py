# Задание 2: Композиция, Наследование и Агрегирование:

# *** Композиция

# Объявляем A Class
class Aclass:
    
    str_a = 'A-Class'
    
    def getAClass(self):
        return f'{self.str_a}'
    

# Объявляем B Class
class Bclass:
    
    str_b = 'B-Class'
    
    def getAClass(self):
        return f'{self.str_b}'
    
    def getClassAB(self):
        rez_b = self.str_b
        rez_a = Aclass.str_a
    
        return f'{rez_b} агрегирутет с {rez_a}'
    

aclass = Aclass()
#print(aclass.getAClass())

bclass = Bclass()
#print(bclass.getAClass())

print(f'Композиция: {bclass.getClassAB()}')


# *** Наследование

# Объявляем D Class
class Dclass:
    
    str_d = 'D-Class'
    
    def getDClass(self):
        return f'{self.str_d}'

# Объявляем C Class

class Cclass(Dclass):
    
    str_c = 'C-Class'
    
    def getCClass(self):
        return f'{self.str_c}'
    
    def getClass(self):
        return f'{self.str_d} наследует с {self.str_c}'


dclass = Dclass()
#print(dclass.getDClass())

cclass = Cclass()
#print(cclass.getCClass())

print(f'Наследование: {cclass.getClass()}')