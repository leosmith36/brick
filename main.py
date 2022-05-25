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

BRICK_WIDTH = 50
BRICK_HEIGHT = 25

COOLDOWN = 100

def main():

    class Ball():
        def __init__(self,spd,x,y,rad):
            self.spd = spd
            self.rad = rad
            self.y = y
            self.x = x
            self.vec = pygame.math.Vector2(0,self.spd)
            #self.vec = pygame.math.Vector2.rotate(self.vec,random.uniform(-30,30))
            self.vec = pygame.math.Vector2.rotate(self.vec,-30)
            self.ntime = pygame.time.get_ticks()
            self.blit()
        def reflect(self,dir):
            if dir == "v":
                self.vec = self.vec.reflect(pygame.math.Vector2(1,0))
            elif dir == "h":
                self.vec = self.vec.reflect(pygame.math.Vector2(0,1))
        def blit(self):
            self.rect = pygame.draw.circle(WIN,RED,(self.x,self.y),self.rad)

    class Bar():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.size = (BAR_WIDTH,BAR_HEIGHT)
            self.blit()
        def blit(self):
            self.rect = pygame.draw.rect(WIN,BLUE,pygame.Rect((self.x,self.y),self.size))

    class Brick():
        def __init__(self,x,y,color,hits,key):
            self.color = color
            self.x = x
            self.y = y
            self.size = (BRICK_WIDTH,BRICK_HEIGHT)
            self.hits = hits
            self.key = key
            self.blit()
        def blit(self):
            if self.hits <= 0:
                for brick in bricks:
                    if brick.key == self.key:
                        bricks.remove(brick)
            elif self.hits == 1:
                self.color = RED
            self.rect = pygame.draw.rect(WIN,self.color,pygame.Rect((self.x,self.y),self.size))

    run = True
    start = False
    clock = pygame.time.Clock()
    ball = Ball(BALL_SPEED,450,399,BALL_RAD)
    bar = Bar(ball.x - BAR_WIDTH/2,ball.y + ball.rad)
    layout = ["g"*10]*5       
    bricks = []
    key = 0
    y = 50
    for item in layout:
        length = len(item)
        total_length = BRICK_WIDTH*length + 5*(length-1)
        x = (WIDTH - total_length)//2
        for letter in item:
            if letter == "g":
                bricks.append(Brick(x,y,GREEN,2,key))
                x += BRICK_WIDTH + 5
                key += 1
        y += BRICK_HEIGHT + 5

    def checkHits():
        collide = False
        if (ball.rect.left <= 0 and ball.vec.x > 0) or (ball.rect.right >= WIDTH and ball.vec.x < 0):
            ball.reflect("v")
        elif ball.rect.top <= 0 and ball.vec.y > 0:
            ball.reflect("h")
        
        if (
            ball.rect.bottom >= bar.rect.top and
            ball.rect.bottom <= bar.rect.bottom and
            ball.rect.centerx >= bar.rect.left and 
            ball.rect.centerx <= bar.rect.right and
            ball.vec.y < 0
        ):
            ball.reflect("h")

        collided = False
        for brick in bricks:
            ctime = pygame.time.get_ticks()
            if collided == True or ctime - ball.ntime <= COOLDOWN:
                continue
            if (
                ball.rect.centerx <= brick.rect.right and 
                ball.rect.centerx >= brick.rect.left and
                ball.rect.top <= brick.rect.bottom and 
                ball.rect.top > brick.rect.top and
                ball.rect.bottom > brick.rect.bottom and
                ball.vec.y > 0
            ):
                ball.reflect("h")
                collide = True
            elif (
                ball.rect.centerx <= brick.rect.right and 
                ball.rect.centerx >= brick.rect.left and
                ball.rect.bottom >= brick.rect.top and 
                ball.rect.bottom < brick.rect.bottom and
                ball.rect.top < brick.rect.top and
                ball.vec.y < 0
            ):
                ball.reflect("h")
                collide = True
            elif (
                ball.rect.left <= brick.rect.right and
                ball.rect.left > brick.rect.left and
                ball.rect.centery <= brick.rect.bottom and
                ball.rect.centery >= brick.rect.top and
                ball.rect.right > brick.rect.right and
                ball.vec.x > 0
            ):
                ball.reflect("v")
                collide = True
            elif (
                ball.rect.right >= brick.rect.left and
                ball.rect.right <= brick.rect.right and
                ball.rect.centery >= brick.rect.top and
                ball.rect.centery <= brick.rect.bottom and
                ball.rect.left < brick.rect.left and
                ball.vec.x < 0
            ):
                ball.reflect("v")
                collide = True
            if collide:
                brick.hits -= 1
                collided = True
                ball.ntime = ctime

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
        if ball.rect.bottom >= HEIGHT and ball.vec.y < 0:
            run = False
        controlBall()
        checkHits()
        draw_window()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()