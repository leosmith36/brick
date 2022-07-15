import os

from scene import Scene
from colors import Color
from objects import Button
from window import Window
from fonts import Font

class Start(Scene):

    def __init__(self, game):
        self.objects = [
            Button(self, Window.WIDTH // 2, Window.HEIGHT // 2, 200, 50, Color.RED.value, lambda : game.next_level(), "PLAY", Color.BLACK.value, Font.FONT1.value, center = True)
        ]
        super().__init__(game)

    def render(self, win):
        win.fill(Color.WHITE.value)
        super().render(win)