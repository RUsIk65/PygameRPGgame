import pygame 
from base_entity import BaseEntity
from system.stats import Stats

class Player(BaseEntity):
    def __init__(self, id, name, image, hp, defense=0, attack=0, speed=5, radar_range=0):
        super().__init__(id, name, image, hp, defense, attack, speed, radar_range)

        self._x = 0
        self._y = 0
        self._direction = pygame.math.Vector2(0, 0)

        self._rect = pygame.Rect(self._x, self._y, 64, 64) 
        self._hitbox = pygame.Rect(self._x +16, self._y + 8, 32, 48)

        self.stats = Stats(hp=hp, mana=50, attack=attack, defense=defense, speed=speed)

        self._state = "idle" # жив не жив то и се

        self._weapon_type = None
        self._atack_cooldown = 0
        self._attack_cooldown_max = 500 #ms

    def entity_type(self):
        return "player"
    
    def update_hitbox(self):
        self._hitbox.x = self._rect.x +16
        self._hitbox.y = self._rect.y + 8
        
    def entity_info(self):
        return f"Player: {self._name} | Level: {self.stats.level} \nHP: {self.stats.current_hp}/{self.stats.max_hp} | Mana: {self.stats.current_mana}/{self.stats.max_mana}"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,  state):
        self._state = state
