import pygame

from circle import Circle

class Trail(Circle):
    def __init__(self, scene, x, y, rad, color, image = None):
        super().__init__(scene, x, y, rad, color, image = image)
        self.rad_0 = rad
        self.color_0 = color
        self.frame = 0
        self.max_frames = 20
    def tick(self):
        self.frame += 1
        diff = (self.max_frames - self.frame) / self.max_frames
        if diff <= 0:
            diff = 0
            self.remove()
        self.rad = self.rad_0 * diff
        alpha = int(255 * diff)
        color = list(self.color)
        color[3] = alpha
        self.color = tuple(color)
        
