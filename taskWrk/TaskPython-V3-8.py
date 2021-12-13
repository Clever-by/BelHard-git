# *** Данные в Python #


# Сравнение в ящейке памяти

p_s1 = 'abcd'
p_s2 = 'abcd'
p_s3 = 'absd'
p_s4 = p_s3

# Сравнение значения в памяти
print(p_s1 is p_s2)
print(p_s2 is p_s3)
print(p_s4 is p_s3)

# Вывод ячеек памяти со значение
print(id(p_s1), id('abcd'), id(p_s3), id('absd'))


# End