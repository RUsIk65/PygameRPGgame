import random
from systems.combat import 

class Combat:

    def calculate_damage(self, attacker, target):

        dodge_chance = target.speed * 2
        if random.randint(1, 100) <= dodge_chance:
            return 0, False 

        base_damage = attacker.attack - target.defense

        if base_damage < 0:
            base_damage = 0
            
        crit_chance = 5
        is_crit = random.randint(1, 100) <= crit_chance

        if is_crit:
            base_damage *= 2

        return base_damage, is_crit
