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
        "1"*10,
        "",
        "",
        "2"*10,
        "",
        "",
        "1"*10,
        "",
        "",
        "2"*10
    ]

    LEVEL_2 = [
        "",
        "",
        "",
        "",
        "",
        "0"*10,
        "1"*10,
        "1"*4 + "3"*2 + "1"*4,
        "1"*10,
        "0"*10

    ]


    # LEVELS = [LEVEL_0]
    LEVELS = {
        "stone.png" : LEVEL_0,
        "stone.png" : LEVEL_1
    }
    BRICKS = {
        "0" : [1, Color.RED, None],
        "1" : [2, Color.GREEN, None],
        "2" : [3, Color.BLUE, None],
        "3" : [1, Color.RED, lambda scene, x, y : Item(scene, x, y, Color.YELLOW, lambda : scene.long_bar(), 2, center = True), 0.5]
    }

    @classmethod
    def make_level(cls, level, scene):
        images = list(cls.LEVELS.keys())
        collection = list(cls.LEVELS.values())
        new_level = collection[level - 1]
        image = os.path.join("images",images[level - 1])
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
        return bricks, image
