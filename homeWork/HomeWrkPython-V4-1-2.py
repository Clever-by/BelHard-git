# Программа на вход получет данные о треугольниках и выводит на экран информацию о каждом треугольнике.

sides = input('Введите через пробел сторон треуголника (a b): ')

sides_tr = sides.split()

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

#Parity check
def parity(p_elment):
    p_out = p_elment % 2
    return p_out

#print('addition collection (a b): ', sides_tr, 'leng =', len(sides_tr))

if parity(len(sides_tr)) == 0:
    index = len(sides_tr)
    
else:
    index = len(sides_tr)-1

print("Количесво введенных значений: ", len(sides_tr), "\n"+"Количество треугольников: ", int(index/2), "\n"+"Лишних значений: ", len(sides_tr)-index)

num = 0
while index > num:
    print('Катет a =',sides_tr[num])
    print('Катет b =',sides_tr[num+1])
    #Calculation the area of a triangel
    print('Площадь треугольника равна =', triangel(abs(int(sides_tr[num])), abs(int(sides_tr[num+1]))))
    # Calculation of the hypotenuse
    print('Гипотернуза равна =', hypotenuse(abs(int(sides_tr[num])), abs(int(sides_tr[num+1]))))
    num += 2