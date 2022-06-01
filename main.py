import pygame
import sys
import random
from objects import *
pygame.font.init()

WIDTH,HEIGHT = 600,600
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brickbreaker")

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
DGREEN = (1,50,32)
GREEN = (0,255,0)
LGREEN = (144,238,144)
BLACK = (0,0,0)

BALL_SPEED = 7
BALL_RAD = 10


COOLDOWN = 100

ANGLE_MULT = 1.5

PLAY_W = 200
PLAY_H = 50
PLAY_TEXT = pygame.font.SysFont("airial",50)
PLAY = pygame.Rect(WIDTH//2 - PLAY_W//2,HEIGHT//2 - PLAY_H//2,PLAY_W,PLAY_H)

LEVEL_TEXT = pygame.font.SysFont("airial",50)

L0 = [
    "gggggggg",
    "",
    "gggggggg",
    "",
    "gggggggg",
    "",
    "gggggggg",
]
L1 = [
    "gggggggg",
    "gggggggg",
    "",
    "",
    "gggggggg",
    "gggggggg"
]
L2 = [
    "gggggggg",
    "gbbbbbbg",
    "gbggggbg",
    "gbggggbg",
    "gbbbbbbg",
    "gggggggg"
]

LEVELS = [L0,L1,L2]

def main():

    

    game = Game()
    clock = pygame.time.Clock()
    ball = Ball(WIN,450,500,BALL_SPEED,BALL_RAD)
    bar = Bar(WIN,0,ball.y + ball.rad)
    bar.setX(ball.x - bar.getWidth()//2)
    bricks = []

    def makeLevel(level):
        key = 0
        y = 50
        for item in LEVELS[level]:
            length = len(item)
            total_length = Brick.width*length + 5*(length-1)
            x = (WIDTH - total_length)//2
            for letter in item:
                if letter == "g":
                    bricks.append(Brick(WIN,x,y,DGREEN,3,key))
                x += Brick.width + 5
                key += 1
            y += Brick.getHeight() + 5

    def checkHits():
        collide = False
        if (ball.rect.left <= ball.vec.x and ball.vec.x > 0) or (ball.rect.right >= WIDTH + ball.vec.x and ball.vec.x < 0):
            ball.reflect("v")
        elif ball.rect.top <= ball.spd and ball.vec.y > 0:
            ball.reflect("h")
        
        if (
            ball.rect.bottom >= bar.rect.top + ball.vec.y and
            ball.rect.bottom <= bar.rect.bottom and
            ball.rect.centerx >= bar.rect.left and 
            ball.rect.centerx <= bar.rect.right and
            ball.vec.y < 0
        ):
            dist = ball.rect.centerx - bar.rect.centerx
            ball.vec = pygame.math.Vector2(0,ball.spd)
            ball.vec = ball.vec.rotate(ANGLE_MULT*dist)

        collided = False
        for brick in bricks:
            if collided == True or brick.ctime - brick.ntime <= COOLDOWN:
                continue
            if (
                ball.rect.centerx <= brick.rect.right and 
                ball.rect.centerx >= brick.rect.left and
                ball.rect.top <= brick.rect.bottom + ball.vec.y and 
                ball.rect.top > brick.rect.top and
                ball.rect.bottom > brick.rect.bottom and
                ball.vec.y > 0
            ):
                ball.reflect("h")
                collide = True
            elif (
                ball.rect.centerx <= brick.rect.right and 
                ball.rect.centerx >= brick.rect.left and
                ball.rect.bottom >= brick.rect.top + ball.vec.y and 
                ball.rect.bottom < brick.rect.bottom and
                ball.rect.top < brick.rect.top and
                ball.vec.y < 0
            ):
                ball.reflect("h")
                collide = True
            elif (
                ball.rect.left <= brick.rect.right + ball.vec.x and
                ball.rect.left > brick.rect.left and
                ball.rect.centery <= brick.rect.bottom and
                ball.rect.centery >= brick.rect.top and
                ball.rect.right > brick.rect.right and
                ball.vec.x > 0
            ):
                ball.reflect("v")
                collide = True
            elif (
                ball.rect.right >= brick.rect.left + ball.vec.x and
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
                brick.ntime = pygame.time.get_ticks()

    def controlBall():
        if game.start:
            ball.x -= ball.vec.x
            ball.y -= ball.vec.y

    def draw_start():
        WIN.fill(WHITE)
        play = PLAY_TEXT.render("PLAY",1,BLACK)
        pygame.draw.rect(WIN,RED,PLAY)
        WIN.blit(play,(
            WIDTH//2 - play.get_width()//2,
            HEIGHT//2 - play.get_height()//2
        ))
        pygame.display.update()

    def draw_window():
        WIN.fill(WHITE)
        ball.blit()
        if mouse_pos[0] > bar.getWidth()/2 and mouse_pos[0] < WIDTH - bar.getWidth()/2:
            bar.x = mouse_pos[0] - bar.getWidth()/2
        if not game.start:
            ball.x = bar.x + bar.getWidth()/2
            ball.y = bar.y - ball.rad - 1
            level_display = LEVEL_TEXT.render("Level " + str(level),1,BLACK)
            WIN.blit(level_display,
                (WIDTH//2 - level_display.get_width()//2,
                HEIGHT//2 - level_display.get_height()//2)
            )
        bar.blit()
        for brick in bricks:
            brick.blit()
        pygame.display.update()

    while game.run:
        clock.tick(FPS)
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                game.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.init:
                    game.start = True
                elif PLAY.collidepoint(mouse_pos):
                    game.init = True
        if ball.rect.bottom >= HEIGHT and ball.vec.y < 0:
            game.run = False
        if len(bricks) == 0 and game.init:
            makeLevel(game.level)
            level +=1
            game.start = False
        if not game.init:
            draw_start()
        else:
            controlBall()
            checkHits()
            draw_window()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()