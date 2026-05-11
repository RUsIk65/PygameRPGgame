from abc import ABC, abstractmethod

class BaseEntity(ABC):
    def __init__(self, name, id, image, hp, defense=0, attack=0, speed=0, radar_range=0):
        self._name = name
        self._id = id
        self._image = image
        self._hp = hp
        self._defense = defense
        self._attack = attack
        self._speed = speed
        self._radar_range = radar_range

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def hp(self):
        return self._hp

    @property
    def image(self):
        return self._image

    @property
    def defense(self):
        return self._defense

    @property
    def attack(self):
        return self._attack

    @property
    def speed(self):
        return self._speed

    @property
    def radar_range(self):
        return self._radar_range

    @radar_range.setter
    def radar_range(self, radar_range):
        self._radar_range = radar_range

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @name.setter
    def name(self, name):
        self._name = name

    @id.setter
    def id(self, id):
        self._id = id

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @image.setter
    def image(self, image):
        self._image = image

    @abstractmethod
    def entity_type(self):
        pass

    @abstractmethod
    def is_live(self):
        return self._hp > 0
    
    @abstractmethod
    def entity_info(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        effective_damage = max(0, damage - self._defense)
        self._hp = max(0, self._hp - effective_damage)
        return effective_damage
    
    @abstractmethod
    def attack_entity(self, target):
        if self.is_live():
            damage_dealt = target.take_damage(self._attack)
            return damage_dealt
        return 0