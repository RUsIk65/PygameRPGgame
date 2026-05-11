import random

class Stats:
    def __init__(self, hp=100, mana=50, 
                 attack=10, 
                 defense=5, 
                 speed=4, 
                 charisma=10, 
                 attack_range=50, 
                 level=1):
        
    self.level = level
        self.xp = 0
        self.xp_to_next_level = 100
    
    self.max_hp = hp
        self.current_hp = hp