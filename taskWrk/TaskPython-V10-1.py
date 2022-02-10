# *** Работа с файлами


from pathlib import Path
#from importlib.resources import path

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


with open(r"./taskWrk/resource/fileTask-11.txt", "r", encoding="utf-8") as f:
    # Если запускаем read, то запись вытягивается из буфера один раз:
    #print(f.read())
    
    # Если по строчно, то получаем записи построчно:
    #print(f.readline())
    
    # Все строки списком:
    #print(f.readlines())
    
    #print(f.read)
    #print(f.readline)
    #print(f.readlines)
    
    string = f.read()
    #string = f.readlines()
    print(string)
    f.close()

"""
# Открытие файла для чтения
f1 = open(r'./taskWrk/resource/fileTask-10-1.txt', "r+t")

print(f"Открыт файл {f1.name} для чтения {f1.mode} c типом: {type(f1)}")
print(f"Используется метод read: {f1.read}")
print(f"Содержание документа: {f1.read()}")

str1 = f1.read()
print(str1)

f1.close()
"""
"""
# Перезапись файла, если файла нет, то файл создается.
f2 = open(r'./taskWrk/resource/fileTask-10-2.txt', "w+t", encoding="utf-8")

print(f"Открыт файл {f2.name} для записи {f2.mode} c типом: {type(f2)}")
print(f"Содержание документа: {f2.read()}")
print(f"Запись в файл: {f2.write('Test')}")
print(f"Содержание документа: {f2.read()}")

f2.close()
"""
"""
# Открытие файла для дозаписи. Если файла нет, то файл создается
f3 = open(r'./taskWrk/resource/fileTask-10-3.txt', "a+t", encoding="utf-8")

print(f"Открыт файл {f3.name} для записи {f3.mode} c типом: {type(f3)}")
print(f"Содержание документа: {f3.read()}")
print(f"Запись в файл: {f3.write('Test')}")
print(f"Содержание документа: {f3.read()}")

f3.close()
"""
#"""
# pathlib.path
path = Path(r"./taskWrk/resource/fileTask-10.txt")


with path.open("r", encoding="utf-8") as pf:
    print(pf.read())
    string = pf.read()
    print(string)
    pf.close()
#"""
path_gl = Path(r"./taskWrk")
print(path_gl.iterdir())
print(list(path_gl.iterdir()))

#Создать директорию с правами
path_new = Path(r"./taskWrk/new")
path_new.mkdir(mode=600)


# End