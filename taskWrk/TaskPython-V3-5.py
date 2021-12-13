# *** Данные в Python #


# *** Манипулчции с числами

int_a = 5
int_b = 6
int_c = input('Введите целое число, иначе будет ошибка: ')

# *** Методы вывода результата
print(f'Sum of a and b is {int_a + int_b}.') # Ver.1
print ('Sum of ' + str(int_a) + ' and ' + str(int_b) + ' is ' + str(int_a+int_b) + '.') # Ver.2

int_c = int(int_c)

if int_c != None and type(int_c) == type(int()):
    import math # Вызов библиотеки math
    a = int_a
    b = int_b
    c = math.cos(45)
    p = math.pi
    d = c + p + (a*b)
    print("cos(45) = ", c, "pi = ", p, "rezult:", d)
 
else:
    print('Не ввели число')


# End