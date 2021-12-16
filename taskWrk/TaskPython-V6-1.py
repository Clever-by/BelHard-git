# *** Функции в  Python

# Функция без входных аргументов
def outString():
    print('Функции в Python')

outString()

import math

# Функция с входными аргументами
def SumInteger(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

a = 3
b = 4

print('Длинна гипотенузы: ', SumInteger(a, b))

# Аргументы двух типов: позиционные и именновыные
def sum(a,b,c=5):
    return (a + b + c)

print('Сумма a + b + c =', sum(a,b))


# Функция по обратотке массива
def sumArray(str_array):
    result = 0
    for item in str_array:
        result += item
    return result


print('Сумма всех эдементов в массиве:', sumArray([1,2,3,4]))

# End