from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id, name, image, cost, rareness, required_level, max_stack=1):
        self._name = name
        self._id = id
        self._image = image
        self._cost = cost
        self._rareness = rareness
        self._required_level = required_level
        self._max_stack = max_stack

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def cost(self):
        return self._cost

    @property
    def image(self):
        return self._image

    @property
    def rareness(self):
        return self._rareness

    @property
    def required_level(self):
        return self._required_level

    @property
    def max_stack(self):
        return self._max_stack

    @name.setter
    def name(self, name):
        self._name = name

    @id.setter
    def id(self, id):
        self._id = id

    @image.setter
    def image(self, image):
        self._image = image
    
    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @rareness.setter
    def rareness(self, rareness):
        self._rareness = rareness

    @required_level.setter
    def required_level(self, required_level):
        self._required_level = required_level

    @max_stack.setter
    def max_stack(self, max_stack):
        self._max_stack = max_stack

    @abstractmethod
    def item_type(self):
        pass
    
    @abstractmethod
    def item_info(self):
        pass

class Weapon(Item):
    def __init__(self, id, name, image, cost, rareness, required_level, damage, max_stack=1):
        super().__init__(id, name, image, cost, rareness, required_level, max_stack)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def item_type(self):
        return "Weapon"

    def item_info(self):
        return (f"Weapon Name: {self._name}," 
                f"Weapon ID: {self._id},"
                f"Cost: {self._cost},"
                f"Max Stack: {self._max_stack},"
                f"Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}," 
                f"Damage: {self._damage}" ) 
    
    def eqiup_weapon(self, player):
        player.damage += self._damage

class Armor(Item):
    def __init__(self, id, name, image, cost, rareness, required_level, defense, max_stack=1):
        super().__init__(id, name, image, cost, rareness, required_level, max_stack)
        self._defense = defense

    @property
    def defense(self):
        return self._defense   
    
    @defense.setter
    def defense(self, defense):
        self._defense = defense

    def item_type(self):
        return "Armor"
    
    def item_info(self):
        return (f"Armor Name: {self._name}," 
                f"Armor ID: {self._id}," 
                f"Cost: {self._cost}," 
                f"Max Stack: {self._max_stack},"
                f"Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}," 
                f"Defense: {self._defense}," 
                f"Max Stack: {self._max_stack}")

    def eqiup_armor(self, target):
        target.defense += self.defense

    
    
class Potion(Item):
    def __init__(self, id, name, image, cost, rareness, required_level, mana_restore, max_stack=100):
        super().__init__(id, name, image, cost, rareness, required_level, max_stack)
        self._mana_restore = mana_restore
    
    @property
    def mana_restore(self):
        return self._mana_restore    

    @mana_restore.setter
    def mana_restore(self, mana_restore):
        self._mana_restore = mana_restore

    def item_type(self):
        return "Potion"

    def item_info(self):
        return (f"Potion Name: {self._name}," 
                f"Potion ID: {self._id}," 
                f"Cost: {self._cost}," 
                f"Max Stack: {self._max_stack},"
                f"Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}," 
                f"Mana Restore: {self._mana_restore}")
    
    def use_potion(self, target):
        target.current_mana += self._mana_restore
        if target.max_mana < target.current_mana:
            target.current_mana = target.max_mana
    


class Food(Item):
    def __init__(self, id, name, image, cost, rareness, required_level, health_restore, max_stack=100):
        super().__init__(id, name, image, cost, rareness, required_level, max_stack)
        self._health_restore = health_restore
    @property
    def health_restore(self):
        return self._health_restore
    
    @health_restore.setter
    def health_restore(self, health_restore):
        self._health_restore = health_restore

    def item_type(self):
        return "Food"
    
    def item_info(self):
        return (f"Food Name: {self._name}," 
                f"Food ID: {self._id}," 
                f"Cost: {self._cost}," 
                f"Max Stack: {self._max_stack}," 
                f"Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}," 
                f"Health Restore: {self._health_restore}")

    def use_food(self, target):
        target.current_hp += self._health_restore
        if target.current_hp > target.max_hp:
            target.current_hp = target.max_hp

  

class Backpack(Item):
    def __init__(self, id, name, image, cost, rareness, required_level, capacity, max_stack=1):
        super().__init__(id, name, image, cost, rareness, required_level, max_stack)
        self._capacity = capacity
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def item_type(self):
        return "Backpack"
    
    def item_info(self):
        return (f"Backpack Name: {self._name}," 
                f"Backpack ID: {self._id}," 
                f"Cost: {self._cost}," 
                f"Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}," 
                f"Capacity: {self._capacity}," 
                f"Max Stack: {self._max_stack}")

weapons = []
armors = []
potions = []
foods = []
backpacks = []
items = []

def set_items(item):
    items.append(item)
def set_weapons(weapon):
    weapons.append(weapon)

def set_armors(armor):
    armors.append(armor)

def set_potions(potion):
    potions.append(potion)

def set_foods(food):
    foods.append(food)

def set_backpacks(backpack):
    backpacks.append(backpack)