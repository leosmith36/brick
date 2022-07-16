import pygame
import os

from window import Window
from scenes import Start, Level, Win, Choose, Fail
from levels import Levels

class Game():

    FPS = 60
    
    def __init__(self):
        self.window = Window()
        self.win = self.window.win
        self.scene = Start(self)
        self.clock = pygame.time.Clock()
        self.level = -1
        self._exited = False

    def update(self):
        self.scene.update()
        self.scene.render(self.win)
        pygame.display.update()
        self.clock.tick(Game.FPS)

    def trigger(self, event):
        self.scene.trigger(event)

    def change_scene(self, new_scene):
        self.scene = new_scene

    def next_level(self):
        self.level += 1
        if self.level <= len(Levels.LEVEL_LIST):
            self.load_level(self.level)
        else:
            self.change_scene(Win(self))

    def load_level(self, level):
        self.change_scene(Level(self, level))

    def choose_level(self):
        self.change_scene(Choose(self))
    
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

    def fail(self):
        self.change_scene(Fail(self))