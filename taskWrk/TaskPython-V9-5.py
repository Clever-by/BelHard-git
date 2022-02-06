# SYS

import sys

#sys.version - версия python
print(sys.version)

#sys.stdin - стандартный ввод
print(sys.stdin)

#sys.stdout - стандартный вывод
print(sys.stdout)

#sys.getsizeof(object[, default]) - возвращает размер объекта (в байтах)
print(f"Размер строки: {sys.getsizeof('Размер строки')}")

#sys.exit([arg]) - выход из Python
a1 = [3, 5, 9]
b1 = [2, 4, 7]

a2 = [3, 5, 9]
b2 = [3, 5, 9, 11]

print(list(zip(a1, b1)))

if len(a2) != len(b2):
    print('Error: length (a2&b2) are different')
    #sys.exit(1)
    

#sys.argv - список аргументов командной строки, передаваемых сценарию Python
#print(sys.argv)
#i = [1,2,3,4,5]
print(sum(int(i) for i in sys.argv[1:]))


# End