import pygame 
from base_entity import BaseEntity
from systems.stats import Stats

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

    def change_state(self, new_state):
        valid_states = ["idle", "run", "attack", "death", "stun"]

        if self._state == "death":
            return
        if self._state == "stun" and new_state not in ["death"]:
            return 
        if new_state in valid_states:
            self._state = new_state

    def is_alive(self):
        return self.stats.current_hp > 0

    def update_state(self):
        if not self.is_alive():
            self.change_state("death")

    def move_to(self, target_x, target_y):
        target = pygame.math.Vector2(target_x, target_y)
        pos = pygame.math.Vector2(self._rect.x, self._rect.y)

        destance = target - pos

        if distance.length() < self.stats.speed:
            self._rect.x = target_x
            self._rect.y = target_y
            self.change_state("idle")
            self._direction = pygame.math.Vector2(0, 0)

        self._direction = distance.normalize()
        self._rect.x += self._direction.x * self.stats.speed
        self._rect.y += self._direction.y * self.stats.speed
        self.update_hitbox()
        self.change_state("run")

    def update(self, target_pos=None):
        if target_pos:
            self.move_to(target_pos[0], target_pos[1])
        self.update_state()
