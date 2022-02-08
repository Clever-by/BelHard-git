# Удаление файлов из директории

import logging
from datetime import datetime
from pathlib import Path

def fDelete():

    dt_start = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

    logging.basicConfig(
        filename="homeWork\logs\deleted_"+dt_start+".log", 
        level=logging.INFO
    )

    def cdDel(cd):
    
        log_del = '\n'+'-'*16
        for file in cd.iterdir():
            if not file.is_dir():
                del_file = cd / f'{file.name}'
                del_file.unlink()
                log_del = log_del + f'\nA file {file.name} has been deleted from the directory {str(cd)}'
                #print(f'A file {file.name} has been deleted from the directory {str(cd)}')
        
            else:
                del_dir = cd / f'{file.name}'
                log_del = log_del + f'\nDirectory {file.name} in {str(del_dir)}'
                #print(f'Directory {file.name} in {str(del_dir)}')
                l_file = list()
                for dir in del_dir.iterdir():
                    if str(dir.name) is not None:
                        l_file.append(dir)
            
                log_del = log_del + f'\nIn the file {len(l_file)} directory {str(del_dir)}'
                #print(f'In the file {len(l_file)} directory {str(del_dir)}')
        
                if len(l_file) == 0:
                    #print(f'There are no files in the directory {str(file.name)}')
                    del_dir.rmdir()
                    log_del = log_del + f'\nDeleting a directory {str(del_dir)}'
                    #print(f'Deleting a directory {str(del_dir)}')
                
                else:
                    #print(f'There are files in the directory {str(file.name)}')
                    cd_old = cd
                    cd = del_dir
                    log_del = log_del + cdDel(cd)
                    cd = cd_old
                    del_dir.rmdir()
                    log_del = log_del + f'\nDeleting a directory {str(del_dir)}'
                    #print(f'Deleting a directory {str(del_dir)}')
    
        return log_del
    
    
    cd = Path('./homeWork/directory')
    log_del = cdDel(cd)

    dt_finish = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

    print(f'Finished delte file and dir in directory {str(cd)}')

    logging.debug("The application is running in debug mode")
    logging.info(f"Informational message"
                f"\nStart: {dt_start}"
                f"\nDeleted Dir and File in directory: {str(cd)}"
                f"\n{log_del}"
                f"\nFinished: {dt_finish}")
    #logging.error("An error has occurred in the application!")


#End