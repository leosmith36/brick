import pygame

from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self, scene, x, y, w, h, color, center = False, image = None):

        self._w = w
        self._h = h
        self.surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self.effects = []

        if center:
            self.centerx = x
            self.centery = y
        else:
            self.x = x
            self.y = y
            
        self._rect = self.surface.get_rect(center = self.center)
        self.image = image
        self.color = color
        self.removed = False
        self._scene = scene
    @abstractmethod
    def update(self):
        pass

    def render(self, win):
        new_effects = []
        for effect in self.effects:
            effect.update()
            if not effect.removed:
                new_effects.append(effect)
        self.effects = new_effects
        
        self.surface.fill(self.color)
        win.blit(self.surface, self.rect)
        if self.image:
            image = pygame.image.load(self.image)
            image = pygame.transform.scale(image, (self.w, self.h))
            win.blit(image, self.rect)

    @property
    def rect(self):
        self._rect.center = self.center
        return self._rect

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def centerx(self):
        return self.x + self.w // 2

    @centerx.setter
    def centerx(self, centerx):
        self.x = centerx - self.w // 2

    @property
    def centery(self):
        return self.y + self.h // 2

    @centery.setter
    def centery(self, centery):
        self.y = centery - self.h // 2

    @property
    def center(self):
        return (self.centerx, self.centery)

    @center.setter
    def center(self, center):
        self.centerx = center[0]
        self.centery = center[1]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        self._w = w
        self.surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
        self._rect = self.surface.get_rect(center = self.center)

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h
        self.surface = pygame.Surface((self._w, self._h), pygame.SRCALPHA)
        self._rect = self.surface.get_rect(center = self.center)

    @property
    def removed(self):
        return self._removed

    @removed.setter
    def removed(self, removed):
        self._removed = removed
    
    def remove(self):
        self.removed = True

    @property
    def scene(self):
        return self._scene

    class Effect():
        def __init__(self, parent, effect, reset, max_time):
            self.time = pygame.time.get_ticks()
            self.reset = reset
            self.max_time = max_time
            self.parent = parent
            self.parent.add_effect(self)
            self.removed = False
            effect(self.parent)
        def update(self):
            newtime = pygame.time.get_ticks()
            diff = (newtime - self.time) / 1000
            if diff >= self.max_time:
                self.reset(self.parent)
                self.remove()

        @property
        def removed(self):
            return self._removed

        @removed.setter
        def removed(self, removed):
            self._removed = removed

        def remove(self):
            self.removed = True


    def add_effect(self, effect):
        self.effects.append(effect)