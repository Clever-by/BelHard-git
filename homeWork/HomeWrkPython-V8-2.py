# Функция Factorial:


def f(n):
    res = 1
    for num in range(1, n+1):
        res *= num

    return res


print(f'Facrotial: {f(5)}')


# Расчет факториалф через рекурсию

def factorial(n):
    #if n == 1:
        #return n
    return n * factorial(n-1) if n > 1 else 1

print(f'Facrotial: {factorial(6)}')