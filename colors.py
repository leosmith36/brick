from enum import Enum

class Color(Enum):
    RED = (255,0,0,255)
    BLACK = (0,0,0,255)
    WHITE = (255,255,255,255)
    BLUE = (0,0,255,255)
    GREEN = (0,255,0,255)
    CLEAR = (0,0,0,0)