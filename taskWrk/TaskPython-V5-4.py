# *** Обработка ошибок: Exception

import math
from typing import final

array = [9, 4, -25, 64, 49, 81, -16]

# Выполнение через if-elif-else
"""
for num in array:
    if num > 0:
        print(f"Корень числа {num}: {math.sqrt(num)}")
    
    else:
        print("Отрицательное цисло")
"""

"""            
# Выполнение через try except else finally
for num in array:
    
    # Код, который может вызвать ошибку
    try:
        print(f"Корень числа {num}: {math.sqrt(num)}")
    
    # Обработчик ощибки
    except:
        print(f"Отрицательное цисло: {num}")
    
    # *** Опционально
    
    # Если ошибка не произошла
    else:
        print("Положительное число: ", abs(num))
    
    # Выполнять, lдаже если была ошибка
    finally:
        if num < 0:
            print(f"Корень отрицательного числа {num}: по модулю {math.sqrt(abs(num))}")
"""
"""
a = input('Введите первое число: ')
b = input('Введите первое число: ')

# Проверка на число
def is_numerable(s):
    # Проверяем строку
    try:
        int(s)
    
    # Если ошибка
    except:
        return False
        
    # Еслм нет ошибки    
    else:
        return True
        
# Проверяем число "a"
if is_numerable(a):
    print('Число')

else:
    print('Не число')

# Проверяем число "b"
if is_numerable(b):
    print('Число')

else:
    print('Не число')


try:
    a = int(a)
    b = int(b)
    print(a/b)

except ValueError as VE:
    #print('Error')
    print("Не число", ValueError)
    print(VE, "Тип ошибки: ", type(VE))   
 
except ArithmeticError as AE:
    #print("Error")
    print("Арифметическая", ArithmeticError)
    print(AE, "Тип ошибки: ", type(AE)) 
"""

"""
except ZeroDivisionError as ZE:
    print("Деление на ноль", ZeroDivisionError)
    print(ZE, "Тип ошибки: ", type(ZE))
"""

# *** Работа с файлами

# «r»	открытие для чтения (по умолчанию)
# «w»	открытие для записи, а если его не существует по заданному пути, то создается новый
# «x»	открытие для записи, но только если его еще не существует, иначе будет выдано исключение
# «a»	открытие на дополнительную запись, чтобы информация добавлялась в конец документа
# «b»	открытие в двоичном режиме
# «t»	открытие в текстовом режиме (по умолчанию)
# «+»	открытие одновременно на чтение и запись         

# Проблема с кодировкой utf-8, читает файлы только с кодировкой cp1251
# Используем encoding="utf-8": open(encoding="utf-8")
# Используем encoding="ansi": open(encoding="ansi")
# Используем encoding="cp1251": open(encoding="cp1251")


with open(r'./taskWrk/resource/fileTask-5.txt', 'r', encoding="utf-8") as f:
    print(f.read())
    string = f.read()
    print(string)
    f.close()


# Открытие файла для чтения
f1 = open(r'./taskWrk/resource/fileTask-5-1.txt', "r")

print(f"Открыт файл {f1.name} для чтения {f1.mode} c типом: {type(f1)}")
print(f"Используется метод read: {f1.read}")
#print(f"Содержание документа: {f1.read()}")

str1 = f1.read()
print(f"Текст с переменной str1={str1}")

f1.close()

"""
# Перезапись файла, если файла нет, то файл создается.
f2 = open(r'./taskWrk/resource/fileTask-5-2.txt', "w", encoding="utf-8")

print(f"Открыт файл {f2.name} для записи {f2.mode} c типом: {type(f2)}")
print(f"Запись в файл: {f2.write('Test')}")

f2.close()
"""
"""
# Открытие файла для дозаписи. Если файла нет, то файл создается
f3 = open(r'./taskWrk/resource/fileTask-5-3.txt', "a", encoding="utf-8")

print(f"Открыт файл {f3.name} для записи {f3.mode} c типом: {type(f3)}")
print(f"Запись в файл: {f3.write('Test')}")

f3.close()
"""

# End