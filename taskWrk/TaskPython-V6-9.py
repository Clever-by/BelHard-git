# *** Рекурсия

# Рекурсия - способность функции вызывать саму себя

def factorial(n):
    #if n == 1:
        #return n
    return n * factorial(n-1) if n > 1 else 1

print(factorial(6))

# Если слишком большая вложенность, будет ошибка "RecursionError"

def f(n):
    res = 1
    for num in range(1, n+1):
        res += num
    return res


print(f(5))

# End