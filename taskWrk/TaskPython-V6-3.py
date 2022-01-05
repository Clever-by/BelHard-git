# *** Аннотации типов

# Аннотации - подсказки для разработчиков и редактора/IDE

import random

# Функция операции над числом, сколько раз и результат = сумма
def operation(in_int: int) -> list:
    count = 0
    sum = 0
    print('Element: ', in_int)
    while in_int > count:
        count += 1
        sum += in_int
    
    return in_int, count, sum 
    

list_operaion = operation(random.randint(1,10))
sum = list_operaion[0]*list_operaion[1]
print('Операции над Числом, Сколько раз, Сумма:', list_operaion, " = ", sum)

# Через "," можно передать значения в переменные
#e1, e2, e3 = operation(int(78))
#print(e1, e2, e3)

# End