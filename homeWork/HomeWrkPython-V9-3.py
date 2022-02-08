# Написать программу, которая упорядочивает файлы в директории по следующему принципу:
# Символ "-" должен стать символом "/" в пути к файлу. 
# Использовалось: pathlib, logging, datetime, random, argparse, re 
# Импорт из директории lesson9(load, change, delete).

from lesson9.load import fLoad as fun_load
from lesson9.change import fChange as fun_change
from lesson9.delete import fDelete as fun_del
import logging
from datetime import datetime
from pathlib import Path
import argparse


class DelLog:

    def Del():
        dt_start = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

        def cdDel(cd):
    
            log_del = '\n'+'-'*16
            for file in cd.iterdir():
                if not file.is_dir():
                    del_file = cd / f'{file.name}'
                    del_file.unlink()
                    log_del = log_del + f'\nA file {file.name} has been deleted from the directory {str(cd)}'
                    #print(f'A file {file.name} has been deleted from the directory {str(cd)}')
   
            return log_del
    
    
        cd = Path('./homeWork/logs')
        log_del = cdDel(cd)

        logging.basicConfig(
            filename="homeWork\logs\log_del_"+dt_start+".log", 
            level=logging.INFO
        )

        dt_finish = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

        print(f'Finished delte logs in directory {str(cd)}')

        logging.debug("The application is running in debug mode")
        logging.info(f"Informational message"
                    f"\nStart: {dt_start}"
                    f"\nDeleted logs in directory: {str(cd)}"
                    f"\n{log_del}"
                    f"\nFinished: {dt_finish}")
        #logging.error("An error has occurred in the application!")


parser = argparse.ArgumentParser(description='Changing files in a directory')
parser.add_argument('-n', '--number', type=str, default='10', help='Action number')
args = parser.parse_args()

# Запускать через командную строку:

# python .\homework\HomeWrkPython-V9-3.py --help
# python .\homework\HomeWrkPython-V9-3.py -h
# python .\homework\HomeWrkPython-V9-3.py -n '10'
# n - опционально
# "1" - Загрузка файлов,
# "2" - Изменение фалов в директории,
# "3" - Очистка директории от файлов,
# "0" - Удалить логи

print(f'Action number={args.number}')
num = args.number

print("1 - Загрузка файлов\n"
      "2 - Изменение фалов в директории\n"
      "3 - Очистка директории от файлов\n"
      "0 - Удалить логи")

if num is None or num == '10':
    num = input(f'Выберите вариант: ')

if num == '1':
    fun_load()

elif num == '2':
    fun_change()

elif num == '3':

    fun_del()

elif num == '0':
    DelLog.Del()

else:
    print("Внимательно прочитайте и введите верный вариант")
    

#End