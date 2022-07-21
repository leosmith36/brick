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
            if event.type == pygame.QUIT or game.is_closed():
                active = False
                break
            game.trigger(event)
        game.update()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()