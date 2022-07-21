import pygame

from scene import Scene
from objects import Text
from window import Window
from fonts import Font
from colors import Color

class Fail(Scene):
    def __init__(self, game):
        super().__init__(game, Color.WHITE)
        self.fail_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "GAME OVER", Font.FONT1, center = True)
        # self.objects.append(self.fail_text)
        self.frames = 0

    def update(self):
        self.frames += 1
        if self.frames >= 300:
            self.game.restart()
        super().update()

    