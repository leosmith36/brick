import pygame

class Window():
    WIDTH = 509
    HEIGHT = 600
    def __init__(self):
        self.win = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Brickbreaker Game")
        