import pygame
import os
import random

from object import Object

class Brick (Object):
    WIDTH = 50
    HEIGHT = 25
    def __init__(self, scene, x, y, color, max_hits, item = None, chance = 1):
        super().__init__(scene, x, y, 50, 25, color, image = os.path.join("images","brick_blank.png"))
        self.hits = 0
        self.max_hits = max_hits
        self.broken = False
        self.item = item
        self.chance = chance
    def tick(self):
        if self.hits >= self.max_hits:
            self.remove()
            if self.item and random.random() < self.chance:
                self.scene.add_object(self.item)
        elif self.hits == self.max_hits - 2 and self.hits != 0:
            self.image = os.path.join("images","brick_blank_crack1.png")
        elif self.hits == self.max_hits - 1 and self.hits != 0:
            self.image = os.path.join("images","brick_blank_crack2.png")
        
    def hit(self):
        self.hits += 1


