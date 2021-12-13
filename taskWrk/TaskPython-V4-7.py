# *** Collection Python


# *** Модуль collections

# *** Дополнительные коллекции, например:
#Counter
#deque
#defaultdict
#namedtuple

# *** Collections (Counter)

import collections

s = 'one two one three two two'
words = s.split()
print(words)
counter = collections.Counter(words)
print(counter)
print(counter['one'] == 5, counter['one'] == 2)

# *** Collections (deque)

deq = collections.deque()

#append(x) # - добавляет x в конец.
#appendleft(x) # - добавляет x в начало.
#clear() # - очищает очередь.
#count(x) # - количество элементов, равных x.
#extend(iterable) # - добавляет в конец все элементы iterable.
#extendleft(iterable) # - добавляет в начало все элементы iterable
#pop() # - удаляет и возвращает последний элемент очереди.
#popleft() # - удаляет и возвращает первый элемент очереди.
#remove(value) # - удаляет первое вхождение value.
#reverse() # - разворачивает очередь.
#rotate(n) # - последовательно переносит n элементов из начала в конец).

# *** Collections (namedtuple)

Point = collections.namedtuple('Point', 'x y')
p = Point(x=1, y=2)
print(p)
print(p.x == 1, p.y ==2)


# End