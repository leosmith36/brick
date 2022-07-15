import pygame
import math
import random

from circle import Circle
from colors import Color
from window import Window
from .bar import Bar
from utils import clamp
from .trail import Trail

class Ball (Circle):
    RAD = 10
    SPEED = 5
    COLOR = Color.GREEN.value
    def __init__(self, scene):
        self.locked = True
        super().__init__(scene, Window.WIDTH // 2, Bar.START_Y - self.RAD, self.RAD, self.COLOR)
        self.vec = pygame.math.Vector2(0,self.SPEED)
        self.speed = self.SPEED
        # self.vec = self.vec.rotate_rad(random.uniform(-math.pi / 8, math.pi / 8))
    def update(self):
        if self.locked:
            mouse_pos = pygame.mouse.get_pos()
            self.centerx = mouse_pos[0]
            self.centerx = clamp(self.centerx, Bar.WIDTH // 2, Window.WIDTH - Bar.WIDTH // 2)
        else:
            self.vec.scale_to_length(self.speed)
            vx = self.vec.x
            vy = self.vec.y
            self.x -= vx
            self.y -= vy
            self.scene.add_object(Trail(self.scene, self.centerx, self.centery, self.rad, self.color))
    def reflect_vertical(self):
        self.vec.x *= -1
    def reflect_horizontal(self):
        self.vec.y *= -1
    def reflect_bar_top(self, bar_x):
        diff = self.centerx - bar_x
        self.vec = pygame.math.Vector2(0,self.speed).rotate_rad(diff / 50)
    def unlock(self):
        self.locked = False
