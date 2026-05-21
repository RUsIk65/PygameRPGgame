import pygame, math

from .BaseEntity import *
from systems.stats import Stats

MAP_WIDTH = 500 * 16
MAP_HEIGHT = 500 * 16
class Player(BaseEntity, Stats):
    def __init__(self, id, name, image, pos,
                hp = 100, mana = 50, attack = 20,
                defense = 10, speed =50,attack_range=0,
                crit_chance=0, level = 1
                ):
        BaseEntity.__init__(self, id, name, image, pos)
    
        Stats.__init__(self, hp, mana, attack, defense,
                       speed, attack_range, crit_chance, level)

        self.rect = self.image.get_rect(topleft=pos)
        # self.rect.topleft = (x, y)

        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.centery)


        self.radius = 20
        self.target_pos = None

    def entity_type(self):
        return "player"

    def entity_info(self):
        pass
    
    def set_target(self, pos):
        self.target_pos = pos

    def update(self):
        if not self.target_pos:
            return

        target_x, target_y = self.target_pos
        dx = target_x - (self.pos_x + self.rect.width / 2)
        dy = target_y - (self.pos_y + self.rect.height / 2)
        distance = math.hypot(dx, dy)

        if distance <= self._speed:
            self.pos_x = target_x - self.rect.width / 2
            self.pos_y = target_y - self.rect.height / 2
            self.target_pos = None
        else:
            self.pos_x += (dx / distance) * self._speed
            self.pos_y += (dy / distance) * self._speed

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos_x = float(self.rect.x)
            self.target_pos = None  
        elif self.rect.right > MAP_WIDTH:
            self.rect.right = MAP_WIDTH
            self.pos_x = float(self.rect.x)
            self.target_pos = None

        if self.rect.top < 0:
            self.rect.top = 0
            self.pos_y = float(self.rect.y)
            self.target_pos = None
        elif self.rect.bottom > MAP_HEIGHT:
            self.rect.bottom = MAP_HEIGHT
            self.pos_y = float(self.rect.y)
            self.target_pos = None
