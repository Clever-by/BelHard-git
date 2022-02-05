# Полезные модули


# Модуль copy
import copy
from multiprocessing.connection import answer_challenge

a = [1, 2, [1,2,3]]

# copy.copy() - Поверхностное копирование
# copy.depcopy() - глубокое копирование
c=a
b=copy.copy(a)
d=copy.deepcopy(a)

b.append(4)
b[2].append(5)

print(a)
print(b)
print(c)
print(d)

# Математические модули


# Decimal - истинные десятичные дроби
from decimal import Decimal as dec

print(f"Последовательно: {0.1 + 0.2 + 0.3}") # Последовательно
print(f"Непоследовательно: {0.1 + 0.4}") # Непоследовательно
print(dec('0.1') + dec('0.2') == dec('0.3'))

# Fraction - дроби без погрешностей
from fractions import Fraction

print(3/3 + 3/5 == 8/3)
print(Fraction(3, 3) + Fraction(5, 3) == Fraction(8, 3))

# Математический math
import math
#Тригонометричексие (sin, cos, tan, ctan)
#Округления (round, ceil, floor)
#Константы (pi, e)
# and others

print(math.pi, math.e)


import random

#random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
#random.choice(sequence) - случайный элемент непустой последовательности.
#random.shuffle(sequence) - перемешивает последовательность.
#random.sample(population, k) - список длиной k из последовательности population.
#random.random() - случайное число от 0 до 1.

answer = random.randint(1, 100)
print(answer)

colors = ['red', 'blue', 'green', 'grey']
color = random.choice(colors)
#print(color)

def choice(collection):
    #print(len(collection))
    rez_color = collection[random.randint(0,len(collection)-1)]
    return rez_color
    
print(choice(colors))

print(colors)
random.shuffle(colors) # Перемешиваем массив с изменением
print(colors)

print(random.sample(colors, 2))


print(random.random())

def randfloat(a=0, b=1):
    length = abs(a - b)
    
    return a + random.random() * length
                 
print(randfloat(-10,5))


# End