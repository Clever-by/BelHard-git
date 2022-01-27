# Функция contact:

list_in = input("Введите список через пробел или нажмите 'Ввод': ")

if list_in == '':
    list_add = ['Far', 'Alisa', 'Genrih', 'Bill', 'Filip', 'Caddy', 'Jolie']
    
else:
    list_add = list_in.split()


def contact(list_in, reversed=True):
    
    if reversed is True:
        list_in.reverse()
        
    list_st = ''
    for st in list_in:
        list_st += st + ' '
    
    return list_st

print(contact(list_add))