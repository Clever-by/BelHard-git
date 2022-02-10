# *** Операторы ветвления if-elif-else


print('Выберите действие: ',"\n"+"Запустить цикл 'For' - F", "\n"+"Запустить цилк 'While' - W", "\n"+"Запустить генератор - 'G'", "\n"+"Запустить случайную последовательность - Any Symbol")
str_in = input("Укажите действие:")

import random

list_num = list()
str_name = ''

if str_in == 'F' or str_in == 'f':
    for i in range(10):
        list_num.append(random.randint(1,20))
        str_name = 'Цикл "For":'

elif str_in == 'W' or str_in == 'w':
    num_start = 0
    num_end = random.randint(1,10)
    while num_end > num_start:
        list_num.append(random.randint(1,20))
        str_name = 'Цикл "While":'
        
elif str_in == 'G' or str_in == 'g':
    list_num = [i+random.randint(10,20) for i in range(10)]
    str_name = 'Цикл "Generator":'

else:
    list_num = list(str_in)
    str_name = 'Random string:'
    # Сокращенная форма if-else
    count_st = len(list_num) if len(list_num) < 1 else 0 
    print('Длина строки str_in: ', count_st)

print(str_name, list_num)


# End