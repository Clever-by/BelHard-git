
int_str = input('Введите строку из чисел: ')
int_str = (int_str.split())
print(list(enumerate(int_str,1)))

l_a = list(int_str)
a = [item for i, item in list(enumerate(int_str,1)) if i == 1]
b = [item for i, item in list(enumerate(int_str,1)) if i == 2]

p_a = a[0]

print(a, l_a, p_a)
print(b)

