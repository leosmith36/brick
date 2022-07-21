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
        self.time = game.time

    def update(self):
        newtime = self.game.time
        diff = (newtime - self.time) / 1000
        if diff >= 3:
            self.game.restart()
        super().update()

    