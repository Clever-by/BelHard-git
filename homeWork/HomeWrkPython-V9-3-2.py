# Сортировка файлов для вывода консоль


from pathlib import Path

cd = Path('./homeWork/directory')
l_file = list()
l_year = list()
l_month = list()

def listFile(fileTXT, lenFile, listFile):
    for nameFile in listFile:
        if nameFile[0:lenFile] == fileTXT:
            return True        
        else: 
            continue
    
def unique(list_in):
    list_out = list(set(list_in))
    return list_out

def symbol(string):
    s_sym = string[1]
    if  s_sym == '-':
        rez = string[0]
    else: 
        rez = string    
    return rez
    

for child in cd.iterdir():
    if not child.is_dir():
        l_file.append(child.name)
        l_year.append(int(child.name[0:4]))
        l_month.append(int(symbol(child.name[5:7])))
           

l_year = unique(l_year)
l_month = unique(l_month)
l_month.sort()
l_year.sort()
l_file.sort()
#print(l_file)
#print(l_year)
#print(l_month)
print('.')
print('|---directory')
for sort_dir in l_year:
    print(f'|   |---{sort_dir}')
    for sort_subdir in l_month:
        #print(str(sort_dir)+'-'+str(sort_subdir), len(str(sort_dir)+'-'+str(sort_subdir)))
        fileTXT = str(sort_dir)+'-'+str(sort_subdir)
        lenFile = len(str(sort_dir)+'-'+str(sort_subdir))
        #listFile(fileTXT, lenFile, l_file)
        if listFile(fileTXT, lenFile, l_file) is True:
            print(f'|   |   |---{sort_subdir}')
            for sort_file in l_file:
                if sort_file[0:lenFile] == fileTXT:
                    print(f'|   |   |   |---{sort_file[lenFile+1:]}')
print('|'+'-'*12)
#End