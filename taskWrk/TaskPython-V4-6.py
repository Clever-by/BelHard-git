# *** Collection Python


# *** Dict - Словарь
# *** Оперпции в словаре

d1 = dict()
d2 = {}
d3 = {1:'one', 2:'two'}
d4 = dict(type='course', name='python')
d5 = dict([(1, 2), (2, 3)])
d6 = dict.fromkeys([1, 2, 3, 4], None)
print("Вывод словарей:", "\n"+"d1:", d1, "\n"+"d2:", d2, "\n"+"d3:", d3, "\n"+"d4:", d4, "\n"+"d5:", d5, "\n"+"d6:", d6)
#squares = {item: item**2 for item in range(6)}
#print("Output squares: ", squares)


#range(x,y,z)
# x - стартовое значение
# y - максимальное значение
# z - шаг
"""
for i in range(3, 28, 8):
    quotient = i / 3
    print (i, quotient)
    print(f"{i} делится на 3, результат {int(quotient)}.")
"""
# *** Оперпции в словаре

#x in d # - проверка ключа
#print('Key 1: ', 1 in d5)
#d[key] # - достать элемент по ключу
print('Key name: ', d4['name'])
#d.get(key[, default]) #
#del d[key] # - удаление ключ-значение
#d.pop(key[, default]) # - удаляет ключ и возвращает значение
#d.popitem() # - удаляет и возвращает пару (ключ, значение)
#d.clear() # - очищает словарь.
#d.copy() # - возвращает копию словаря.
#d.items() # - возвращает пары (ключ, значение).
#d.keys() # - возвращает ключи в словаре.
#d.values() # - возвращает значения в словаре.
#d.update([other]) #- обновляет словарь, добавляя пары (ключ, значение) из other.


# End