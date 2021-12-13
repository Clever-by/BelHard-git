# *** Collection Python


# *** Кортеж, неизменяемый массив

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


# End