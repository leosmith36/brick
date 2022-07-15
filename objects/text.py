import pygame

from object import Object
from colors import Color

class Text(Object):
    def __init__(self, scene, x, y, color, text, font, center = False, timer = None):
        self.text = text
        self.font = font.value
        self.text_surface = self.font.render(text, 1, color.value)
        self.time = pygame.time.get_ticks()
        self.timer = timer
        super().__init__(scene, x, y, self.text_surface.get_width(), self.text_surface.get_height(), Color.CLEAR, center)
    def tick(self):
        if self.timer:
            time = pygame.time.get_ticks()
            diff = abs(time - self.time) / 1000
            if diff >= self.timer:
                self.removed = True
    def render(self, win):
        win.blit(self.text_surface, (self.x,self.y))