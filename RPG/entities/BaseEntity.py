from abc import ABC, abstractmethod
from world.camera import camera_group
import pygame

MAP_WIDTH = 500 * 16
MAP_HEIGHT = 500 * 16
class BaseEntity(ABC, pygame.sprite.Sprite):
    def __init__(self, id, name, image, pos):
        super().__init__(camera_group)
        self._name = name
        self._id = id
        self._image = pygame.image.load(image)
        self._rect = self.image.get_rect(topleft = pos)
        self._hitbox = (self._rect.x + 10, self._rect.y + 5, 45, 70)
    
        self._hitbox = pygame.Rect(self._rect.x + 10, self._rect.y + 5, 45, 70)
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

    def move(self, dx, dy, walls_group=None):
        collided = False

        if dx != 0:
            self.pos_x += dx
            self._rect.x = int(self.pos_x)
            self._update_hitbox_position()

            if self._rect.left < 0:
                self._rect.left = 0
                self.pos_x = float(self._rect.x)
                collided = True
            elif self._rect.right > MAP_WIDTH:
                self._rect.right = MAP_WIDTH
                self.pos_x = float(self._rect.x)
                collided = True

            if walls_group:
                old_rect = self.rect
                self.rect = self._hitbox 
                hit_list = pygame.sprite.spritecollide(self, walls_group, False)
                self.rect = old_rect   
                
                for wall in hit_list:
                    if dx > 0: 
                        self._hitbox.right = wall.rect.left
                        self._rect.x = self._hitbox.x - 10 
                    if dx < 0: 
                        self._hitbox.left = wall.rect.right
                        self._rect.x = self._hitbox.x - 10
                    self.pos_x = float(self._rect.x)
                    collided = True

        if dy != 0:
            self.pos_y += dy
            self._rect.y = int(self.pos_y)
            self._update_hitbox_position()

            if self._rect.top < 0:
                self._rect.top = 0
                self.pos_y = float(self._rect.y)
                collided = True
            elif self._rect.bottom > MAP_HEIGHT:
                self._rect.bottom = MAP_HEIGHT
                self.pos_y = float(self._rect.y)
                collided = True

            if walls_group:
                old_rect = self.rect
                self.rect = self._hitbox
                hit_list = pygame.sprite.spritecollide(self, walls_group, False)
                self.rect = old_rect
                
                for wall in hit_list:
                    if dy > 0: 
                        self._hitbox.bottom = wall.rect.top
                        self._rect.y = self._hitbox.y - 5 
                    if dy < 0: 
                        self._hitbox.top = wall.rect.bottom
                        self._rect.y = self._hitbox.y - 5
                    self.pos_y = float(self._rect.y)
                    collided = True

        self._update_hitbox_position()
        return collided


    def take_damage(self, damage):
       effective_damage = max(0, damage - self._defense)
       self._hp = max(0, self._hp - effective_damage)
       return effective_damage

    def attack_entity(self, target):
       if self.is_live():
           damage_dealt = target.take_damage(self._attack)
           return damage_dealt
       return 0

    def is_live(self):
       return self._hp > 0
    
