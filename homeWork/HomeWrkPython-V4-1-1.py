# Программа на вход получет данные о треугольниках и выводит на экран информацию о каждом треугольнике.

print('Выберите режим ввода:', '\n' + 'Если ввести - Y, то ввод будет ручным', '\n' + 'Если ввести - N либо любое другое значение, то ввод будет автоматический')

str_way = input('Введите режим: ')

import math
import random

#Calculation of the hypotenuse
def hypotenuse(side_a, side_b):
    side_c = math.sqrt(side_a**2 + side_b**2)
    return side_c 

#Calculation the area of a triangel
def triangel(side_a, side_b):
    area_t = (side_a * side_b)/2
    return area_t 


if str_way == 'Y' or str_way == 'y':
    str_a = input('Введите стороны треугольника через пробел a= ')
    str_b = input('Введите стороны треугольника через пробел b= ')
    
    a = str_a.split()
    b = str_b.split()

    print('addition collection a: ', a, 'leng =', len(a))
    print('addition collection a: ', b, 'leng =', len(b))
    
    if len(a) >= len(b):
        index = len(b)
        
    else: 
        index = len(a)
    
else:
    int_count = input('Сколько треугольников рассчитать?=')
    int_count = abs(int(int_count))
    a = []
    b = []
    
    index = 0
    while index < int_count:
        #print(index)
        a.append(random.randint(1,100))
        b.append(random.randint(1,100))
        index += 1
        
print('addition collection a: ', a)
print('addition collection b: ', b)
    
num = 0
while index > num:
    print('Катет a =',a[num])
    print('Катет b =',b[num])
    #Calculation the area of a triangel
    print('Площадь треугольника равна =', triangel(abs(int(a[num])), abs(int(b[num]))))
    # Calculation of the hypotenuse
    print('Гипотернуза равна =', hypotenuse(abs(int(a[num])), abs(int(b[num]))))
    num += 1