from abc import ABC
import pygame

from objects import Button
from window import Window

class Scene(ABC):

    def __init__(self, game, background_color, image = None):
        self.game = game
        self.objects = []
        self.new_objects = []
        self.del_objects = []
        self.bindings = []
        self.background_color = background_color.value
        self.background_image = image

    @property
    def objects(self):
        return self._objects
    
    @objects.setter
    def objects(self, objects):
        self._objects = objects

    def update(self):
        remaining_objects = []
        for object in self.objects:
            object.update()
            if not object.removed and not object in self.del_objects:
                remaining_objects.append(object)
        self.objects = remaining_objects
        self.objects += self.new_objects
        self.new_objects.clear()
        

    def render(self, win):
        win.fill(self.background_color)
        if self.background_image:
            image = pygame.image.load(self.background_image)
            image = pygame.transform.scale(image, (Window.WIDTH, Window.HEIGHT))
            win.blit(image, (0,0))
        for object in self.objects:
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
        def __init__(self, parent, type, function, key = None):
            self.parent = parent
            self.type = type
            self.key = key
            self.parent.add_binding(self)
            self.function = function
        def check(self, event):
            if event.type == self.type:
                if self.key:
                    if self.key == event.key:
                        self.function()
                else:
                    self.function()

