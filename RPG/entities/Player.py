import pygame, math
from .BaseEntity import *
from systems.stats import Stats

#from systems.inventory import Inventory

class Player(BaseEntity, Stats):
    def __init__(self, id, name, image, pos,
                hp = 100, mana = 50, attack = 20,
                defense = 10, speed = 10, attack_range=0,
                crit_chance=0, level = 1
                ):
        BaseEntity.__init__(self, id, name, image, pos)
    
        Stats.__init__(self, hp, mana, attack, defense,
                       speed, attack_range, crit_chance, level)

        self.rect = self.image.get_rect(topleft=pos)

        # Плавное движение
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
        if self.target_pos:
            dx = self.target_pos[0] - self.pos_x
            dy = self.target_pos[1] - self.pos_y
            distance = math.hypot(dx, dy)

            if distance > self._speed:
                dx /= distance
                dy /= distance
                self.pos_x += dx * self._speed
                self.pos_y += dy * self._speed
            else:
                self.target_pos = None

            self.rect.center = (int(self.pos_x), int(self.pos_y))

        # Ограничение карты
        self.rect.x = max(0, min(1500 - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(800 - self.rect.height, self.rect.y))


