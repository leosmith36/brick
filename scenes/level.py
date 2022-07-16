import pygame

from scene import Scene
from levels import Levels
from colors import Color
from objects import Bar, Ball, Brick, Text, Item
from window import Window
from fonts import Font
from .fail import Fail

class Level(Scene):

    def __init__(self, game, level):
        new_level, background = Levels.make_level(level, self)
        super().__init__(game, Color.WHITE, image = background)
        self.level = level
        self.bar = Bar(self)
        self.ball = Ball(self)
        self.level_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, f"Level {self.level}", Font.FONT1, center = True)
        
        self.objects.extend(new_level)
        self.objects.extend([self.bar, self.ball, self.level_text])
        self.started = False
        self.Binding(self, pygame.MOUSEBUTTONDOWN, lambda: self.start())
        self.Binding(self, pygame.KEYDOWN, lambda : self.pause(), key = pygame.K_ESCAPE)
        self.paused = False
        self.pause_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "PAUSED", Font.FONT1, center = True)


    def update(self):
        if not self.paused:
            self.check_collisions()
            super().update()

    def fail(self):
        self.game.change_scene(Fail(self.game))

    def start(self):
        if not self.started:
            self.started = True
            self.ball.unlock()
            self.level_text.remove()

    def pause(self):
        if self.started and not self.paused:
            self.paused = True
            self.objects.append(self.pause_text)
        elif self.paused:
            self.paused = False
            self.remove_object(self.pause_text)

    def check_collisions(self):
        num_bricks = 0
        for object in self.objects:
            if isinstance(object, Brick):
                num_bricks += 1
                if self.ball.check_collisions(object):
                    object.hit()
            if isinstance(object, Item):
                if object.rect.colliderect(self.bar.rect):
                    object.activate()
        if num_bricks == 0:
            self.game.next_level()
        
        self.ball.check_bar(self.bar)

    def long_bar(self):
        self.bar.long_bar()


