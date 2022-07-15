import os

from objects import Brick
from colors import Color
from window import Window
from objects import Item

class Levels():

    LEVEL_0 = [
        "0"
    ]

    LEVEL_1 = [
        "",
        "",
        "0000000000",
        "",
        "",
        "0000000000",
        "",
        "",
        "0000000000",
        "",
        "",
        "1111331111"
    ]

    LEVEL_2 = [
        "",
        "",
        "",
        "",
        "",
        "0000000000",
        "1111221111",
        "1122222211",
        "1111221111",
        "0000000000"

    ]



    LEVELS = [LEVEL_1, LEVEL_2]
    BRICKS = {
        "0" : [1, Color.RED.value, None],
        "1" : [2, Color.GREEN.value, None],
        "2" : [3, Color.BLUE.value, None],
        "3" : [1, Color.BLACK.value, lambda scene, x, y : Item(scene, x, y, Color.RED.value, lambda : scene.long_bar(), 2, center = True), 0.5]
    }

    @classmethod
    def make_level(cls, level, scene):
        new_level = cls.LEVELS[level - 1]
        vert_spacing = 1
        horiz_spacing = 1
        y = 0
        x = 0
        bricks = []
        for row in new_level:
            for item in row:
                props = cls.BRICKS[item]
                if props[2]:
                    bricks.append(Brick(scene, x,y,props[1], props[0], props[2](scene, x, y), props[3]))
                else:
                    bricks.append(Brick(scene, x,y,props[1], props[0]))
                x += Brick.WIDTH + horiz_spacing
            x = 0
            y += Brick.HEIGHT + vert_spacing
        return bricks
