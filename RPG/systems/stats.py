import random


class Stats:

    def __init__(
        self,
        hp=100,
        mana=50,
        attack=20,
        defense=10,
        speed=10,
        attack_range=0,
        crit_chance=0,
        level=1
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

    # ── Properties 

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        # Пересчитываем статы при смене уровня
        self._max_hp = int(self._base_hp * 1.20 * self._level)
        self._max_mana = int(self._base_mana * 1.15 * self._level)
        self._attack = int(self._base_attack * 1.15 * self._level)
        self._defense = int(self._base_defense * 1.10 * self._level)

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def max_mana(self):
        return self._max_mana

    @property
    def xp_to_next_level(self):
        return self._xp_to_next_level

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def speed(self):
        return self._speed

    @property
    def attack_range(self):
        return self._attack_range

    @property
    def crit_chance(self):
        return self._crit_chance

    # ── XP система 

    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()

    # ── Level Up

    def level_up(self):
        self.level += 1
        self._xp_to_next_level = int(100 * 1.35 * self._level)
        self.current_hp = self.max_hp
        self.current_mana = self.max_mana
        print(f"LEVEL UP! New level: {self.level}")

    # ── Heal 

    def heal(self, amount):
        self.current_hp = min(self.max_hp, self.current_hp + amount)

    # ── Show stats

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
