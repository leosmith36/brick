import pygame

from scene import Scene
from levels import Levels
from colors import Color
from objects import Bar, Ball, Brick, Text, Item
from window import Window
from fonts import Font
from .fail import Fail

class Level(Scene):

    def __init__(self, game, level, consecutive):
        super().__init__(game, Color.WHITE)
        self.bricks, background = Levels.make_level(level, self)
        self.image = pygame.image.load(background).convert()
        

        self.level = level
        self.bar = Bar(self)
        self.ball = Ball(self)
        self.level_text = Text(self, Window.WIDTH // 2, 200, Color.BLACK, f"Level {self.level + 1}", Font.FONT1, center = True)
        
        self.lives_text = Text(self, Window.WIDTH - 75, 10, Color.BLACK, f"Lives: val", Font.FONT2, value = 3)

        # self.objects.extend(self.bricks)
        # self.objects.extend([self.bar, self.ball, self.level_text, self.lives_text])

        self.started = False
        # self.paused = False
        self.consecutive = consecutive

        self.Binding(self, pygame.KEYDOWN, lambda : self.start(), key = pygame.K_SPACE)
        self.Binding(self, pygame.KEYDOWN, lambda : self.game.pause(), key = pygame.K_ESCAPE, on_paused = True)

        # self.pause_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "PAUSED", Font.FONT1, center = True)


    def update(self):
        # if not self.paused:
        #     self.pause_text.visible = False
        if self.started:
            self.level_text.visible = False
            self.check_collisions()
        super().update()
        # else:
        # self.pause_text.visible = True

    def fail(self):
        if self.lives <= 1:
            self.game.fail()
        else:
            self.reload()

    def start(self):
        if not self.started:
            self.started = True
            self.ball.unlock()

    # def pause(self):
    #     if self.started and not self.paused:
    #         self.paused = True
    #     elif self.paused:
    #         self.paused = False

    def reload(self):
        self.started = False
        self.ball = Ball(self)
        self.lives -= 1
        # for object in self.objects:
        #     if not isinstance(object, Brick):
        #         self.remove_object(object)
        # self.objects.extend([self.bar, self.ball, self.lives_text])

    def win(self):
        if self.consecutive:
            self.game.next_level()
        else:
            self.game.choose_level()


    def check_collisions(self):
        new_bricks = []
        for object in self.objects:
            if isinstance(object, Brick):
                if self.ball.check_collisions(object):
                    object.hit()
                if not object.removed:
                    new_bricks.append(object)
            if isinstance(object, Item):
                if object.rect.colliderect(self.bar.rect):
                    object.activate()
        self.bricks = new_bricks
        if len(new_bricks) == 0 and self.started:
            self.win()
        
        self.ball.check_bar(self.bar)

    def long_bar(self):
        self.bar.long_bar()

    def slow_ball(self):
        self.ball.slow_ball()

    def fast_bar(self):
        self.bar.fast_bar()

    @property
    def lives(self):
        return self.lives_text.value

    @lives.setter
    def lives(self, lives):
        self.lives_text.value = lives

    @property
    def bar(self):
        return self._bar
    
    @bar.setter
    def bar(self, bar):
        self._bar = bar


