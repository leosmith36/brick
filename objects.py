import pygame
import random

class GameObject():
    def __init__(self,win,x,y):
        self.x = x
        self.y = y
        self.win = win
        self.blit()
    def blit(self):
        self.win.blit(self.x,self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y

class Ball(GameObject):
    def __init__(self,win,x,y,spd,rad):
        self.spd = spd
        self.rad = rad
        self.vec = pygame.math.Vector2(0,self.spd)
        self.vec = pygame.math.Vector2.rotate(self.vec,random.uniform(-30,30))
        super().__init__(win,x,y)
    def reflect(self,dir):
        if dir == "v":
            self.vec = self.vec.reflect(pygame.math.Vector2(1,0))
        elif dir == "h":
            self.vec = self.vec.reflect(pygame.math.Vector2(0,1))
    def blit(self):
        self.rect = pygame.draw.circle(self.win,(255,0,0),(self.x,self.y),self.rad)