# Случайно выбирает какую вам купить игрушку для ёлки ( enum + random ) с двумя параметрами

import argparse
from enum import Enum
import random

class Toys(Enum):

    BALL = 'Ball'
    ANGEL = 'Angel'
    STAR = 'Asterisk'
    BOX = 'Box'
    
    decorations = ['BALL', 'ANGEL', 'STAR', 'BOX']

class Colors(Enum):
    
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'
    WHITE = 'White'
    YELLOW = 'Yellow'

    color_palette = ['RED', 'GREEN', 'BLUE', 'WHITE', 'YELLOW']

parser = argparse.ArgumentParser(description='Selection of Christmas decorations')
parser.add_argument('-a', '--action', type=str, default='Y', help='Action')
args = parser.parse_args()

print(f'action={args.action}')

#Запускать через командную строку из директории, где лежит файл:

# python .\HomeWrkPython-V9-2.py --help
# python .\HomeWrkPython-V9-2.py -h
# a - опционально
# python .\HomeWrkPython-V9-2.py -a Y
# Y - 'Вешаем игрушку', 
# N - 'Не сегодня' 

def makingAction(action):
    if action == 'Y':
        count_toys = len(Toys.decorations.value)
        count_colors = len(Colors.color_palette.value) 
        #print(f'выбор новоголних украшений: {count_toys}, с количеством цветов: {count_colors}')

        toy = Toys.decorations.value[random.randint(0,count_toys-1)]
        color =(Colors.color_palette.value[random.randint(0,count_colors-1)])
        
        return f'{Toys[toy].value} {Colors[color].value}'
    
    else:
        return f'Выбор сделаем следуюший раз'

print(makingAction(args.action))

