# *** Lambda

# Лямбда - это краткая, неименованная функция

# Задаем List
a = [(1,3), (5,2), (0,10)]

# Сортируем список по первому [0] или второму улементу [1]
a.sort(key=lambda item: item[0])

print(f"Отсортированный список: {a}")

# End