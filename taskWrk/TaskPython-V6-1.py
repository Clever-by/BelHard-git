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


def sum_all(a, b, c, d):
    
    def sum_in(s1, s2):
        return s1+s2
    
    return sum_in(
        sum_in(a, b),
        sum_in(c, d)
    )

list_el = [1,2,3,4]
#list_el = list(1,2,3,4)
s = sum_all(list_el[0], list_el[1], list_el[2], list_el[3])
print(f"Сумма функции = {s}")

# End