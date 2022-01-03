# *** Вызываемые исключения: Raise

class ZeroAdditionError(ValueError):
    pass
    

a = input('Введите число "a": ')
b = input('Введите число "b": ')

def add_to(a, b):
    if a == 0:
        # Если a = 0 
        a = 100
        
    if b == 0:
        # Сообщить об ошибке
        raise ZeroAdditionError('zero addition is not supported')
        #raise ZeroAdditionError # - Без комментария
        #raise ValueError('zero addition is not supported')
    return a * b

# *** 
try:
    a = int(a)
    b = int(b)
    print(add_to(a, b))

except ValueError as VE:
    print(ValueError),
    print("сообщение об ошибке: ", VE, "\n"+"тип ошибки: ", type(VE))
    # Если b = 0 и получаем ошибку, то b = 1  
    b = int(1)
    print(add_to(a, b))

    
# End