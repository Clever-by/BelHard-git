# *** Генератор

# Генератор — это объект, который сразу при создании не вычисляет значения всех своих элементов.

#squads = [num**2 for num in range(100)]

def squads():
    for num in range(10):
        element = num**2
        # Генератор - ключевое слово "yield"
        yield element
        print("next:", (num+1)**2)

# Выполнение значения по ключу генератора
for num in squads():
        print("element:", num)

# *** Второй вариант задать второй вариант:
gen = (num**2 for num in range(100))
for num in gen:
    print("element: ", num)

# End