# *** Class

# Методы

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


    
i = HomoSapince(82, 170)
you = HomoSapince(83, 172)
print("ip:", i.weight_index())
print(i.talk('en'))
print(you.talk('ru'))
i.weight = 85
print("ip:", i.weight_index())

#baby = HomoSapince.born()
#print(baby)
#baby.talk('ru')

HomoSapince.born().arms

baby1 = HomoSapince.work()
print(baby1)

#baby2 = HomoSapince(5, 50)
#print(baby2)


# End