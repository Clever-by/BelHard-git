# enum

#Enum - это множество символических имён

#import enum
from enum import Enum

class Color(Enum):
    RED = '#f00'
    GREEN = '#0f0'
    BLUE = '#00f'

print(type(Color))
print(type(Color.RED))
print(Color.RED)
print(Color.RED.value)

class Region:
    R1 = 'Brest'
    R2 = 'Vitebsk'
    R3 = 'Gomel'
    R4 = 'Grodno'
    R5 = 'Minsk'
    R6 = 'Mogilev'
    
print(type(Region))
print(type(Region.R2))
print(Region.R2)


# End