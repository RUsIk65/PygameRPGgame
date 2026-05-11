from base_entity import BaseEntity

class NPS(BaseEntity):
    def __init__(self, id, name, image, hp, defense, attack, speed, radar_range):
        super().__init__(name, id, image, hp, defense, attack, speed, radar_range)
        self.shop = []

    def entity_type(self):
        return "NPS"
    
    def entity_info(self):
        return (f"ID: {self.id}"
        f"Name: {self.name}"
        f"HP: {self.hp}"
        f"Defense: {self.defense}"
        f"Attack: {self.attack}"
        f"Speed: {self.speed}"
        f"Radar Range: {self.radar_range}"
        f"Image: {self.image}"
        f"Shop: {self.shop}")
    
    def get_shop(self):
        return self.shop
    
    def add_to_shop(self, item):
        self.shop.append(item)

    def sell_item(self, item_id, player):
        for item in self._shop:
            if item["id"] == item_id:

                if player.gold <= item["price"]:
                    return "Not enough gold"
                
                
                player.gold -= item["price"]

                player.inventory.append(item)

                return f"Player bought {item['name']}"
                
        return "Item not found"
    
    def buy_item(self, item_id, player, scam = 0.75):
        for item in self._shop:

            if item["id"] == item_id:

                sell_price = int(item["price"] * scam)
                
                player.gold += sell_price

                player.inventory.remove(item)

                return f"Sold {item['name']}"
            
        return "Item not found"