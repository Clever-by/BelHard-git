# *** Данные в Python #


# *** комментарии в Python

# *** однострочный комментраий
#print("Комментариий")


# *** Блочный комментарий
"""

1~
2~
...
n~

"""
# End


# **** Переменные
"""
a = 4
b = 5
c = None
c = a + b
i = 10

# Вывод значений переменных

print ('Значение переменных: ', 'a =', a, 'b =', b, 'c = ', c, 'i = ', i, 'c меньше i', c < i)

"""
# End


# *** Работа со строками
"""
str_x = 'Test1'
str_y = 'Test2'
int_i  = 5

print("Конкатенация строк: 'str_x||str_y' = ", str_x + str_y)
print("Длинна строки: ", (str_x+str_y), '=', len(str_x+str_y))
print("Строка c||d повтаренная - ", int_i, " = ", (int_i * (str_x + str_y)))

# *** Вывод определеного символа в строке с конца
# от 0[1] - сначала, [-1] - сконца
print(str_x[1]) # нумерация с начала строки, отсчет с 0 (нуля)
print(str_x[-2]) # нумерация с конца строки

# [::] чтение строки начиная с определенного по нумерации символа справа на лево, [::-] - слева на правл
print(str_y[::-1]) # слева на правл
print(str_y[::2]) # справа на лево

str_l = "/n"*100
print('Длинна строки: ' , str_l, '=', len(str_l))

# *** Однотипность ковычек

print("Single quoted: ' '") # Вывод одинарных ''
print('Double quoted: " "') # Вывод двойных " "

print('a\tb\tc\n','a\tb\tc\n', sep='', end='\\*') # \t - Табуляция
print(r'\\fdfsd\sdf\n', 'Single quote: \'.') # r - отключение спец-символов 

# *** Вывод данных

self = 'String manual'
# sep= - разделитель
# end= - Конец строки
# /n - Перенос строки

print('string1', self, 'string2', self, sep='*', end='\n**End**\n*\n')

"""
# End


# **** Ввод (input), вывод (print) строковых данных
"""
print('Введите строку')
str_a = None
str_b = input()
str_c = len(str_b)
str_a = str_b
#str_m = 'Длинна строки str_a: ' +  str_a*2 + ' + str_b: ' + str_b*5 + ' + str_c: ' +  str(str_c)*2
#print(str_m)

if str_b == 'None':
    print('No data')

else:
    print('Sucefully', 'Input: ', str_b)

"""
# End
    
# *** Манипулчции с числами
"""
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

"""
# End


# *** Тип данных и определение: int, float, str, ...
"""
a1 = 1
a2 = -1.0
a3 = "string"

# *** Вывод типа переменной
print('Вывод типа переменной: ', '\na1: ', type(a1), '\na2: ', type(a2), '\na3: ', type(a3))
print('Отсутствие значения и Логический тип: ', '\nNone', type(None), '\nbool', type(a1 > a2), '\nbool', type(a1 == a2))


b1 = (0b0, 0b1, 0b10, 0b11, 0b100)
b2 = 1/2
b3 = 1e12
b4 = 1 * 10**12

# *** Вывод зеачения и типа переменной
print("переменная b1 = ", b1, "type: ", type(b1))
print("переменная b2 = ", b2, "type: ", type(b2))
print("переменная b3 = ", b3, "type: ", type(b3))
print("переменная b4 = ", b4, "type: ", type(b4))


# *** Фиксированное количество знаков после запятой
c1 = 1 / 3
c2 = c1

c1 = float('{0:.3f}'.format(c1))  # Ver.1 -- {:.3f}
c2 = ("%.3f" % c1) # Ver.2
# Вывод результата количество знаков после запятой
print('c1 = ', c1)
print('c2 = ', c2)

"""
# End


# Поиск в строке позиции символа
"""
s = 'string one length'
print(s.find('ring'))
print(s.rfind('str'))
print(s.find('tit'))

# Замена в строке
print(s.replace('one', 'two'))

"""
# End


# Разделитель
""""
s = 'string one length'
print(s.split()) # Разделитель поумолчанию пробеил(' ')

st = input()
print(st.split(',')) # задаем разделитель свой запятая(',')

"""
# End


# Поиск в строке 
"""
print('spr' not in 'Spam') # невхождение подстроки, True
print('spr' in 'Spam') # вхождение подстроки, False

"""
# End


# Сравнение в ящейке памяти
#"""
p_s1 = 'abcd'
p_s2 = 'abcd'
p_s3 = 'absd'
p_s4 = p_s3

# Сравнение значения в памяти
print(p_s1 is p_s2)
print(p_s2 is p_s3)
print(p_s4 is p_s3)

# Вывод ячеек памяти со значение
print(id(p_s1), id('abcd'), id(p_s3), id('absd'))

#"""
# End