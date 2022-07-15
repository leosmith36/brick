import pygame

from scene import Scene
from objects import Text
from window import Window
from fonts import Font
from colors import Color

class Fail(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.fail_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "GAME OVER", Font.FONT1, center = True)
        self.objects = [self.fail_text]
        self.time = pygame.time.get_ticks()

    def update(self):
        newtime = pygame.time.get_ticks()
        diff = (newtime - self.time) * 1000
        if diff >= 5:
            self.game.exit()
        super().update()

    def render(self, win):
        win.fill(Color.WHITE.value)
        super().render(win)

    