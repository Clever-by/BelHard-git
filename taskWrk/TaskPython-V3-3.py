# *** Данные в Python #


# *** Работа со строками

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


# End