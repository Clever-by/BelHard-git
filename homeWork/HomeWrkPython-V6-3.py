# Декоратор Inspect:


list_in = input("Введите список через пробел или нажмите 'Ввод': ")

if list_in == '':
    list_add = ['Far', 'Alisa', 'Genrih', 'Bill', 'Filip', 'Caddy', 'Jolie']
    
else:
    list_add = list_in.split()


def inspect(function):
    def wrapper(str, key=True):
        print(f'входные параметры str: {str}, key: {key}')
        rez_func = function(str, key)
        print(f'выходные параметры функции: {rez_func}')
        return 'End'
    
    return wrapper
    
@inspect
def contact(list_in, reversed=True):
    
    if reversed is True:
        list_in.reverse()
        
    list_st = ''
    for st in list_in:
        list_st += st + ' '
    
    return list_st

#contact = inspect(contact)
#print(inspect(contact)(list_add))
print(contact(list_add, False))