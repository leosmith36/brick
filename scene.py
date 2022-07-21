from abc import ABC
import pygame

from objects import Button
from window import Window
from objects import Text
from colors import Color
from fonts import Font

class Scene(ABC):

    def __init__(self, game, background_color, image = None):
        self.game = game
        self.objects = []
        self.new_objects = []
        self.del_objects = []
        self.bindings = []
        self.background_color = background_color.value

        if image:
            self.image = pygame.image.load(image).convert()
        else:
            self.image = None

        self.Binding(self, pygame.KEYDOWN, lambda : self.game.restart(), key = pygame.K_BACKSPACE)

        self.pause_text = Text(self, Window.WIDTH // 2, 100, Color.BLACK, "PAUSED", Font.FONT1, center = True)

    def update(self):
        remaining_objects = []
        for object in self.objects:
            object.update()
            if not object.is_removed() and not object in self.del_objects:
                remaining_objects.append(object)
        self.objects = remaining_objects
        self.objects += self.new_objects
        self.new_objects.clear()
        self.del_objects.clear()
        

    def render(self, win):
        self.pause_text.visible = self.game.is_paused()
        win.fill(self.background_color)
        if self.image:
            image = pygame.transform.scale(self.image, (Window.WIDTH, Window.HEIGHT))
            win.blit(image, (0,0))
        text_objects = []
        for object in self.objects:
            if isinstance(object, Text):
                text_objects.append(object)
            else:
                object.render(win)
        for object in text_objects:
            object.render(win)

    def trigger(self, event):
        for object in self.objects:
            if isinstance(object, Button):
                object.trigger(event)
        for binding in self.bindings:
            binding.check(event)

    def add_object(self, object):
        self.new_objects.append(object)

    def remove_object(self, object):
        self.del_objects.append(object)

    def add_binding(self, binding):
        self.bindings.append(binding)

    class Binding:
        def __init__(self, parent, type, function, key = None, on_paused = False):
            self.parent = parent
            self.type = type
            self.key = key
            self.parent.add_binding(self)
            self.function = function
            self.on_paused = on_paused
        def check(self, event):
            if not self.on_paused and self.parent.game.is_paused():
                return
            if event.type == self.type:
                if self.key:
                    if self.key == event.key:
                        self.function()
                else:
                    self.function()

