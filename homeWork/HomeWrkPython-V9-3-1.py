# Написать программу, которая упорядочивает файлы в директории по следующему принципу:
#Символ "-" должен стать символом "/"" в пути к файлу (pathlib).

from pathlib import Path
from random import randint

Path('./homeWork/directory').mkdir(exist_ok=True)

for i in range(10):
    Path(f'./homeWork/directory/'
        f'{randint(2020, 2022)}-'
        f'{randint(1, 12)}-'
        f'{randint(1, 31)}.txt'
    ).touch()


#End