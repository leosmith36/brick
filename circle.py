import pygame

from object import Object

class Circle(Object):
    def __init__(self, scene, x, y, rad, color, image = None):
        self.rad = rad
        self.rad_0 = rad
        super().__init__(scene, x, y, 2 * rad, 2 * rad, color, center = True, image = image)
    def render(self, win):
        self.surface = pygame.Surface((2 * self.rad_0, 2 * self.rad_0), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, self.color, (self.rad_0, self.rad_0), self.rad)
        win.blit(self.surface, self.rect)
    @property
    def rad(self):
        return self._rad
    @rad.setter
    def rad(self, rad):
        self._rad = rad