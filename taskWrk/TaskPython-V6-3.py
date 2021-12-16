# *** Аннотации типов

# Аннотации - подсказки для разработчиков и редактора/IDE

import random

# Функция операции над числом
def operation(in_int):
    result = 0
    print(in_int)
    while in_int > result:
        result += 1
    
    return result


print('Операции над Числом', operation(random.randint(1,10)))

# End