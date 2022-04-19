from typing import Union

import tcod
from tcod import Color, Console


class Entity:
    def __init__(self,char, color):
        self.x = -1
        self.y = -1
        self.char = char
        self.color = color

    def set_position(self,x,y):
        self.x = int(x)
        self.y = int(y)
        return self
