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
        "0"*10,
        "0"*10,
        "",
        "",
        "0"*10,
        "0"*10,
        "",
        "",
        "1"*10
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

    LEVEL_3 = [
        "",
        "",
        "",
        "",
        "",
        "4"*10
    ]


    # LEVELS = [LEVEL_0]
    LEVEL_LIST = [
        # [LEVEL_0, "stone.png"],
        [LEVEL_1, "stone.png"],
        [LEVEL_2, "stone.png"],
        [LEVEL_3, "stone.png"]
    ]
    BRICKS = {
        "0" : [1, Color.GREEN, None],
        "1" : [2, Color.YELLOW, None],
        "2" : [3, Color.RED, None],
        "3" : [1, Color.GREEN, lambda scene, x, y : Item(scene, x, y, Color.CLEAR, lambda : scene.long_bar(), 2, center = True, image = os.path.join("images", "plus.png")), 0.1],
        "4" : [1, Color.YELLOW, lambda scene, x, y : Item(scene, x, y, Color.CLEAR, lambda : scene.fast_bar(), 3, center = True, image = os.path.join("images","speed.png")), 0.2],
        "5" : [1, Color.RED, lambda scene, x, y : Item(scene, x, y, Color.CLEAR, lambda : scene.slow_ball(), 4, center = True, image = os.path.join("images","slow.png")), 0.3]
    }

    @classmethod
    def make_level(cls, level, scene):
        new_level = cls.LEVEL_LIST[level][0]
        image = os.path.join("images",cls.LEVEL_LIST[level][1])
        vert_spacing = 1
        horiz_spacing = 1
        y = 0
        x = 0
        bricks = []
        for row in new_level:
            for item in row:
                if not item == "_":
                    props = cls.BRICKS[item]
                    if props[2]:
                        bricks.append(Brick(scene, x,y,props[1], props[0], props[2](scene, x, y), props[3]))
                    else:
                        bricks.append(Brick(scene, x,y,props[1], props[0]))
                x += Brick.WIDTH + horiz_spacing
            x = 0
            y += Brick.HEIGHT + vert_spacing
        return bricks, image
