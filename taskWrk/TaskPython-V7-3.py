# *** Class

# Магические методы

class HomoSapince:
    # Переменная класса
    arms = 2
    
    def __init__(self, weight=1, height=1):
        
        # Атрибуты объекта
        self.weight = weight # Задается и может изменяться
        self.height = height # Задается и может изменяться
        #self.weight_index = weight / height**2 # Расчитывается

    def weight_index(self):
        return self.weight / (self.height / 100) ** 2
    
    def talk(self, lang=None):
        if lang == 'ru':
            print(f'Привет, мой рост: {self.height}, мой вес {self.weight}')
            
        elif lang == 'en':
            print(f'HI, My height: {self.height}, My weight {self.weight}')
         
        else:
            print("I Don't")
            
        # Если нету вывода, будет "None"
        return 'End'

    # При обращении, выводит результат без print
    @classmethod
    def born(cls):
        print("arms:", cls.arms)
        return cls(4.5, 53)

    @staticmethod
    def work():
        return 'Стремление к труду'
    
    def isGreater(self, other):
        return self.height > other.height

    # Использование магического метода ">"
    def __gt__(self, other):
        return self.height > other.height
    
    #def __add__(self, other):
        #return self.born().talk('ru')
    
    def __add__(self, other):
        return 'Love'
    
    def __len__(self):
        return len(str(self.height))
    
    def __int__(self):
        return self.height

    def __call__(self, where):
        return f"Вызвать на {where}"

    def __getitem__(self, index):
        print(index)
       
alex = HomoSapince(82, 175)
anna = HomoSapince(55, 160)

print(alex.isGreater(anna))
print(anna.isGreater(alex))

# Использование магического метода
print(alex > anna)
print(alex + anna)
print(len(alex))
print(alex.height)
print(alex('работу'))
alex[1]


#baby = HomoSapince.born()
#print(baby.height, baby.weight)
#print(baby.height + 6, baby.weight + 3)
#print(baby.height, baby.weight)

# Если в функции нет "Return", то втрой строчкой выводится "None"?
# @classmethod - Как работает? Если обратиться напрямую, то это функция?
# HomoSapince.born().arms - выдает результат без "Print", почему?
# 

# End