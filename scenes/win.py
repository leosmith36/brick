import pygame

from scene import Scene
from objects import Text
from window import Window
from colors import Color
from fonts import Font

class Win(Scene):
    def __init__(self, game):
        super().__init__(game, Color.WHITE)
        win_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "WINNER", Font.FONT1, center = True)
        self.objects.append(win_text)
        self.time = pygame.time.get_ticks()
        

    def update(self):
        newtime = pygame.time.get_ticks()
        diff = (newtime - self.time) / 1000
        if diff >= 3:
            self.game.exit()
        super().update()
