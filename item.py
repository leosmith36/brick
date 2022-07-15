from object import Object

class Item(Object):
    WIDTH = 50
    HEIGHT = 50
    def __init__(self, x, y, color, function, image = None):
        super().__init__(x, y, self.WIDTH, self.HEIGHT, color, image = image)
        self.function = function
    def activate(self):
        self.function()