import pygame
from abc import ABC, abstractmethod

from window import Window


class Object(ABC):
    def __init__(self, scene, x, y, w, h, color, center = False, image = None, visible = True):

        self._w = w
        self._h = h
        self.surface = pygame.Surface((w, h), pygame.SRCALPHA)

        if center:
            self.centerx = x
            self.centery = y
        else:
            self.x = x
            self.y = y
       
        if image:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = None

        self.effects = []
        self.rect = self.surface.get_rect(center = self.center)
        self.color = color.value
        self.color_key = color
        self.removed = False
        self.visible = visible
        self.scene = scene
        self.scene.add_object(self)
    
    @abstractmethod
    def tick(self):
        pass

    def update(self):
        if not self.visible:
            return
        new_effects = []
        for effect in self.effects:
            effect.update()
            if not effect.is_removed():
                new_effects.append(effect)
        self.effects = new_effects
        self.tick()

    def render(self, win):
        if not self.visible:
            return
        self.surface.fill(self.color)
        win.blit(self.surface, self.rect)
        if self.image:
            image = pygame.transform.scale(self.image, (self.w, self.h))
            win.blit(image, self.rect)

    @property
    def rect(self):
        self._rect.center = self.center
        return self._rect
    
    @rect.setter
    def rect(self, rect):
        self._rect = rect

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

    def is_removed(self):
        return self.removed
    
    def remove(self):
        self.removed = True

    def add_effect(self, effect):
        self.effects.append(effect)

    @property
    def alpha(self):
        return self.color[3]
    
    @alpha.setter
    def alpha(self, alpha):
        self.color = (self.color[0],self.color[1],self.color[2],alpha)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    class Effect():
        def __init__(self, parent, effect, reset, max_frames):
            self.reset = reset
            self.max_frames = max_frames
            self.frames = 0
            self.parent = parent
            self.parent.add_effect(self)
            self.removed = False
            effect(self.parent)
            
        def update(self):
            self.frames += 1
            diff = self.max_frames - self.frames
            if diff <= 0:
                self.reset(self.parent)
                self.remove()

        def is_removed(self):
            return self.removed

        def remove(self):
            self.removed = True



