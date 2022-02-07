# Удаление файлов из директории


from pathlib import Path

def cdDel(cd):
    
    for file in cd.iterdir():
        if not file.is_dir():
            del_file = cd / f'{file.name}'
            del_file.unlink()
        else:    
            del_dir = cd / f'{file.name}'
            #print(f'Директория {file.name}, {del_dir}')
            l_file = list()
        
            for dir in del_dir.iterdir():
                if str(dir.name) is not None:
                    l_file.append(dir)
        
            #print(f'В директории {del_dir} файлов {len(l_file)}')
        
            if len(l_file) == 0:
                #print(f'Директория {file.name} пустая')
                del_dir.rmdir()
            else:
                #print(f'Директория {file.name} не пустая')
                cd_old = cd
                cd = del_dir
                cdDel(cd)
                cd = cd_old
                del_dir.rmdir()
    
    
    
cd = Path('./homeWork/directory')
cdDel(cd)


#End