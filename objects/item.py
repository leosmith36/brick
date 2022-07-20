from object import Object
from .brick import Brick
from colors import Color

class Item(Object):
    WIDTH = 25
    HEIGHT = 25
    def __init__(self, scene, x, y, color, function, speed, center = False, image = None):
        self.function = function
        self.speed = speed
        super().__init__(scene, x + Brick.WIDTH // 2, y + Brick.HEIGHT // 2, self.WIDTH, self.HEIGHT, color, center, image, visible = False)
    def tick(self):
        self.y += self.speed
    def activate(self):
        self.function()
        self.remove()