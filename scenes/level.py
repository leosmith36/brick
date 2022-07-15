from scene import Scene
from levels import Levels
from colors import Color
from objects import Bar, Ball, Brick
from window import Window
from utils import collides_top, collides_bottom, collides_right, collides_left
from objects import Trail
from objects import Text
from fonts import Font
from .fail import Fail
from objects import Item

class Level(Scene):

    def __init__(self, game, level):
        super().__init__(game)
        self.level = level
        self.bar = Bar(self)
        self.ball = Ball(self)
        self.level_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK.value, f"Level {self.level}", Font.FONT1.value, center = True)
        self.objects = Levels.make_level(level, self) + [self.bar, self.ball, self.level_text]
        self.started = False


    def update(self):
        self.check_collisions()
        super().update()


    def render(self, win):
        win.fill(Color.WHITE.value)
        super().render(win)


    def click(self):
        if not self.started:
            self.started = True
            self.ball.unlock()
            self.level_text.remove()
        super().click()

    def check_collisions(self):
        num_bricks = 0
        for object in self.objects:
            if isinstance(object, Brick):
                num_bricks += 1
                hit = True
                if collides_bottom(self.ball, object) or collides_top(self.ball, object):
                    self.ball.reflect_horizontal()
                elif collides_left(self.ball, object) or collides_right(self.ball, object):
                    self.ball.reflect_vertical()
                else:
                    hit = False
                if hit:
                    object.hit()
            if isinstance(object, Item):
                if object.rect.colliderect(self.bar.rect):
                    object.activate()
        
        if num_bricks == 0:
            self.game.next_level()
        
        if collides_top(self.ball, self.bar):
            self.ball.reflect_bar_top(self.bar.centerx)
        elif collides_left(self.ball, self.bar) or collides_left(self.ball, self.bar) or self.ball.rect.colliderect(self.bar.rect):
            self.ball.reflect_vertical()
        elif self.ball.rect.top - self.ball.vec.y < 0:
            self.ball.reflect_horizontal()
        elif self.ball.rect.right - self.ball.vec.x > Window.WIDTH or self.ball.rect.left  - self.ball.vec.x < 0:
            self.ball.reflect_vertical()
        elif self.ball.rect.top >= Window.HEIGHT:
            self.game.change_scene(Fail(self.game))

    def long_bar(self):
        self.bar.long_bar()


