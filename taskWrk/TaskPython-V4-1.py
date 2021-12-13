# *** Collection Python


# *** List
# *** Список методов
# *** Встроенные функции
# *** Сортировка
# *** Встроенные функции
a0 = []
a2 = [1, 2, 3, -6, 10, 3, 20, 4, 3]
a3 = list()
a4 = list(a2)

print('Output element collection: ', a4[2], '\n', 'Output collection: ', a2) # Вывод с переносом на новую строку
# a[start:end:step]
# -1 - обратный отсчет 
print('Output range on step: ', a4[1:4:2])


# *** Список методов

a4.append(3)        # - Добавить в конец строки
a2.insert(4, 7)     # - добавить по индексу

print('addition collection: ', 'a4:', a4, ' and ', 'a2:', a2)

a4.remove(3)        # - удадение по значению

print('Detleted element in collection "a4":', a4)

a4.clear()          # - Удаление все массива

print('All collection:', 'a1:', a1, 'a2:', a2, 'a4:', a4)

p = a2[3]                               # - Возвразщает значение элмемента по позиции, если позиция(индекс) в массиве не существует, выдаст ошибку
print('Element value: ', p)        
i = a2.index(2)                         # - Возвразщает позицию элмемента по значению, если значения нет, выдаст ошибку
print('Element Index: ', i)  

print ('Collection a2: ', a2)
a2.pop(i)           # - удаляет по индексу
print ('Collection a2: ', a2)
a2.append(2)        # - Добавляем в конец коллекции
a2.append(3)        # - Добавляем в конец коллекции
print ('Collection a2: ', a2)

b = a2.count(3)     # - считает совпадение элементов в коллекции
print('Element count value=3: ', b, 'Collection a2: ', a2)

print('Output collection a2: ', a2)


# *** Сортировка 
# Можно использовать ключ
c = list(a2)
c.sort()        
#c = list(a2.sort())

print('Output collection "Sort" c: ', c)

k = list(a2)
print('Output collection k: ', k)

def st(k):
    return abs(k)

k.sort(key=st)
print('Output collection "Sort(ABS)" k: ', k)

r = list(c)
r.reverse()     # - Обратный порядок
print('Output collection "Sort" c: ', c)
print('Output collection "Revers" r:', r)


# *** Встроенные функции

print('String Length collection a2: ', len(a2))
print('Sorted collection a2: ', a2) # - Сортирует элементы без внесение изменений в список
print('Max element collection a2: ', max(a2))
print('Min element collection a2: ', min(a2))

print('Output collection a2: ', a2)

# ф-ция enumerate, добавляет нумерацию к списку. Можно указать начало нумерации

print('Output collection a2: ', list(enumerate(a2,1)))

print('Output collection a2: ', list(enumerate(a2)))