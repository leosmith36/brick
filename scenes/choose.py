from scene import Scene
from colors import Color
from levels import Levels
from .level import Level
from objects import Button
from window import Window
from fonts import Font

class Choose(Scene):
    def __init__(self, game):
        super().__init__(game, Color.WHITE)
        y = 100
        for i in range(len(Levels.LEVEL_LIST)):
            self.objects.append(
                Button(
                    self,
                    Window.WIDTH // 2,
                    y,
                    200,
                    50,
                    Color.BLUE,
                    lambda num = i : self.game.change_scene(Level(self.game, num, False)),
                    f"LEVEL {i + 1}",
                    Color.BLACK,
                    Font.FONT1,
                    center = True
                )
            )
            y += 60        