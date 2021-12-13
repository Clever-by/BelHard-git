# *** Данные в Python #

# *** Поиск в строке позиции символа и вхождение строк
# *** Замена в строке
# *** Вхождение строк
# *** Разделитель

s = 'string one length'
print(s.find('ring'))
print(s.rfind('str'))
print(s.find('tit'))

# *** Замена в строке
print(s.replace('one', 'two'))

# *** Вхождение строк
print('spr' not in 'Spam') # невхождение подстроки, True
print('spr' in 'Spam') # вхождение подстроки, False

# *** Разделитель
s = 'string one length'
print(s.split()) # Разделитель поумолчанию пробеил(' ')

st = input()
print(st.split(',')) # задаем разделитель свой запятая(',')

# End