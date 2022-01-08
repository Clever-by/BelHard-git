# *** Внутренние функции, замыкания

# nonlocal - обращение к родительскому замыканию
# global - глобальное замыкание

x = 5

def f1():
    x = 1
    print("Функция-1 =", x)
    def f2():
        nonlocal x
        #global x
        x = 2
        y = x
        print("Функция-2 =", x)
        return y
    print("Функция-2 =", f2())
    return x

print("Global =", x)
print("Функция-1 =", f1())
print("После выполнения Функции-2 Global =", x)

# End