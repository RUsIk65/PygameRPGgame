from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, id, cost, rareness, required_level):
        self._name = name
        self._id = id
        self._cost = cost
        self._rareness = rareness
        self._required_level = required_level

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
    def rareness(self):
        return self._rareness

    @property
    def required_level(self):
        return self._required_level

    @name.setter
    def name(self, name):
        self._name = name

    @id.setter
    def id(self, id):
        self._id = id
    
    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @rareness.setter
    def rareness(self, rareness):
        self._rareness = rareness

    @required_level.setter
    def required_level(self, required_level):
        self._required_level = required_level

    @abstractmethod
    def entity_type(self):
        pass
    
    @abstractmethod
    def entity_info(self):
        pass

class Weapon(Item):
    def __init__(self, name, id, cost, rareness, required_level, damage):
        super().__init__(name, id, cost, rareness, required_level)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def entity_type(self):
        return "Weapon"

    def entity_info(self):
        return (f"Weapon Name: {self._name}, Weapon ID: {self._id},"
                f"Cost: {self._cost}, Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}, Damage: {self._damage}" ) 

class Armor(Item):
    def __init__(self, name, id, cost, rareness, required_level, defense):
        super().__init__(name, id, cost, rareness, required_level)
        self._defense = defense

    @property
    def defense(self):
        return self._defense
    
    @defense.setter
    def defense(self, defense):
        self._defense = defense

    def entity_type(self):
        return "Armor"
    
    def entity_info(self):
        return (f"Armor Name: {self._name}, Armor ID: {self._id}," 
                f"Cost: {self._cost}, Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}, Defense: {self._defense}")
    
class Potion(Item):
    def __init__(self, name, id, cost, rareness, required_level, mana_restore):
        super().__init__(name, id, cost, rareness, required_level)
        self._mana_restore = mana_restore
    
    @property
    def mana_restore(self):
        return self._mana_restore

    @mana_restore.setter
    def mana_restore(self, mana_restore):
        self._mana_restore = mana_restore

    def entity_type(self):
        return "Potion"

    def entity_info(self):
        return (f"Potion Name: {self._name}, Potion ID: {self._id}, "
                f"Cost: {self._cost}, Rareness: {self._rareness}, "
                f"Required Level: {self._required_level}, Mana Restore: {self._mana_restore}")

class Food(Item):
    def __init__(self, name, id, cost, rareness, required_level, health_restore):
        super().__init__(name, id, cost, rareness, required_level)
        self._health_restore = health_restore

    @property
    def health_restore(self):
        return self._health_restore

    @health_restore.setter
    def health_restore(self, health_restore):
        self._health_restore = health_restore

    def entity_type(self):
        return "Food"
    
    def entity_info(self):
        return (f"Food Name: {self._name}, Food ID: {self._id},"
                f"Cost: {self._cost}, Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}, Health Restore: {self._health_restore}")

class Backpack(Item):
    def __init__(self, name, id, cost, rareness, required_level, capacity):
        super().__init__(name, id, cost, rareness, required_level)
        self._capacity = capacity
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def entity_type(self):
        return "Backpack"
    
    def entity_info(self):
        return (f"Backpack Name: {self._name}, Backpack ID: {self._id}," 
                f"Cost: {self._cost}, Rareness: {self._rareness}," 
                f"Required Level: {self._required_level}, Capacity: {self._capacity}")
    
