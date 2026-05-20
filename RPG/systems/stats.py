import random


class Stats:

    def __init__(
        self,
        hp=0,
        mana=0,
        attack=0,
        defense=0,
        speed=0,
        attack_range=0,
        crit_chance=0,
        level = 1
    ):

        # Уровень 
        self._level = level
        self.xp = 0
        self._xp_to_next_level = 100

        # БАЗОВЫЕ значения
        self._base_hp = hp
        self._base_mana = mana
        self._base_attack = attack
        self._base_defense = defense

        # Расчёт с учётом уровня
        self._max_hp = int(self._base_hp * 1.20 * self._level)
        self._max_mana = int(self._base_mana * 1.15 * self._level)

        self.current_hp = self._max_hp
        self.current_mana = self._max_mana

        self._attack = int(self._base_attack * 1.15 * self._level)
        self._defense = int(self._base_defense * 1.10 * self._level)

        self._speed = speed
        self._attack_range = attack_range
        self._crit_chance = crit_chance

        self._xp_to_next_level = int(self._xp_to_next_level * 1.35 * self._level)
            
    # система XP   
    def add_xp(self, amount):
        self.xp += amount

        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()
   
    # LEVEL UP
  
    def level_up(self):
        self.level += 1
        self.current_hp = self.max_hp
        self.current_mana = self.max_mana

        print(f"LEVEL UP! New level: {self.level}")

    
    def show_stats(self):
        print("====== PLAYER STATS ======")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}/{self.xp_to_next_level}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Mana: {self.current_mana}/{self.max_mana}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Attack Range: {self.attack_range}")
        print("==========================")
