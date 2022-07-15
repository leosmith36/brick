import pygame

from object import Object

class Text(Object):
    def __init__(self, scene, x, y, color, text, font, center = False, timer = None):
        self.text = text
        self.font = font
        self.text_surface = self.font.render(text, 1, color)
        self.time = pygame.time.get_ticks()
        self.timer = timer
        super().__init__(scene, x, y, self.text_surface.get_width(), self.text_surface.get_height(), 0, (0,0,0,255), center)
    def update(self):
        if self.timer:
            time = pygame.time.get_ticks()
            diff = abs(time - self.time) / 1000
            if diff >= self.timer:
                self.removed = True
    def render(self, win):
        win.blit(self.text_surface, (self.x,self.y))