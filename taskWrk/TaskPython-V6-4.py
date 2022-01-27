# *** Декораторы

# Декораторы - это фунции, которые принимают другие функции и изменяют их поведения

#from functools import lru_cache

# ................................

"""
@lru_cache
def sum(*array, start_with = 0):
    result = start_with
    if len(array) == 0:
        return 0, len(array) 
    else:
        for element in array:
            result += element
            
    return result, len(array)

"""
# ................................
"""

def sum(*array, start_with = 0):
    result = start_with
    if len(array) == 0:
        return 0, len(array) 
    else:
        for element in array:
            result += element
           
    return result, len(array)

"""

# передача фунуции sum через декоратор
#sum = lru_cache(sum)

#rez, rez_len = sum(1,2,3,5)
#print(sum(1,2,3,5))
#print(rez, rez_len)

# ................................

def logger(f):
    def inner(*args, **kwargs):
        print("Before")
        # *********************
        res = f(*args, **kwargs)
        res_kw = f(**kwargs)
        # *********************
        print(f"Res: {res} KW: {res_kw}")
        print("After")
        return res
    
    return inner


# Оборачивание функции:
#@logger
def sum(*array, start_with = 0):
    result = start_with
    if len(array) == 0:
        return 0, len(array) 
    else:
        for element in array:
            result += element
           
    return result, len(array)


res_list = logger(sum)(3,5,6)
print(res_list)

# передача фунуции sum через декоратор
#sum = logger(sum)

#res_sum, res_len = sum(1,2,3,5)
#print("Результат: ", res_sum)


# End