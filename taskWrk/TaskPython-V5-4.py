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
except ZeroDivisionError as ZE:
    print("Деление на ноль", ZeroDivisionError)
    print(ZE, "Тип ошибки: ", type(ZE))
"""

# *** Запись в файл
"""
a = input('Введите цисло:')            

try:
    f = open('resource/file-5.txt')
    a = int(a)
    
except:
    print('Error')
    
else:
    f.write(a)

finally:
    a = 0
    f.write(a)
    f.close()
"""

# End