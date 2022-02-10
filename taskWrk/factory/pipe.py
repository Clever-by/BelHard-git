import random

#"""
# Есть доступ с внешнего файла TaskPython-V9-1.py
from .towel import Towel
from .colors import Colors
# Но не работает, если обратиться на прямую
#"""

"""
# Работает, если обратиться на прямую
#Var.1
#import towel
#import colors
#Var.2
from towel import Towel
from colors import Colors
# Не отработывает, если обратиться с внешнего файла TaskPython-V9-1.py
"""

def pipe():
    while True:
        yield Towel(
            length = random.randint(1, 8),
            color = random.choice(list(Colors))
        )
        

print(pipe())
#print(Towel(45, 'Grey').length)

