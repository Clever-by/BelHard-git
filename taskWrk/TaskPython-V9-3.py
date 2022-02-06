# itertools

#zip, range, enumerate

import itertools

colors = ['red', 'blue', 'green', 'grey']
for color in colors:
    print(color)

# itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step
i = 0
for color in itertools.count():
    print(colors[color % len(colors)])
    i += 1
    if i == 100:
       print(i)
       break

#itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз
i = 0
for color in itertools.cycle(colors):
    print(color)
    i += 1
    if i == 100:
        print(i)
        break

#itertools.repeat(elem, n=Inf) - повторяет elem n раз
print(f"{list(itertools.repeat(4,5))}")

#itertools.accumulate(iterable) - аккумулирует суммы
salaries = [4,3,8,4,9,3,4,6,4]
print(list(itertools.accumulate(salaries)))

#itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор, пока итераторы не кончатся
print([1,4,6]+[0,5,3,6])
print(list(itertools.chain([1,4,6], [0,5,3,6])))
print(list(itertools.chain(range(1, 10), range(8, -10, -2))))

#itertools.zip_longest(*iterables, fillvalue=None) - как  встроенная функция zip, но берет самый длинный итератор, а более  короткие дополняет fillvalue
a = [1,3,4,6,7,11]
b = [4,6,8,10]
print(list(zip(a,b)))
print(list(itertools.zip_longest(a,b, fillvalue=0)))


# End