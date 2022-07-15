import pygame
import sys

from game import Game

def main():
    pygame.init()
    active = True
    game = Game()
    while active:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or game.exited:
                active = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                game.click(event)
        game.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()