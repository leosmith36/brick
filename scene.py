from abc import ABC
import pygame

from objects import Button

class Scene(ABC):

    def __init__(self, game):
        self.game = game
        self.new_objects = []
        self.del_objects = []
        self.bindings = []

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
        for object in self.objects:
            object.render(win)

    def click(self, event):
        for object in self.objects:
            if isinstance(object, Button):
                object.click(event)
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

