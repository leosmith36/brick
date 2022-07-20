import pygame
import re

from object import Object
from colors import Color

class Text(Object):
    def __init__(self, scene, x, y, color, text, font, center = False, timer = None, value = None):
        
        if value and "val" in text:
            self._value = value
            self._text = re.sub("val", str(value), text)
        else:
            self._value = None
            self._text = text
        self.text_0 = text
        self.font = font.value
        self.text_surface = self.font.render(self.text, 1, color.value)
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
        if not self.visible:
            return
        win.blit(self.text_surface, (self.x,self.y))
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, text):
        self._text = text

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
        self.text = re.sub("val", str(value), self.text_0)
        self.text_surface = self.font.render(self.text, 1, self.color)