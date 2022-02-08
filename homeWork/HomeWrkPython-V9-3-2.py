# Сортировка файлов по директориям и вывод результата в консоль

import logging
from datetime import datetime
from pathlib import Path

dt_start = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

logging.basicConfig(
    filename="homeWork\logs\chaned_"+dt_start+".log", 
    level=logging.INFO
)

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
    

for file in cd.iterdir():
    if not file.is_dir():
        l_file.append(file.name)
        l_year.append(int(file.name[0:4]))
        l_month.append(int(symbol(file.name[5:7])))
        del_file = cd / f'{file.name}'
        del_file.unlink()  

l_year = unique(l_year)
l_month = unique(l_month)
l_month.sort()
l_year.sort()
l_file.sort()
#print(l_file)
#print(l_year)
#print(l_month)
log_scheme = f'.'
log_scheme = log_scheme + f'\n|---directory'
#print('|---directory')
for sort_dir in l_year:
    log_scheme = log_scheme + f'\n|   |---{sort_dir}'
    #print(f'|   |---{sort_dir}')
    cd_dir = cd / f'{sort_dir}' 
    cd_dir.mkdir(exist_ok=True)
    for sort_subdir in l_month:
        #print(str(sort_dir)+'-'+str(sort_subdir), len(str(sort_dir)+'-'+str(sort_subdir)))
        fileTXT = str(sort_dir)+'-'+str(sort_subdir)+'-'
        lenFile = len(fileTXT)
        #listFile(fileTXT, lenFile, l_file)
        if listFile(fileTXT, lenFile, l_file) is True:
            log_scheme = log_scheme + f'\n|   |   |---{sort_subdir}'
            #print(f'|   |   |---{sort_subdir}')
            cd_subdir = cd_dir / f'{sort_subdir}' 
            cd_subdir.mkdir(exist_ok=True)
            for sort_file in l_file:
                if sort_file[0:lenFile] == fileTXT:
                    log_scheme = log_scheme + f'\n|   |   |   |---{sort_file[lenFile:]}'
                    #print(f'|   |   |   |---{sort_file[lenFile:]}')
                    cd_file = cd_subdir / f'{sort_file[lenFile:]}' 
                    cd_file.touch()
#print('|'+'-'*12)
log_scheme = log_scheme + '\n|'+'-'*12

dt_finish = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

print(f'Finished change file in directory {str(cd)}')

logging.debug("The application is running in debug mode")
logging.info(f"Informational message"
             f"\nStart: {dt_start}"
             f"\nList file:"
             f"\n{l_file}"
             f"\nScheme:"
             f"\n{log_scheme}"
             f"\nUpdated: Created Dir and File to directory: {str(cd)}"
             f"\nFinished: {dt_finish}")
#logging.error("An error has occurred in the application!")


#End