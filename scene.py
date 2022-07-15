from abc import ABC

from objects import Button

class Scene(ABC):

    def __init__(self, game):
        self.game = game
        self.new_objects = []
        self.del_objects = []

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

    def click(self):
        for object in self.objects:
            if isinstance(object, Button):
                object.click()

    def add_object(self, object):
        self.new_objects.append(object)

    def remove_object(self, object):
        self.del_objects.append(object)