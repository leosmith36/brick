import os

from scene import Scene
from colors import Color
from objects import Button
from window import Window
from fonts import Font

class Start(Scene):

    def __init__(self, game):
        self.objects = [
            Button(self, Window.WIDTH // 2, Window.HEIGHT // 2, 200, 50, Color.RED, lambda : game.next_level(), "PLAY", Color.BLACK, Font.FONT1, center = True)
        ]
        super().__init__(game, Color.WHITE)
