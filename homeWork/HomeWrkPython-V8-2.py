# Расчет факториала

def factorial(n):

    f = 1
    if n >= 1:
        f = n * factorial(n-1)
    
    return f
    #return n * factorial(n-1) if n > 1 else 1


print(f'Facrotial: {factorial(5)}')