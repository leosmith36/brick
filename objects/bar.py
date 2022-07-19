import pygame
import os

from object import Object
from utils import clamp
from window import Window
from colors import Color

class Bar (Object):
    WIDTH = 100
    HEIGHT = 25
    SPEED = 6
    START_Y = Window.HEIGHT - 100 - HEIGHT // 2
    def __init__(self, scene):
        self.speed = self.SPEED
        super().__init__(scene, Window.WIDTH // 2, Window.HEIGHT - 100, self.WIDTH, self.HEIGHT, Color.GREEN, center = True, image = os.path.join("images","bar.png"))
    def tick(self):
        # self.centerx = pygame.mouse.get_pos()[0]
        self.control()
        self.x = clamp(self.x, 0, Window.WIDTH - self.w)
    def long_bar(self):
        self.Effect(self, lambda parent : setattr(parent, "w", parent.WIDTH * 1.5), lambda parent : setattr(parent, "w", parent.WIDTH), 300)
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed


