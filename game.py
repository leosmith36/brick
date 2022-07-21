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
        self.closed = False
        self.paused = False
        self.elapsed_time = 0

    def update(self):
        self.clock.tick(Game.FPS)
        if not self.paused:
            self.scene.update()
            self.elapsed_time += self.clock.get_time()
        self.scene.render(self.win)
        pygame.display.update()

    def trigger(self, event):
        self.scene.trigger(event)

    def change_scene(self, new_scene):
        self.paused = False
        self.scene = new_scene

    def next_level(self):
        self.level += 1
        if self.level <= len(Levels.LEVEL_LIST):
            self.load_level(self.level, True)
        else:
            self.change_scene(Win(self))

    def load_level(self, level, consecutive):
        self.change_scene(Level(self, level, consecutive))

    def choose_level(self):
        self.change_scene(Choose(self))

    def restart(self):
        self.change_scene(Start(self))
        self.level = -1

    def fail(self):
        self.change_scene(Fail(self))
    
    def is_closed(self):
        return self.closed

    def close(self):
        self.closed = True

    @property
    def time(self):
        return self.elapsed_time

    @property
    def paused(self):
        return self._paused

    @paused.setter
    def paused(self,paused):
        self._paused = paused

    def pause(self):
        if self.paused:
            self.paused = False
        else:
            self.paused = True

    @property
    def scene(self):
        return self.scene

    @scene.setter
    def scene(self, scene):
        self._scene = scene


