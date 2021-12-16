# *** Собирание аргументов

# *аrgs - массив позиционных аргументов
# kwargs - словарь именнованных аргументов


# Функция по собиранию аргументов
def sumArray(*str_array, **named):
    #print(str_array)
    #print(named)
    result = 0
    for item in str_array:
        result += item
    
    for item in named.values():
        result += item
    
    return result


#rez = sumArray(1, 2, 3, 4, a='Col', b='Key')
print('Сумма всех эдементов в массиве:', sumArray(1, 2, 3, 4, a=6, b=9))


def sumArraySt(*str_array, start_num = 0):
    result = start_num
    for item in str_array:
        result += item
    
    
    return result


print('Сумма всех эдементов в массиве:', sumArraySt(1, 2, 3, 4, start_num=10))


# End