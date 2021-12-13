# *** Collection Python


# *** Множества, уникальные и неизменяемые элементы в случайном порядке
t = (6,4,6,4)
tu = t

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
# difference(X, Y, ... ) - Множества из всех эдементов (X - Y - ...), непринадлежащее другим
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


# End