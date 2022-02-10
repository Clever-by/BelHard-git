# *** Сериализация


import pickle

# pickle

# метод dump - получает объект и файл
# метод dumps - получает строку 

# Метод load загружает файл
# Метод loads загружает строку

def fun():
    print(f"print{6}")
    return f"ret-{5}"


"""
# Упрощенная технолония:
# метод dump - получает объект и файл
with open(r"./taskWrk/dump/dump_pickle", "w+b") as file:
    pickle.dump(fun, file)
    file.close()
    
with open(r"./taskWrk/dump/dump_pickle", "r+b") as file:
    # Метод loads загружает строку
    #f_fun = pickle.loads(dump_load)
    #dump_load = file.read()
    
    # Метод load загружает файл
    f_fun = pickle.load(file) 
    
    file.close()

f_fun()
"""


#"""
# Старый метод
# метод dumps - получает строку
dump = pickle.dumps(fun)
#print(f"Выводим строку: {dump}")

with open(r"./taskWrk/dump/dump_pickle", "wb") as fw:
    #print(f"Запись в файл: {fw.write(dump)}")
    fw.write(dump)
    fw.close
    
with open(r"./taskWrk/dump/dump_pickle", "rb") as fr:
    #print(f"Содержание документа: {fr.read()}")
    dump_load = fr.read()
    fr.close

# Получение объекта
#print(pickle.loads(dump_load))
#pickle.loads(dump_load)()

# передаем dump в другую переменную
f_fun = pickle.loads(dump_load)

#запускаем
print(f"Результат в функции {f_fun()}")
f_fun()
#"""


"""
# Передаем переменную
string = 'pickle'

with open(r"./taskWrk/dump/dump_pickle", "wb") as file:
    pickle.dump(string, file)
    file.close()

with open(r"./taskWrk/dump/dump_pickle", "rb") as file:
    # Метод loads загружает строку
    dump_load = file.read()
    f_fun = pickle.loads(dump_load)
    # Метод load загружает файл
    #f_fun = pickle.load(file) 
    file.close()

print(f"Результат переменной: {f_fun}")
"""

# End