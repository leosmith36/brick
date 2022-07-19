import pygame
import math
import random
import os

from circle import Circle
from colors import Color
from window import Window
from .bar import Bar
from utils import clamp, collides_bottom, collides_top, collides_right, collides_left
from .trail import Trail

class Ball (Circle):
    RAD = 10
    SPEED = 5
    COLOR = Color.ORANGE
    def __init__(self, scene):
        self.locked = True
        super().__init__(scene, Window.WIDTH // 2, Bar.START_Y - self.RAD, self.RAD, self.COLOR)
        self.vec = pygame.math.Vector2(0,self.SPEED)
        self.speed = self.SPEED
        self.sound = pygame.mixer.Sound(os.path.join("sounds","hit1.mp3"))
        self.hit_bar = False
        self.vec = self.vec.rotate_rad(random.uniform(-math.pi / 8, math.pi / 8))
        self.centerx = self.scene.bar.centerx
    def tick(self):
        if self.locked:
            # mouse_pos = pygame.mouse.get_pos()
            # self.centerx = mouse_pos[0]
            self.control()
            self.centerx = clamp(self.centerx, Bar.WIDTH // 2, Window.WIDTH - Bar.WIDTH // 2)
        else:
            self.check_bounds()
            self.vec.scale_to_length(self.speed)
            vx = self.vec.x
            vy = self.vec.y
            self.x -= vx
            self.y -= vy
            self.scene.add_object(Trail(self.scene, self.centerx, self.centery, self.rad, self.color_key))
    def reflect_vertical(self):
        self.vec.x *= -1
        self.sound.play()
    def reflect_horizontal(self):
        self.vec.y *= -1
        self.sound.play()
    def reflect_bar_top(self, bar_x):
        diff = self.centerx - bar_x
        self.vec = pygame.math.Vector2(0,self.speed).rotate_rad(diff / 50)
        self.sound.play()
    def unlock(self):
        self.locked = False
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.scene.bar.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.scene.bar.speed
    def check_collisions(self, object):
        if collides_bottom(self, object) or collides_top(self, object):
            self.reflect_horizontal()
        elif collides_left(self, object) or collides_right(self, object):
            self.reflect_vertical()
        else:
            return False
        self.hit_bar = False
        return True
    def check_bar(self, object):
        if collides_bottom(self, object) or collides_top(self, object):
            self.reflect_bar_top(object.centerx)
        elif collides_left(self, object) or collides_right(self, object) or self.rect.colliderect(object.rect):
            if self.hit_bar:
                if self.centerx < object.centerx:
                    self.x -= self.scene.bar.speed
                    # self.vec.x += 1
                    # self.vec.scale_to_length(self.speed)
                if self.centerx > object.centerx:
                    self.x += self.scene.bar.speed
                    # self.vec.x -= 1
                    # self.vec.scale_to_length(self.speed)
            else:
                self.reflect_vertical()
        else:
            return
        self.hit_bar = True
    def check_bounds(self):
        if self.rect.top - self.vec.y < 0:
            self.reflect_horizontal()
        elif self.rect.right - self.vec.x > Window.WIDTH or self.rect.left - self.vec.x < 0:
            self.reflect_vertical()
        elif self.rect.top >= Window.HEIGHT:
            self.scene.fail()
            self.remove()
        else:
            return
        self.hit_bar = False

