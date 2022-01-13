# *** Class

# Итераторы

# Тот же Counter, только из библиотеки
from itertools import count

import random

class Counter:
    '''Итератор числе от 'start' до бесконечности'''
    
    def __init__(self, start):
        '''Итератор числе от 'start' до бесконечности
        Parameters: start (int)
        '''
        self.counter = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        res = self.counter
        self.counter += 1
        return res
    

#range(100)

sample = [False]*9 + [True]
# shuffle - перемешивание
#random.shuffle(sample)
#print(sample)

# Функция запроса
def do_request():
    """Функция запроса"""
    random.shuffle(sample)
    return sample[0]


# *** Вариант 1
# *** C использованием Class Counter
for attempt in Counter(1):
    if do_request():
        print(f'Good test {attempt}')
        break
    
    else:
        print(f'False test {attempt}')
    
# Описание функции
#print(do_request.__doc__)

# *** Вариант 2
# *** Без использования Class Counter
attempt = 0
while True:
    if do_request():
        print(f'Good test {attempt}')
        break
    
    else:
        print(f'False test {attempt}')
        attempt += 1


# *** Вариант 3
# *** C использованием Class count
for attempt in count(1):
    if do_request():
        print(f'Good test {attempt}')
        break
    
    else:
        print(f'False test {attempt}')
        
        
# End