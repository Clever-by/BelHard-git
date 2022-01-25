import random

from towel import Towel
from colors import Colors


def pipe():
    while True:
        yield Towel(
            length = random.randint(1, 8),
            color = random.choice(list(Colors)))       

#print(pipe())
#print(Towel(45, 'Grey').length)