import pygame

from circle import Circle

class Trail(Circle):
    def __init__(self, scene, x, y, rad, color, image = None):
        super().__init__(scene, x, y, rad, color, image = image)
        self.time = pygame.time.get_ticks()
        self.rad_0 = rad
        self.color_0 = color

    def update(self):
        newtime = pygame.time.get_ticks()
        diff = 1 - (abs(newtime - self.time) / 300)
        if diff <= 0:
            diff = 0
            self.remove()
        self.rad = self.rad_0 * diff
        alpha = int(255 * diff)
        color = list(self.color)
        color[3] = alpha
        self.color = tuple(color)
        
