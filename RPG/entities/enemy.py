import pygame
from BaseEntity import BaseEntity

class Enemy(BaseEntity):
    def __init__(self, id, name, image, hp, defense, attack, speed, radar_range):
        super().__init__(name, id, image, hp, defense, attack, speed, radar_range)

        self._x = 0
        self._y = 0
        self._direction = pygame.math.Vector2(0, 0)

        self._rect = pygame.Rect(self._x, self._y, 64, 64) 
        self._hitbox = pygame.Rect(self._x +16, self._y + 8, 32, 48)

    def entity_type(self):
        return "Enemy"

    def entity_info(self):
        return (f"ID: {self.id}"
        f"Name: {self.name}"
        f"HP: {self.hp}"
        f"Defense: {self.defense}"
        f"Attack: {self.attack}"
        f"Speed: {self.speed}"
        f"Radar Range: {self.radar_range}"
        f"Image: {self.image}")
    
    def pos(self):
        return self._x, self._y

