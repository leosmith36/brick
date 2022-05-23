import pygame
import sys
import random

WIDTH,HEIGHT = 900,500
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brickbreaker")

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

BALL_SPEED = 5
BALL_RAD = 10

BAR_WIDTH = 100
BAR_HEIGHT = 20

BRICK_WIDTH = 40
BRICK_HEIGHT = 20

def main():

    class Ball():
        def __init__(self,spd,x,y,rad):
            self.spd = spd
            self.rad = rad
            self.y = y
            self.x = x
            vec = pygame.math.Vector2(0,self.spd)
            self.vec = pygame.math.Vector2.rotate(vec,random.uniform(-30,30))
            self.fail = False
        def reflect(self,dir):
            if dir == "v":
                self.vec = self.vec.reflect(pygame.math.Vector2(1,0))
            else:
                self.vec = self.vec.reflect(pygame.math.Vector2(0,1))
        def blit(self):
            self.rect = pygame.draw.circle(WIN,RED,(self.x,self.y),self.rad)

    class Bar():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.size = (BAR_WIDTH,BAR_HEIGHT)
        def blit(self):
            self.rect = pygame.draw.rect(WIN,BLUE,pygame.Rect((self.x,self.y),self.size))

    class Brick():
        def __init__(self,x,y,color,hits):
            self.color = color
            self.x = x
            self.y = y
            self.size = (BRICK_WIDTH,BRICK_HEIGHT)
            self.hits = hits
        def blit(self):
            self.rect = pygame.draw.rect(WIN,self.color,pygame.Rect((self.x,self.y),self.size))

    def checkHits():
        if ball.x <= ball.rad or ball.x >= WIDTH - ball.rad:
            ball.reflect("v")
        if ball.y <= ball.rad:
            ball.reflect("h")
        if ball.y > bar.y - ball.rad and ball.x > bar.x and ball.x < bar.x + BAR_WIDTH and not ball.fail:
            ball.reflect("h")
        elif ball.y > bar.y -ball.rad and not (ball.x > bar.x and ball.x < bar.x + BAR_WIDTH):
            ball.fail = True

    def controlBall():
        if start:
            ball.x -= ball.vec.x
            ball.y -= ball.vec.y

    def draw_window():
        WIN.fill(WHITE)
        ball.blit()
        if mouse_pos[0] > BAR_WIDTH/2 and mouse_pos[0] < WIDTH - BAR_WIDTH/2:
            bar.x = mouse_pos[0] - BAR_WIDTH/2
        if not start:
            ball.x = bar.x + BAR_WIDTH/2
        bar.blit()
        for brick in bricks:
            brick.blit()
        pygame.display.update()

    run = True
    start = False
    clock = pygame.time.Clock()
    ball = Ball(BALL_SPEED,450,400,BALL_RAD)
    bar = Bar(ball.x - BAR_WIDTH/2,ball.y + ball.rad)
    bricks = [Brick(100,100,GREEN,3)]

    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = True
        controlBall()
        checkHits()
        draw_window()


if __name__ == "__main__":
    main()