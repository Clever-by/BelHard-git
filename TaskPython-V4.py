### Collection

"""

# List
a1 = []
a2 = [1, 2, 3, -6, 10, 3, 20, 4, 3]
a3 = list()
a4 = list(a2)

print('Output element collection: ', a4[2], '\n', 'Output collection: ', a2) # Вывод с переносом на новую строку
# a[start:end:step]
# -1 - обратный отсчет 
print('Output range on step: ', a4[1:4:2])

# Список методов

a4.append(3)        # - Добавить в конец строки
a2.insert(4, 7)     # - добавить по индексу

print('addition collection: ', 'a4:', a4, ' and ', 'a2:', a2)

a4.remove(3)        # - удадение по значению

print('Detleted element in collection "a4":', a4)

a4.clear()          #  - Удаление все массива

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

c = list(a2)
# - Сортировка. Можно испольщовать ключ
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

# - Встроенные функции

print('String Length collection a2: ', len(a2))
print('Sorted collection a2: ', a2) # - Сортирует элементы без внесение изменений в список
print('Max element collection a2: ', max(a2))
print('Min element collection a2: ', min(a2))

print('Output collection a2: ', a2)
print('Output collection a2: ', list(enumerate(a2,1)))
# ф-ция enumerate, добавляет нумерацию к списку. Можно указать начало нумерации
print('Output collection a2: ', list(enumerate(a2)))

# - Генератор

def positive(value):
    return value % 2 == 0 and value > 0


print('Output collection enumerate a2(i(j)): ', list(enumerate(a2)))
col_num = [i[0] for i in enumerate(a2) if i[1]==3]
# i[1] - Индекс по значению, т.к. i[0,1] состоит из индекса и значения
print(col_num)
col_num = [ind for ind, item in enumerate(a2) if positive(item)] #==4]
print(col_num)



print('Output collection a2: ', a2)
sq = [i**2 for i in a2]
print('Collection a2 in squares: ', sq)
#
print('Output collection a2: ', a2)
#
m = [i-2 for i in a2]
print('Collection a2 in minus-2: ', m)
#
print('Output collection a2: ', a2)
ab = [abs(i) for i in a2]
print('Collection a2 in ABS: ', ab)
#
print('Output collection a2: ', a2)
ot1 = [i+100 for i in a2 if i >= 5 and i < 100]
print('Collection a2 in Other If1: ', ot1)
#
print('Output collection a2: ', a2)
ot2 = []
#ot2 = [(if i < 0 i+200) for i in a2]
print('Collection a2 in Other If2: ', ot2)

"""

# Кортеж, неизменяемый массив

t = (6,4,6,4)
print('Output tuple t():', t)
print('Output tuple t():', tuple(enumerate(t)))
# кортежу можно присваивать коллекции
m = list(t) 
print('Collection to tuple ', list(enumerate(m)))
# Коллекцию можно присваивать кортежу
l = tuple(m)
print('Tuple to collection ', tuple(enumerate(t)))

#Изменения в Кортеже
#a = None
#b = None

st = [i+20 for i in t if i > 4]
print('Change tuple:', st, 'Count symbol:', len(st))
if len(st) == 2:
    a, b = st
    print('first value:', a, 'Second value:', b)

print(a,b)
a = None
b = None
print(a,b)

for a, b in tuple(enumerate(t)):
    print(f'first value: {a} Second value: {b}')

print(a,b)

tu = t
# Можно вывести первыми, некую последовательность символов, а остальное в массив
a1, a2,*an = tu
print('list:', a1, a2, an)

list(t).append(10)
t = tuple(t)
print(t)

t = [i*5 for i in t] # Если не обернуть в tuple, будет list
print(t)
print('Output tuple t():', tuple(enumerate(t)))

"""

# Множества, уникальные и неизменяемые элементы в случайном порядке

#s = set()
s = set(t)
su = set(tu)
print('Set: s', s)
print('Set: s', list(enumerate(s)))
print('Set: su', su)

su = {i**2 for i in s}
print(su)

# Количество элементов в можестве
print('Количество элементов в множетсве s:', len(s), 'Количество в Кортеже t:', len(t))

# in - Принадлежность значения, какому-либо контейнеру. 
# Можно использовать для Collection, Tuple, Set или для других объектов
if 40 in s:
    print('No')
elif 30 in s:
    print('Yes')

# Наличие общих элементов - истина, если su и s не имеют общих элементов.
print(su.isdisjoint(s))

# Наличие общих элементов - истина, если su и s имеют общие элементы.
print(su.issubset(s))

# == - равно, <= - , >=
# X.isdisjoint(Y) - не имеют общих, 
# X.issubset(Y) - имеют общие,  из X <= Y
# X.issuperset(Y) - имеют общие, из Y >= X
# union(X, Y, ...) - Объединение (X | Y |...)
# intersection(X, Y, ...) - Пересечение (X & Y & ...)
# difference(X, Y, ... ) - Множества из всех эдементов (X - Y - ...), не принадлежащее другим
# X.symmetric_difference(Y) - Множества из элементов X ^ Y -, встречаюзиеся в одном множестве, но не встречающиеся в обоих  
# X.copy() - копия множества

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}
s3 = s1.symmetric_difference(s2)
print(s3)
print(s1 - s2)

# update()
# intersection_update()
# difference_update()
# symmetric_difference_update()
# add()
# remove()
# discard()
# pop()
# clear()

"""

# frozenset - Неизменяемое множество
f1 = frozenset({1, 2 , 3, 4})
f3 = frozenset({'Nat', 'Set', 'Most'})
f2 = {(6, 7), frozenset({8, 9, 10})}
print(f1, f2, f3)

# Dict - Словарь