import random


class Stats:

    def __init__(
        self,
        hp=100,
        mana=50,
        attack=10,
        defense=5,
        speed=4,
        charisma=10,
        attack_range=50,
        level=0
    ):

        # Уровень 
        self.level = level
        self.xp = 0
        self.xp_to_next_level = 100

        
        self.max_hp = hp
        self.current_hp = hp

        self.max_mana = mana
        self.current_mana = mana

        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.attack_range = attack_range

    
    # система XP
   

    def add_xp(self, amount):
        self.xp += amount

        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()

    
    # LEVEL UP
  
    def level_up(self):
        self.level += 1

        #self.max_hp = int(self.max_hp * 1.20 * self.level)
        self.current_hp = self.max_hp

        #self.max_mana = int(self.max_mana * 1.15)
        self.current_mana = self.max_mana


        #self.attack = int(self.attack * 1.15)

        #self.defense = int(self.defense * 1.10)

        #self.speed = int(self.speed * 1.15)

        # self.attack_range = int(self.attack_range * 1.05)

        # self.xp_to_next_level = int(self.xp_to_next_level * 1.35)

        print(f"LEVEL UP! New level: {self.level}")

    #система урона

    # def take_damage(self, damage):
    #     final_damage = max(0, damage - self.defense)

    #     self.current_hp -= final_damage

    #     if self.current_hp < 0:
    #         self.current_hp = 0

    #     return final_damage

    #хилка

    def heal(self, amount):
        self.current_hp += amount

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

  
    #система маны

    def use_mana(self, amount):
        if self.current_mana >= amount:
            self.current_mana -= amount
            return True

        return False

 
    
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
