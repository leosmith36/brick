import pygame

from window import Window
from scenes import Start, Level, Win
from levels import Levels

class Game():

    FPS = 60
    
    def __init__(self):
        self.window = Window()
        self.win = self.window.win
        self.scene = Start(self)
        self.clock = pygame.time.Clock()
        self.level = 0
        self._exited = False

    def update(self):
        self.scene.update()
        self.scene.render(self.win)
        pygame.display.update()
        self.clock.tick(Game.FPS)

    def click(self, event):
        self.scene.click(event)

    def change_scene(self, new_scene):
        self.scene = new_scene

    def next_level(self):
        self.level += 1
        if self.level <= len(Levels.LEVELS):
            self.change_scene(Level(self, self.level))
        else:
            self.change_scene(Win(self))
    
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def exited(self):
        return self._exited
    
    def exit(self):
        self._exited = True