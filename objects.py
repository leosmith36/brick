import pygame
import random
import sys

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

class Bar(GameObject):
    width = 100
    height = 20
    def __init__(self,win,x,y):
        super().__init__(win,x,y)
    def blit(self):
        self.rect = pygame.draw.rect(self.win,(0,0,255),pygame.Rect((self.x,self.y),(Bar.width,Bar.height)))


class Brick(GameObject):
    width = 50
    height = 25
    def __init__(self,win,x,y,color,hits,key,game):
        self.color = color
        self.hits = hits
        self.key = key
        self.ntime = pygame.time.get_ticks()
        self.game = game
        super().__init__(win,x,y)
    def blit(self):
        bricks = self.game.getBricks()
        self.ctime = pygame.time.get_ticks()
        if self.hits <= 0:
            for brick in bricks:
                if brick.key == self.key:
                    bricks.remove(brick)
                    self.game.newBricks(bricks)
        elif self.hits == 2:
            self.color = (0,255,0)
        elif self.hits == 1:
            self.color = (144,238,144)
        self.rect = pygame.draw.rect(self.win,self.color,pygame.Rect((self.x,self.y),(self.width,self.height)))

class Game():
    def __init__(self):
        self.bricks = []
        self.init = False
        self.run = True
        self.start = False
        self.level = 0
    def getBricks(self):
        return self.bricks
    def removeBrick(self,brick):
        self.bricks.remove(brick)
    def newBricks(self,bricks):
        self.bricks = bricks
    def exit(self):
        self.run = False
        pygame.quit()
        sys.exit()