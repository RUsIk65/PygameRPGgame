from abc import ABC, abstractmethod
from world.camera import camera_group
import pygame

class BaseEntity(ABC, pygame.sprite.Sprite):
    def __init__(self, id, name, image, pos):
        super().__init__(camera_group)
        self._name = name
        self._id = id
        self._image = pygame.image.load(image)
        self._rect = self.image.get_rect(topleft = pos)
        self._hitbox = (self._rect.x + 10, self._rect.y + 5, 45, 70)
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect
    
    @property
    def hitbox(self):
        return self._hitbox

    @id.setter
    def id(self, id):
        self._id = id

    @name.setter
    def name(self, name):
        self._name = name

    @image.setter
    def image(self, image):
        self._image = image

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    #@radar_range.setter
    #def radar_range(self, radar_range):
    #   self._radar_range = radar_range

    
    @abstractmethod
    def entity_type(self):
        pass
    
    @abstractmethod
    def entity_info(self):
        pass



    #def take_damage(self, damage):
    #    effective_damage = max(0, damage - self._defense)
    #    self._hp = max(0, self._hp - effective_damage)
    #    return effective_damage

    #def attack_entity(self, target):
    #    if self.is_live():
    #        damage_dealt = target.take_damage(self._attack)
    #        return damage_dealt
    #    return 0

    #def is_live(self):
    #    return self._hp > 0
    