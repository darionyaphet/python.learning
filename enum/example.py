from enum import Enum

class Color(Enum):
    red  = 1
    green= 2
    blue = 3

for color in Color:
    print(color.name+'\t'+str(color.value))
