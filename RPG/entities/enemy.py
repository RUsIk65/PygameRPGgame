from base_entity import BaseEntity

class Enemy(BaseEntity):
    def __init__(self, id, name, image, hp, defense, attack, speed, radar_range):
        super().__init__(name, id, image, hp, defense, attack, speed, radar_range)

    def entity_type(self):
        return "Enemy"

    def entity_info(self):
        return (f"ID: {self.id}"
        f"Name: {self.name}"
        f"HP: {self.hp}"
        f"Defense: {self.defense}"
        f"Attack: {self.attack}"
        f"Speed: {self.speed}"
        f"Radar Range: {self.radar_range}"
        f"Image: {self.image}")
    
