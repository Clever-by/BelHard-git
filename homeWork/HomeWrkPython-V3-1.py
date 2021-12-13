# *** Задание №1
# *** Программа получет на вход две строки и выводит на экран:

print("\n" + "Если 'Y' or 'y' - ручной ввод", "\n"+"Если 'N' or 'n' либо другой символ - значения поумолчанию")
strg = input("Выберите ввод данных: ")

if strg == 'Y' or strg == 'y':
    print("Введите две строки /n")
    
    
    S1 = input("Введите строку S1: ")
    S2 = input("Введите строку S2: ")

else:
    S1 = 'Python Developer is a part of a software team who skills in creating, designing, deploying computer applications, and different programs using the Python programming language'
    S2 = 'The Python Software Foundation is the organization behind Python. Become a member of the PSF and help advance the software and our mission'

print("Длина S1 = ", len(S1), '\n'+"Длина S2 = ", len(S2))
print("1-ый символ строки S1", S1[0])
print("n-ый символ строки S2", S2[-1])
print("Статус равенства S1иS2: ", S1 == S2)
print("Вхождение строки S1 в S2", S1 in S2)
print("Вхождение строки S2 в S1", S2 in S1)