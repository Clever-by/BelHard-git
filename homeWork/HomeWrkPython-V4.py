#
print('Выберите из списка:', '\n', '1 - Ввести стороны треуголника в ручную для расчет гипотенузы', '\n', '2 - Ввести стороны треуголника в ручную для площади', '\n', 'Либо введите любое значение')
st_tiket = input('Введите значение=')

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

if st_tiket == '1' or st_tiket == '2':
    side_a = input('Введите сторону треугольника a=')
    side_b = input('Введите сторону треугольника b=')
    side_a = abs(int(side_a))
    side_b = abs(int(side_b))
    print('Катет a =', side_a, 'тип переменной:', type(side_a))
    print('Катет b =', side_b, 'тип переменной:', type(side_b))
    if st_tiket == '1':
        # Calculation of the hypotenuse
        print('Гипотернуза равна =', hypotenuse(side_a, side_b))
    
    if st_tiket == '2':
        #Calculation the area of a triangel
        print('Площадь треугольника равна =', triangel(side_a, side_b))
        
else:
    print('Others')
    st_step = input('Сколько треугольников рассчитать?=')
    st_step = abs(int(st_step))
    a = []
    b = []
    
    index = 0
    while index < st_step:
        #print(index)
        a.append(random.randint(1,100))
        b.append(random.randint(1,100))
        index += 1
        
    print('addition collection a: ', a)
    print('addition collection b: ', b)
    
    num = 0
    while index > num:
        print('Катет a=',a[num])
        print('Катет b=',b[num])
        #Calculation the area of a triangel
        print('Площадь треугольника равна =', triangel(a[num], a[num]))
        # Calculation of the hypotenuse
        print('Гипотернуза равна =', hypotenuse(a[num], a[num]))
        num += 1
        
        #persons_three_most_popular_names = Counter([d.get("name") for d in persons]).most_common(3)
