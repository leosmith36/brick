import pygame
from enum import Enum

pygame.font.init()

class Font(Enum):
    FONT1 = pygame.font.SysFont("airial", 50)
    FONT2 = pygame.font.SysFont("airial", 25)