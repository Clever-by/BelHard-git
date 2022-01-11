# *** Class

# Класс является шаблоном или формальным описанием объекта, а объект представляет экземпляр этого класса, его реальное воплощение

class HomoSapince:
    # Переменная класса
    arms = 2
    
    def __init__(self, weight=1, height=1):
        
        # Атрибуты объекта
        self.weight = weight # Задается и может изменяться
        self.height = height # Задается и может изменяться
        self.weight_index = weight / height**2 # Расчитывается
        
        #print("Object:", self)

i = HomoSapince()

#print("Object:", i)
#print("Type:", type(i))

# *** Self Ссылка на самого себя

i.weight = 82
i.height = 30
ip = i.weight_index
i.skin_color = 'White'

print("ip:", ip)
print("Arms:", i.arms)
print("skin_color:", i.skin_color)

you = HomoSapince(83,40)
you.skin_color = 'Grey'

print("weight:", you.weight)
print("height:", you.height)
print("ip:", you.weight_index)
print("skin_color:", you.skin_color)

# Обращение к переменной класс
print("Arms:", HomoSapince.arms)


# End