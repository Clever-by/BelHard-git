# Генерация файлов

from pathlib import Path
from random import randint
import logging
from datetime import datetime

dt_start = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

logging.basicConfig(
    filename="homeWork\logs\inform_"+dt_start+".log", 
    level=logging.INFO
)

cd = Path('./homeWork/directory')
cd.mkdir(exist_ok=True)

for i in range(10):
    cd_file = cd / (f'{randint(2020, 2022)}-'
                    f'{randint(1, 12)}-'
                    f'{randint(1, 31)}.txt'
                    )
    
    cd_file.touch()

dt_finish = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")

logging.info(f"Informational message\nStart: {dt_start} \nImported file to directory: {str(cd)} \nStop: {dt_finish}")


#End