import pygame

from object import Object
from .text import Text

class Button(Object):
    def __init__(self, scene, x, y, w, h, color, function, text, text_color, text_font, center = False, key = None):
        super().__init__(scene, x, y, w, h, color, center = center)
        self.function = function
        self.key = key
        self.text = Text(scene, self.centerx, self.centery, text_color, text, text_font, center = True)
    def activate(self):
        self.function()
    def hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
    def trigger(self, event):
        if self.hovering():
            self.alpha = 100
        else:
            self.alpha = 255
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovering():
                self.activate()
        elif event.type == pygame.KEYDOWN:
            if event.key == self.key:
                self.activate()
    def tick(self):
        pass
    def render(self, win):
        super().render(win)
        self.text.render(win)

        
